void setup() {
  Serial.begin(115200);
  analogReadResolution(12);  // 0–4095
}

void loop() {
  // Read A0…A3 (on Teensy 4.1 these map to pins 14–17)
  int v0 = analogRead(A16);
  int v1 = analogRead(A17);
  int v2 = analogRead(A0);
  int v3 = analogRead(A1);

  // Print space-separated values, ending with newline
  Serial.print(v0); Serial.print(' ');
  Serial.print(v1); Serial.print(' ');
  Serial.print(v2); Serial.print(' ');
  Serial.println(v3);

  delay(10);  // ~100 Hz sample rate
}
