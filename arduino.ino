int scale = 200;
boolean micro_is_5V = true; 

void setup() {
  // Initialize serial communication at 115200 baud
  Serial.begin(115200);
}

void loop() {
  // Get raw accelerometer data for each axis
  int rawX = analogRead(A0);
  float scaledX // Scaled values for each axis
  if (micro_is_5V) { // microcontroller runs off 5V
    scaledX = map(rawX, 0, 675, -scale, scale); // 3.3/5 * 1023 =~ 675
  } else { // microcontroller runs off 3.3V
    scaledX = map(rawX, 0, 1023, -scale, scale);
  }
  
  // Print out scaled X accelerometer readings
  Serial.print(millis());
  Serial.print(" ");
  Serial.print(scaledX);
  Serial.print("\n");
}
