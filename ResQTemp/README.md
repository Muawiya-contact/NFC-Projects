# ResQTemp

A temperature monitoring and rescue-alert system built as a semester project for
Computer Organization & Assembly Language (COAL). An ESP8266 reads an LM35
temperature sensor, serves a small web dashboard over its own Wi-Fi access
point, and if the temperature stays above a safe threshold for too long it
drives a GSM module with AT commands to send an emergency SMS and place a call.

## How it works

- The LM35 on pin A0 is sampled every 500 ms; the safe limit is 33 °C.
- Below the threshold a green LED stays on. Above it, the red LED and buzzer
  activate and a hold timer starts (5 s in real mode, 10 s in demo mode).
- If the temperature is still high when the timer expires, the ESP8266 steps
  through a GSM sequence over serial (`AT+CMGF`, `AT+CMGS` to text the
  configured phone number, then `ATD` to call and `ATH` to hang up).
- The dashboard, served on port 80, shows the live temperature and state
  (Normal / Alert / Calling) and has buttons to toggle demo mode (persisted in
  EEPROM), cancel an in-progress call, and reset the ESP.
- Demo mode simulates a rising temperature so the alert flow can be shown
  without actually heating the sensor.

## Repository layout

- `assembly/esp.c++` — the full Arduino sketch for the ESP8266 (sensor
  reading, web server, embedded dashboard page, GSM state machine).
- `esp_web/main.html` — standalone copy of the dashboard page.
- `Circuit/circuit-diagram.jpeg` — wiring diagram.
- `doc/RQT-Proposal.pdf`, `doc/RQT-Report.pdf` — project proposal and report.

## Hardware

ESP8266 (NodeMCU-style board), LM35 temperature sensor on A0, green/red/blue
LEDs on D1–D3, buzzer on D4, and a GSM module wired to the ESP's serial pins.
Powered at 5 V with the usual breadboard, jumpers, and resistors.

## Build and run

1. Open `assembly/esp.c++` in the Arduino IDE with the ESP8266 board package
   installed, plus the ArduinoJson library.
2. Adjust `phoneNumber` (and the AP credentials if you like) near the top of
   the sketch, then flash it to the board.
3. Connect to the Wi-Fi access point `ResQTemp` (password in the sketch) and
   open the ESP's IP in a browser (192.168.4.1 by default) to see the
   dashboard.

## Credits

Course: Computer Organization & Assembly Language (COAL), 3rd semester,
NFC IET Multan. Submitted to Prof. Ghulam Mustafa.

Team: Moavia Amir (2k24_BSAI_72, contactmuawia@gmail.com) and
Muhammad Dawood (2k24_BSAI_31, Mirzamuhammaddawood0098@gmail.com).
