int incomingByte = 0; // for incoming serial data
int dir = 0;


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600); // opens serial port, sets data rate to 9600 bps

}

void loop() {
 
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = char(Serial.read());

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte);

    if (incomingByte == 108)  {
//      if (dir==0) {
//        dir =1;
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
//      }
//      else{
//        dir = 1;
//      }
  
    }
    else if  (incomingByte == 114){
//      if (dir==1) {
//        dir =0;
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
//      }
//      else{
//        dir = 0;
//      }
    }
    
  }
}
