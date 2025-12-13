from flask import Flask, request, jsonify
import threading
import requests
import time

# === Input IP Address of Smart Flashlight Device ===
ip = input("Enter the IP address of the smart light (e.g., 192.168.1.2): ")
smart_light_IP = f"http://{ip}:5000"

# === OOP Class: Flashlight ===
class SmartFlashlight:
    def __init__(self):
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        return "Smart Flashlight is ON"

    def turn_off(self):
        self.state = "off"
        return "Smart Flashlight is OFF"

    def get_state(self):
        return self.state

# === OOP Controller ===
class FlashController:
    def __init__(self, flashlight):
        self.flashlight = flashlight

    def handle_action(self, action):
        if action == "on":
            return self.flashlight.turn_on()
        elif action == "off":
            return self.flashlight.turn_off()
        else:
            return "Invalid action"

# === Flask Setup ===
app = Flask(__name__)
smart_light = SmartFlashlight()
controller = FlashController(smart_light)

@app.route('/flash', methods=['POST'])
def control_flash():
    data = request.get_json()
    action = data.get("action", "")
    result = controller.handle_action(action)
    return jsonify({
        "status": result,
        "current_state": smart_light.get_state()
    })

# === Run Flask Server in Background ===
def run_server():
    app.run(host='0.0.0.0', port=5000)

server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# === Client Functions ===
def flash_on():
    response = requests.post(f"{smart_light_IP}/flash", json={"action": "on"})
    print("Flash ON →", response.json())

def flash_off():
    response = requests.post(f"{smart_light_IP}/flash", json={"action": "off"})
    print("Flash OFF →", response.json())

def blink():
    n = 5  # Number of blinks
    print("Blinking...")
    while n:
        flash_on()
        time.sleep(0.3)
        flash_off()
        time.sleep(0.3)
        n -= 1

# === Main Menu ===
if __name__ == "__main__":
    print("\nSmart Flashlight Controller\n")
    while True:
        print("\nSelect an action:")
        print("1. Flash ON")
        print("2. Flash OFF")
        print("3. Blink 3 Times")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            flash_on()
        elif choice == "2":
            flash_off()
        elif choice == "3":
            blink()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
