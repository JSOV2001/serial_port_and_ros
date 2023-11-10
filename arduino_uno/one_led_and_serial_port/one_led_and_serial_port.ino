//Serial port data's related variables
String data_str = ""; //Incoming data from serial port
int led_pwm_signal = 0; //PWM signal for actuator

//Hardware's related variables
int led_pin = 11; //LED's pin
float cur_led_bright = 0.0; //LED's Current bright
int max_led_bright = 25; //LED's Maximum bright
int min_led_bright = 0; //LED's Minimum bright
 
void setup() {
  Serial.begin(9600); //Beginning serial portT);
  Serial.println("Let's Go!");
} 

void loop() {
  //Doing nothing while serial port is NOT available
  while (!Serial.available());

  //Reading incoming data from serial port
  data_str = Serial.readString(); //Reading incoming data as a String datatype (common practice)
  Serial.println(data_str); //Printing incomming data (common practice)
  cur_led_bright = data_str.toInt(); //Converting incoming data to Int datatype

  //Getting the incoming data to a actuator
  led_pwm_signal = map(cur_led_bright, min_led_bright, max_led_bright, 0, 255); //Take the incoming data and convert it into a PWM signal
  analogWrite(led_pin, led_pwm_signal);
  delay(100);
  analogWrite(led_pin, 0);
} 
