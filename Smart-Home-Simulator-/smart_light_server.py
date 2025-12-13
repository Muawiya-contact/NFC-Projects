from flask import Flask, request, jsonify
import os

# === OOP Class: Smart Flashlight ===
class SmartFlashlight:
    def __init__(self):
        self.state = "off"

    def turn_on(self):
        os.system("termux-torch on")
        self.state = "on"
        return "Smart Flashlight is ON"

    def turn_off(self):
        os.system("termux-torch off")
        self.state = "off"
        return "Smart Flashlight is OFF"

    def get_state(self):
        return self.state

# === OOP Controller Class ===
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

# === Flask App Setup ===
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

if __name__ == '__main__':
    print("🚀 Smart Light Server is running on your phone...")
    app.run(host='0.0.0.0', port=5000)
