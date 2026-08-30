# Stocks Trend Analyzer

A desktop tool for analyzing historical stock prices, built as a 3rd-semester
Data Structures & Algorithms project. You load a CSV of daily prices and the
app detects rising/falling streaks, computes a moving average, finds local
highs and lows, and picks the best single buy–sell interval, all plotted on a
Matplotlib chart embedded in a CustomTkinter GUI. The point of the project is
to back each analysis step with a hand-written data structure rather than
library shortcuts.

## How it works

- `dsa/` contains the custom structures: `ArrayList` (price/date storage),
  `Queue` (keeps a running sum for O(1) sliding-window averages), and `Stack`.
- `algorithms/trend_analysis.py` scans consecutive closes to track
  rising/falling streaks.
- `algorithms/moving_average.py` computes an N-day moving average with the
  queue as a sliding window.
- `algorithms/max_profit.py` finds the most profitable buy/sell days with a
  single O(n) pass (classic best-time-to-buy-and-sell).
- `algorithms/local_high_low.py` marks local highs and lows by comparing each
  point with its neighbors.
- `main.py` ties it together: load a CSV, set the moving-average window,
  click "Analyze Trends" to draw the chart (price line, MA line, buy/sell
  markers, high/low points), and "Save Chart" to write a PNG into `charts/`.

## Running it

Requires Python 3 with `customtkinter` and `matplotlib` installed
(`tkinter` ships with Python):

```
pip install customtkinter matplotlib
python main.py
```

The CSV needs `Date` and `Close` columns. Sample datasets are in `data/`
(`sample_stock01.csv` through `sample_stock04.csv` and `bitcoin.csv`), and
`data/random_csv_genrator.py` can generate more. The project proposal and
report PDFs are in `doc/`.

## Credits

Course: Data Structures & Algorithms (DSA), 3rd semester
Submitted to: Sir Hasnain Yousaf Khan

Team:
- Shazada M. Umar (2k24_BSAI_42)
- Moavia Amir (2k24_BSAI_72) — contactmuawia@gmail.com
- Faizan Ishfaq (2k24_BSAI_50)
- M. Hamza (2k24_BSAI_46)
