// By Coding Moves
// WiFi Controlled Car using NodeMCU (ESP8266)
// Project: Coding Moves RC+

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// Motor driver pin definitions
#define ENA   14  // Enable/speed motors Right  (D5)
#define ENB   12  // Enable/speed motors Left   (D6)
#define IN_1  15  // Motor IN1 (Right)          (D8)
#define IN_2  13  // Motor IN2 (Right)          (D7)
#define IN_3  2   // Motor IN3 (Left)           (D4)
#define IN_4  0   // Motor IN4 (Left)           (D3)

// WiFi settings
const char* ssid = "Coding Moves RC+";
const char* password = "codingmoves_123";

ESP8266WebServer server(80);

String command;              // Command received from mobile app
int speedCar = 800;          // Default speed
int speed_Coeff = 3;         // Coefficient for turning curves

void setup() {
  // Motor pin setup
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN_1, OUTPUT);
  pinMode(IN_2, OUTPUT);
  pinMode(IN_3, OUTPUT);
  pinMode(IN_4, OUTPUT);

  Serial.begin(115200);

  // Start WiFi access point
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);

  // Route handling
  server.on("/", HTTP_handleRoot);
  server.onNotFound(HTTP_handleRoot);
  server.begin();
}

// Movement functions
void goAhead() {
  digitalWrite(IN_1, LOW);  digitalWrite(IN_2, HIGH); analogWrite(ENA, speedCar);
  digitalWrite(IN_3, LOW);  digitalWrite(IN_4, HIGH); analogWrite(ENB, speedCar);
}

void goBack() {
  digitalWrite(IN_1, HIGH); digitalWrite(IN_2, LOW);  analogWrite(ENA, speedCar);
  digitalWrite(IN_3, HIGH); digitalWrite(IN_4, LOW);  analogWrite(ENB, speedCar);
}

void goRight() {
  digitalWrite(IN_1, LOW);  digitalWrite(IN_2, HIGH); analogWrite(ENA, speedCar);
  digitalWrite(IN_3, HIGH); digitalWrite(IN_4, LOW);  analogWrite(ENB, speedCar);
}

void goLeft() {
  digitalWrite(IN_1, HIGH); digitalWrite(IN_2, LOW);  analogWrite(ENA, speedCar);
  digitalWrite(IN_3, LOW);  digitalWrite(IN_4, HIGH); analogWrite(ENB, speedCar);
}

void goAheadRight() {
  digitalWrite(IN_1, LOW);  digitalWrite(IN_2, HIGH); analogWrite(ENA, speedCar / speed_Coeff);
  digitalWrite(IN_3, LOW);  digitalWrite(IN_4, HIGH); analogWrite(ENB, speedCar);
}

void goAheadLeft() {
  digitalWrite(IN_1, LOW);  digitalWrite(IN_2, HIGH); analogWrite(ENA, speedCar);
  digitalWrite(IN_3, LOW);  digitalWrite(IN_4, HIGH); analogWrite(ENB, speedCar / speed_Coeff);
}

void goBackRight() {
  digitalWrite(IN_1, HIGH); digitalWrite(IN_2, LOW);  analogWrite(ENA, speedCar / speed_Coeff);
  digitalWrite(IN_3, HIGH); digitalWrite(IN_4, LOW);  analogWrite(ENB, speedCar);
}

void goBackLeft() {
  digitalWrite(IN_1, HIGH); digitalWrite(IN_2, LOW);  analogWrite(ENA, speedCar);
  digitalWrite(IN_3, HIGH); digitalWrite(IN_4, LOW);  analogWrite(ENB, speedCar / speed_Coeff);
}

void stopRobot() {
  digitalWrite(IN_1, LOW);  digitalWrite(IN_2, LOW);  analogWrite(ENA, 0);
  digitalWrite(IN_3, LOW);  digitalWrite(IN_4, LOW);  analogWrite(ENB, 0);
}

// Handle incoming commands
void loop() {
  server.handleClient();
  command = server.arg("State");

  if      (command == "F") goAhead();
  else if (command == "B") goBack();
  else if (command == "L") goLeft();
  else if (command == "R") goRight();
  else if (command == "I") goAheadRight();
  else if (command == "G") goAheadLeft();
  else if (command == "J") goBackRight();
  else if (command == "H") goBackLeft();
  else if (command == "S") stopRobot();

  // Speed levels 0–9
  else if (command == "0") speedCar = 400;
  else if (command == "1") speedCar = 470;
  else if (command == "2") speedCar = 540;
  else if (command == "3") speedCar = 610;
  else if (command == "4") speedCar = 680;
  else if (command == "5") speedCar = 750;
  else if (command == "6") speedCar = 820;
  else if (command == "7") speedCar = 890;
  else if (command == "8") speedCar = 960;
  else if (command == "9") speedCar = 1023;
}

// Web server route
void HTTP_handleRoot() {
  if (server.hasArg("State")) {
    Serial.println(server.arg("State"));
  }
  server.send(200, "text/html", "");
  delay(1);
}
