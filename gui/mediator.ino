#include <WiFi.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

const char* server_ip = "192.168.1.100";  // Replace with your laptop's local IP
const int server_port = 8080;

WiFiClient client;

// UART pins
#define RXD2 16
#define TXD2 17

void setup() {
  Serial.begin(115200);        // Serial for debugging
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2); // UART with Rover

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected.");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (!client.connected()) {
    Serial.println("Connecting to server...");
    if (client.connect(server_ip, server_port)) {
      Serial.println("Connected to server!");
    } else {
      Serial.println("Connection failed.");
      delay(2000);
      return;
    }
  }

  // Forward Rover telemetry to Ground Station
  if (Serial2.available()) {
    String telemetry = Serial2.readStringUntil('\n');
    client.println(telemetry);
    Serial.print("Sent telemetry: ");
    Serial.println(telemetry);
  }

  // Receive commands from Ground Station and send to Rover
  if (client.available()) {
    String command = client.readStringUntil('\n');
    Serial2.println(command);
    Serial.print("Received command: ");
    Serial.println(command);
  }
}

