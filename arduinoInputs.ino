//Joystick pins connected to A0 and A1 and button click pin is connected to 6 and the joystick itself is connected to pin A0/A1
const int joyX = A0;
const int joyY = A1;
const int ClickBtn = 6;
//const int joyBtn = 9; //leftclick
const int rBtn = 7;   //rightclick
const int reedSwitch = 8;
const int wkey = 4;
const int akey =3;
const int skey=2;
const int dkey =5;

void setup() {
//baud rate set to 115200
  Serial.begin(115200);

//sees pins for the buttons
//inputpullup uses internal built in resistors reads high as sensor off low sensor is on it reads the ground makes it so real resistors wont be needed
  pinMode(ClickBtn, INPUT_PULLUP);
  //pinMode(joyBtn, INPUT_PULLUP);
  pinMode(rBtn, INPUT_PULLUP);
  pinMode(reedSwitch,INPUT_PULLUP);
  pinMode(wkey,INPUT_PULLUP);
  pinMode(akey,INPUT_PULLUP);
  pinMode(skey,INPUT_PULLUP);
  pinMode(dkey,INPUT_PULLUP);

}
//joystick sits around position 512 so its subtracted to start at position 0 it reads from (-500,500)
void loop() {
  int x = analogRead(joyX) - 512;
  int y = analogRead(joyY) - 512;

//if button is low then it will be seen as pressed (1)
 
  int btn = (digitalRead(ClickBtn)==LOW)? 1:0;
  int btn2 = (digitalRead(rBtn)==LOW)? 1:0; 
 // int btn3 = (digitalRead(ClickBtn) == LOW) ? 1 : 0;
  int reed = (digitalRead(reedSwitch)==LOW)?1:0;
  int wBtn = (digitalRead(wkey)==LOW)?1:0;
  int aBtn = (digitalRead(akey)==LOW)?1:0;
  int sBtn = (digitalRead(skey)==LOW)?1:0;
  int dBtn = (digitalRead(dkey)==LOW)?1:0;

//prints position of x and y along with button inputs
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.print(btn);
  Serial.print(",");
  Serial.print(btn2);
  Serial.print(",");
 // Serial.print(btn3);
 // Serial.print(",");
  Serial.print(wBtn);
  Serial.print(",");
  Serial.print(aBtn);
  Serial.print(",");
  Serial.print(sBtn);
  Serial.print(",");
  Serial.print(dBtn);
  Serial.print(",");
  Serial.println(reed);

//delay to not overwhelm serial monitor
  delay(10);  
}
