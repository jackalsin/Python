const int signalPin= 0; //yellow wire connects to analog pin A0
const int LEDPin= 13; //LED connects to digital pin 13
int signal;//this variable, signal, will hold the analog value read by the arduino

void setup() {
Serial.begin(9600); //sets the baud rate for data transfer in bits/second 
pinMode(signalPin, INPUT); //the infrared sensor signal line will be an input to the arduino
pinMode(LEDPin, OUTPUT); //the LED serves an output in the circuit
}

void loop() {
signal= analogRead(signalPin); //arduino reads the value from the infrared sensor
Serial.println(signal); //prints out analog value
delay(500); //delays the next analog reading by 500 ms or a half a second 

if(signal < 200){ //if the analog value is less than 200, the object is within a few inches
digitalWrite(LEDPin, HIGH);
}
else{
digitalWrite(LEDPin, LOW);
}
}
