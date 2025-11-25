import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dsa.array_list import ArrayList
from algorithms.trend_analysis import TrendAnalysis
from algorithms.moving_average import MovingAverage
from algorithms.max_profit import MaxProfit
from algorithms.local_high_low import LocalHighLow

class StockAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Stocks Trend Analyzer")
        master.geometry("950x700")

        # Variables
        self.prices = ArrayList()
        self.dates = ArrayList()
        self.window_size = tk.IntVar(value=5)  # Default moving average window

        # Widgets
        self.label = tk.Label(master, text="Stocks Trend Analyzer", font=("Arial", 18))
        self.label.pack(pady=10)

        self.load_button = tk.Button(master, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=5)

        frame = tk.Frame(master)
        frame.pack(pady=5)
        tk.Label(frame, text="Moving Average Window:").pack(side=tk.LEFT)
        self.window_entry = tk.Entry(frame, textvariable=self.window_size, width=5)
        self.window_entry.pack(side=tk.LEFT)

        self.analyze_button = tk.Button(master, text="Analyze Trends", command=self.analyze)
        self.analyze_button.pack(pady=5)

        self.save_button = tk.Button(master, text="Save Chart", command=self.save_chart)
        self.save_button.pack(pady=5)

        self.figure = plt.Figure(figsize=(8,5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master)
        self.canvas.get_tk_widget().pack(pady=20)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.prices.clear()
                self.dates.clear()
                for row in reader:
                    self.dates.append(row['Date'])
                    self.prices.append(float(row['Close']))
            messagebox.showinfo("Success", f"Loaded {self.prices.size()} records.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

    def analyze(self):
        if self.prices.size() == 0:
            messagebox.showwarning("Warning", "Please load a CSV first.")
            return

        try:
            window = int(self.window_entry.get())
            if window < 1:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Warning", "Window size must be a positive integer.")
            return

        # Trend detection
        trend_module = TrendAnalysis(self.prices)
        trends = trend_module.detect_trends()

        # Moving Average
        ma_module = MovingAverage(window)
        moving_avg = ma_module.calculate([self.prices.get(i) for i in range(self.prices.size())])

        # Max Profit
        max_profit_module = MaxProfit([self.prices.get(i) for i in range(self.prices.size())])
        buy_day, sell_day, profit = max_profit_module.best_interval()

        # Local High/Low
        lh_module = LocalHighLow([self.prices.get(i) for i in range(self.prices.size())])
        extremes = lh_module.find_local_extremes()

        # Plotting
        self.ax.clear()
        x_vals = [i for i in range(self.prices.size())]
        y_vals = [self.prices.get(i) for i in range(self.prices.size())]

        self.ax.plot(x_vals, y_vals, label="Close Price", color="blue")
        self.ax.plot(x_vals, moving_avg, label=f"{window}-Day MA", color="orange")

        # Mark buy/sell
        self.ax.scatter(buy_day, y_vals[buy_day], marker="^", color="green", s=100, label="Buy")
        self.ax.scatter(sell_day, y_vals[sell_day], marker="v", color="red", s=100, label="Sell")

        # Mark local highs/lows
        for idx, kind, price in extremes:
            color = "purple" if kind == "High" else "brown"
            self.ax.scatter(idx, price, color=color, marker="o", s=50)

        self.ax.set_title("Stock Trend Analysis")
        self.ax.set_xlabel("Day Index")
        self.ax.set_ylabel("Price")
        self.ax.legend()
        self.canvas.draw()

        messagebox.showinfo("Analysis Complete", f"Max Profit: {profit:.2f} (Buy day {buy_day}, Sell day {sell_day})")

    def save_chart(self):  

        project_dir = os.path.abspath(os.path.dirname(__file__))

        charts_dir = os.path.join(project_dir, "charts")
        os.makedirs(charts_dir, exist_ok=True)

        # Save chart
        save_path = os.path.join(charts_dir, "generated_charts.png")
        self.figure.savefig(save_path)
        messagebox.showinfo("Saved", f"Chart saved to {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockAnalyzerApp(root)
    root.mainloop()
