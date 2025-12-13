#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <EEPROM.h>
#include <ArduinoJson.h>

#define GREEN_LED D1
#define RED_LED   D2
#define BLUE_LED  D3
#define BUZZER    D4
#define LM35_PIN  A0

const char* ssid = "ResQTemp";
const char* password = "11223344";
ESP8266WebServer server(80);

const float REAL_TEMP_THRESHOLD = 33.0;
const unsigned long HOLD_TIME_REAL = 5000UL;   
const unsigned long HOLD_TIME_DEMO = 10000UL;  
const unsigned long LOOP_PERIOD_MS = 500UL;

float temperature = REAL_TEMP_THRESHOLD - 5;
bool demoMode = false;
bool alertSent = false;
bool isGsmActive = false;
bool cancelCallFlag = false;
unsigned long tempStartTime = 0;
unsigned long lastLoopTime = 0;

const int EEPROM_DEMO_ADDRESS = 0;
const int EEPROM_LOG_COUNT_ADDRESS = 1;
String phoneNumber = "03218010098";

const char PAGE[] PROGMEM = R"====(
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ResQTemp</title>
<style>
body{margin:0;font-family:sans-serif;background:#0f2027;color:white;}
.container{max-width:420px;margin:auto;padding:20px}
.card{background:rgba(255,255,255,0.12);border-radius:18px;padding:25px;text-align:center;position:relative;box-shadow:0 4px 6px rgba(0,0,0,0.1);}
.temp{font-size:60px;font-weight:bold;margin-bottom:10px;}
.status{margin-top:12px;padding:10px;border-radius:10px;font-weight:600;}
.normal{background:#2ecc71;color:#000;}
.alert{background:#e74c3c}
.calling{background:#3498db}
.btn-group{margin-top:20px}
button{width:100%;padding:12px;border-radius:10px;border:0;background:#f1c40f;font-size:15px;margin-top:10px;cursor:pointer;transition:background 0.2s;}
button.reset-btn{background:#e74c3c;color:white;}
button.cancel{background:#e74c3c;color:white;}
.indicator{position:absolute;top:15px;right:15px;width:12px;height:12px;border-radius:50%;}
.indicator.connected{background:#2ecc71;}
.indicator.disconnected{background:#e74c3c;}
.mode-info{font-size:14px;color:rgba(255,255,255,0.7);margin-top:10px;}
</style>
</head>
<body>
<div class="container">
<h3>ResQTemp System</h3>
<div class="card">
  <div class="indicator disconnected" id="conn"></div>
  <div class="temp" id="temp">--</div>
  <div class="status" id="status">Waiting...</div>
  <div class="mode-info" id="modeInfo"></div>
  <div class="mode-info" id="countdownInfo"></div>
  <div class="btn-group">
    <button id="demoBtn" onclick="toggleDemo()">Toggle Demo Mode</button>
    <button onclick="window.location.reload()">Refresh</button>
    <button class="reset-btn" onclick="resetEsp()">Reset ESP</button>
    <button id="cancelBtn" class="cancel" onclick="cancelCall()" style="display:none;">Cancel Call</button>
  </div>
  <div style="font-size:13px;margin-top:15px">Location: NFC-IET Multan Lab 114 AI Depart</div>
</div>
</div>
<script>
let lastUpdate=0;
function updateUI(d){
  lastUpdate=Date.now();
  document.getElementById("conn").className="indicator connected";
  document.getElementById("temp").innerHTML=d.temp+" °C";
  let st=document.getElementById("status");
  st.innerHTML=d.state;
  st.className="status "+d.state.toLowerCase();
  let demoBtn=document.getElementById("demoBtn");
  let modeInfo=document.getElementById("modeInfo");
  let countdownInfo=document.getElementById("countdownInfo");
  let cancelBtn=document.getElementById("cancelBtn");
  if(d.demo==="true"){
    demoBtn.innerText="Disable Demo Mode";
    modeInfo.innerHTML="Demo Mode Active (Simulation to "+d.limit+" °C)";
  }else{
    demoBtn.innerText="Enable Demo Mode";
    modeInfo.innerHTML="Real Mode Active (Threshold: "+d.limit+" °C)";
  }
  if(d.state==="NORMAL") st.innerHTML="Normal";
  if(d.state==="ALARM") st.innerHTML="Overheating Alert";
  if(d.state==="CALLING") st.innerHTML="Emergency Alert Sent";
  if(d.countdown>0 && d.state==="ALARM"){
    countdownInfo.innerHTML="Alert in: "+d.countdown+" sec";
    cancelBtn.style.display="block";
  } else {
    countdownInfo.innerHTML="";
    cancelBtn.style.display="none";
  }
}
function fetchData(){
  fetch('/data').then(r=>r.json()).then(updateUI).catch(()=>document.getElementById("conn").className="indicator disconnected");
}
function toggleDemo(){ fetch('/demo').then(()=>fetchData()); }
function resetEsp(){ fetch('/reset').then(()=>setTimeout(()=>{window.location.reload();},2500)); }
function cancelCall(){ fetch('/cancelCall').then(()=>fetchData()); }
fetchData();
setInterval(fetchData,1500);
setInterval(()=>{ if(Date.now()-lastUpdate>3000) document.getElementById("conn").className="indicator disconnected"; },1000);
</script>
</body>
</html>
)====";

void runGsmSequence(){
  static int gsmState=0;
  static unsigned long stateStartTime=0;

  if(cancelCallFlag){  // Stop GSM immediately
    gsmState = 0;
    cancelCallFlag = false;
    isGsmActive = false;
    return;
  }

  if(!isGsmActive) return;

  unsigned long now = millis();
  unsigned long dialDelay = demoMode ? HOLD_TIME_DEMO : HOLD_TIME_REAL;

  switch(gsmState){
    case 0:
      stateStartTime = now;
      gsmState = 1;
      break;
    case 1:
      if(now - stateStartTime >= 500){
        Serial.println("AT+CMGF=1");
        stateStartTime = now;
        gsmState = 2;
      }
      break;
    case 2:
      if(now - stateStartTime >= 500){
        Serial.print("AT+CMGS=\"");
        Serial.print(phoneNumber);
        Serial.println("\"");
        stateStartTime = now;
        gsmState = 3;
      }
      break;
    case 3:
      if(now - stateStartTime >= 500){
        Serial.println("ResQTemp Emergency: Temperature has crossed the safe limit!");
        stateStartTime = now;
        gsmState = 4;
      }
      break;
    case 4:
      if(now - stateStartTime >= 300){
        Serial.write(26); // CTRL+Z
        stateStartTime = now;
        gsmState = 5;
      }
      break;
    case 5:
      if(now - stateStartTime >= dialDelay){
        Serial.print("ATD");
        Serial.print(phoneNumber);
        Serial.println(";");
        stateStartTime = now;
        gsmState = 6;
      }
      break;
    case 6:
      if(now - stateStartTime >= 15000){
        Serial.println("ATH");
        isGsmActive = false;
        gsmState = 0;
      }
      break;
    default:
      gsmState = 0;
      break;
  }

  server.handleClient(); 
}

void startGsmAlert(){
  if(!isGsmActive){
    isGsmActive=true;
    cancelCallFlag=false;
    unsigned int count;
    EEPROM.get(EEPROM_LOG_COUNT_ADDRESS,count);
    count++;
    EEPROM.put(EEPROM_LOG_COUNT_ADDRESS,count);
    EEPROM.commit();
  }
}

void handleRoot(){ server.send_P(200,"text/html",PAGE); }
void handleResetEsp(){ server.send(200,"text/plain","Restarting..."); delay(500); ESP.restart(); }
void handleData(){
  StaticJsonDocument<200> doc;
  float limit = REAL_TEMP_THRESHOLD;
  String state = "NORMAL";
  unsigned long holdTime = demoMode ? HOLD_TIME_DEMO : HOLD_TIME_REAL;
  unsigned long remainingSec = 0;

  if(isGsmActive) state = "CALLING";
  else if(temperature>=limit){
    state = alertSent ? "CALLING" : "ALARM";
    if(tempStartTime>0) remainingSec = max(0UL,(holdTime-(millis()-tempStartTime))/1000UL);
  }

  doc["temp"] = String(temperature,1);
  doc["demo"] = demoMode ? "true" : "false";
  doc["state"] = state;
  doc["limit"] = String(limit,1);
  doc["countdown"] = remainingSec;

  String json; serializeJson(doc,json);
  server.send(200,"application/json",json);
}

void handleDemo(){
  demoMode = !demoMode;
  EEPROM.write(EEPROM_DEMO_ADDRESS, demoMode?1:0);
  EEPROM.commit();
  alertSent=false;
  tempStartTime=0;
  isGsmActive=false;
  cancelCallFlag=false;
  temperature = REAL_TEMP_THRESHOLD - 5;
  server.send(200,"text/plain", demoMode?"DEMO_ON":"DEMO_OFF");
}

void handleCancelCall(){
  if(isGsmActive || alertSent){
    cancelCallFlag = true;
    alertSent = false;
    isGsmActive = false;
  }
  server.send(200,"text/plain","CALL_CANCELED");
}


void setup(){
  Serial.begin(9600);
  delay(1000);

  EEPROM.begin(32);
  demoMode = (EEPROM.read(EEPROM_DEMO_ADDRESS)==1);

  pinMode(GREEN_LED,OUTPUT);
  pinMode(RED_LED,OUTPUT);
  pinMode(BLUE_LED,OUTPUT);
  pinMode(BUZZER,OUTPUT);

  digitalWrite(GREEN_LED,LOW);
  digitalWrite(RED_LED,LOW);
  digitalWrite(BLUE_LED,LOW);
  digitalWrite(BUZZER,LOW);
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);

  server.on("/", handleRoot);
  server.on("/data", handleData);
  server.on("/demo", handleDemo);
  server.on("/reset", handleResetEsp);
  server.on("/cancelCall", handleCancelCall);

  server.begin();
}

void readTemperature(){
  if(!demoMode) temperature = analogRead(LM35_PIN)*(3.3/1024.0)*100.0;
}

void simulateTempRise(){
  if(demoMode) temperature = min(temperature + 0.5 * (LOOP_PERIOD_MS/1000.0), REAL_TEMP_THRESHOLD + 5.0);
}

void handleAlert(float limit, unsigned long hold){
  unsigned long now = millis();
  if(temperature < limit){
    alertSent=false;
    tempStartTime=0;
    isGsmActive=false;
    cancelCallFlag=false;
    digitalWrite(GREEN_LED,HIGH);
    digitalWrite(RED_LED,LOW);
    digitalWrite(BLUE_LED,LOW);
    digitalWrite(BUZZER,LOW);
  } else {
    digitalWrite(GREEN_LED,LOW);
    digitalWrite(RED_LED,HIGH);
    digitalWrite(BLUE_LED,LOW);
    digitalWrite(BUZZER,HIGH);
    if(tempStartTime==0) tempStartTime=now;
    if(now-tempStartTime>=hold && !alertSent && !isGsmActive && !cancelCallFlag){
      alertSent=true;
      startGsmAlert();
    }
    if(alertSent){
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(RED_LED,LOW);
      digitalWrite(BLUE_LED,HIGH);
      digitalWrite(BUZZER,LOW);
    }
  }
}

void loop(){
  runGsmSequence();
  server.handleClient();
  unsigned long now = millis();
  if(now - lastLoopTime >= LOOP_PERIOD_MS){
    lastLoopTime = now;
    readTemperature();
    simulateTempRise();
    unsigned long hold = demoMode ? HOLD_TIME_DEMO : HOLD_TIME_REAL;
    handleAlert(REAL_TEMP_THRESHOLD, hold);
  }
}