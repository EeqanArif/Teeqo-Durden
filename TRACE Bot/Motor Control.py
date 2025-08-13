#include <Servo.h>  // Include the Servo library

// ==========================
// Servo Motor Definitions
// ==========================

Servo lm, rm, lf, rf, lb, rb;  // Servo objects

// ==========================
// DC Motor Pin Definitions
// ==========================

// Motor 1 (Left Front)
const int M1_IN1 = 20;
const int M1_IN2 = 21;

// Motor 2 (Left Middle)
const int M2_IN1 = 16;
const int M2_IN2 = 17;

// Motor 3 (Left Rear)
const int M3_IN1 = 25;
const int M3_IN2 = 27;

// Motor 4 (Right Front)
const int M4_IN1 = 3;
const int M4_IN2 = 2;

// Motor 5 (Right Middle)
const int M5_IN1 = 14;
const int M5_IN2 = 15;

// Motor 6 (Right Rear)
const int M6_IN1 = 19;
const int M6_IN2 = 23;

void setup() {
  Serial.begin(9600);

  // Set all DC motor pins as output
  pinMode(M1_IN1, OUTPUT); pinMode(M1_IN2, OUTPUT);
  pinMode(M2_IN1, OUTPUT); pinMode(M2_IN2, OUTPUT);
  pinMode(M3_IN1, OUTPUT); pinMode(M3_IN2, OUTPUT);
  pinMode(M4_IN1, OUTPUT); pinMode(M4_IN2, OUTPUT);
  pinMode(M5_IN1, OUTPUT); pinMode(M5_IN2, OUTPUT);
  pinMode(M6_IN1, OUTPUT); pinMode(M6_IN2, OUTPUT);

  // Attach servos to correct pins
  lm.attach(6);   // Left Middle
  rm.attach(7);   // Right Middle
  lf.attach(8);   // Left Front
  rf.attach(10);  // Right Front
  lb.attach(12);  // Left Back
  rb.attach(13);  // Right Back

  setServoAngle(70); // All forward (0° mapped to 70)
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    handleMotorCommand(cmd);
    handleServoCommand(cmd);
  }
}

// ==========================
// Motor Control
// ==========================

void moveForward() {
  digitalWrite(M1_IN1, HIGH); digitalWrite(M1_IN2, LOW);
  digitalWrite(M2_IN1, HIGH); digitalWrite(M2_IN2, LOW);
  digitalWrite(M3_IN1, HIGH); digitalWrite(M3_IN2, LOW);
  digitalWrite(M4_IN1, HIGH); digitalWrite(M4_IN2, LOW);
  digitalWrite(M5_IN1, HIGH); digitalWrite(M5_IN2, LOW);
  digitalWrite(M6_IN1, HIGH); digitalWrite(M6_IN2, LOW);
}

void moveBackward() {
  digitalWrite(M1_IN1, LOW); digitalWrite(M1_IN2, HIGH);
  digitalWrite(M2_IN1, LOW); digitalWrite(M2_IN2, HIGH);
  digitalWrite(M3_IN1, LOW); digitalWrite(M3_IN2, HIGH);
  digitalWrite(M4_IN1, LOW); digitalWrite(M4_IN2, HIGH);
  digitalWrite(M5_IN1, LOW); digitalWrite(M5_IN2, HIGH);
  digitalWrite(M6_IN1, LOW); digitalWrite(M6_IN2, HIGH);
}

void turnLeft() {
  digitalWrite(M1_IN1, LOW); digitalWrite(M1_IN2, LOW);
  digitalWrite(M2_IN1, LOW); digitalWrite(M2_IN2, LOW);
  digitalWrite(M3_IN1, LOW); digitalWrite(M3_IN2, LOW);

  digitalWrite(M4_IN1, HIGH); digitalWrite(M4_IN2, LOW);
  digitalWrite(M5_IN1, HIGH); digitalWrite(M5_IN2, LOW);
  digitalWrite(M6_IN1, HIGH); digitalWrite(M6_IN2, LOW);
}

void turnRight() {
  digitalWrite(M1_IN1, HIGH); digitalWrite(M1_IN2, LOW);
  digitalWrite(M2_IN1, HIGH); digitalWrite(M2_IN2, LOW);
  digitalWrite(M3_IN1, HIGH); digitalWrite(M3_IN2, LOW);

  digitalWrite(M4_IN1, LOW); digitalWrite(M4_IN2, LOW);
  digitalWrite(M5_IN1, LOW); digitalWrite(M5_IN2, LOW);
  digitalWrite(M6_IN1, LOW); digitalWrite(M6_IN2, LOW);
}

void stopMotors() {
  digitalWrite(M1_IN1, LOW); digitalWrite(M1_IN2, LOW);
  digitalWrite(M2_IN1, LOW); digitalWrite(M2_IN2, LOW);
  digitalWrite(M3_IN1, LOW); digitalWrite(M3_IN2, LOW);
  digitalWrite(M4_IN1, LOW); digitalWrite(M4_IN2, LOW);
  digitalWrite(M5_IN1, LOW); digitalWrite(M5_IN2, LOW);
  digitalWrite(M6_IN1, LOW); digitalWrite(M6_IN2, LOW);
}

void handleMotorCommand(char cmd) {
  switch (cmd) {
    case 'w': moveForward(); break;
    case 's': moveBackward(); break;
    case 'a': turnLeft(); break;
    case 'd': turnRight(); break;
    case 'x': stopMotors(); break;
  }
}

// ==========================
// Servo Control
// ==========================

void setServoAngle(int angle) {
  lm.write(angle);
  rm.write(angle);
  lf.write(angle);
  rf.write(angle);
  lb.write(angle);
  rb.write(angle);
}

void handleServoCommand(char cmd) {
  switch (cmd) {
    case 'c': setServoAngle(70); break;   // 0°
    case 'v': setServoAngle(125); break;  // 45°
    case 'b': setServoAngle(180); break;  // 90°
  }
}
