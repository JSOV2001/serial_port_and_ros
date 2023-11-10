// Serial port's related variables
String incomming_data; //Incoming data from serial port
int individual_data_length = 2;

// Hardware's related variables
int max_led_bright = 25; //All LEDs' Maximum bright
int min_led_bright = 0; //All LEDs' Minimum bright

int led1_pin = 9; //LED 1's pin
float cur_led1_bright = 0; //LED 1's Current bright
int led1_first_char = 0; //LED 1's First Char 
int led1_final_char = led1_first_char + (individual_data_length - 1); //LED 1's Final Char
int led1_pwm_signal = 0; //PWM signal for actuator 1

int led2_pin = 11; //LED 2's pin
float cur_led2_bright = 0; //LED 2's Current bright
int led2_first_char = led1_final_char + 2; //LED 1's First Char 
int led2_final_char = led2_first_char + (individual_data_length - 1); //LED 1's Final Char
int led2_pwm_signal = 0; //PWM signal for actuator 2

void setup() {
  Serial.begin(9600); //Beginning serial port
  Serial.setTimeout(10); 
  
  pinMode(led1_pin, OUTPUT);
  pinMode(led1_pin, OUTPUT);
  
  Serial.println("Let's Go!");
} 

void loop() {
  // Processing incomming data
  // Doing nothing while serial port is NOT available
  while (!Serial.available());
  incomming_data= Serial.readString(); // Reading incoming data as a String datatype (common practice)
  Serial.print("Incomming Data: ");
  Serial.print(incomming_data);

  // Extracting value for each actuator from incoming data
  cur_led1_bright = incomming_data.substring(led1_first_char, led1_final_char + 1).toFloat(); // Value must be a float datatype
  cur_led2_bright = incomming_data.substring(led2_first_char, led2_final_char + 1).toFloat(); // Value must be a float datatype

  // Printing incomming data (common practice)
  Serial.print("\nLED 1's Bright: ");
  Serial.println(cur_led1_bright);
  Serial.print("LED 2's Bright: ");
  Serial.println(cur_led2_bright);

  // Getting PWM signal from incomming data
  led1_pwm_signal = map(cur_led1_bright, min_led_bright, max_led_bright, 0, 255); // Take the incoming data and convert it into a PWM signal
  led2_pwm_signal = map(cur_led2_bright, min_led_bright, max_led_bright, 0, 255); // Take the incoming data and convert it into a PWM signal

  // Sending PWM signal to actuators
  analogWrite(led1_pin, led1_pwm_signal);
  analogWrite(led2_pin, led2_pwm_signal);
  delay(500);
  analogWrite(led1_pin, 0);
  analogWrite(led2_pin, 0);
}
