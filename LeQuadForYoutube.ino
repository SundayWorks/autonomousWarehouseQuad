void setup() {
  // put your setup code here, to run once:

}

void loop() {
  
  string = "";
  
  ReadString();
  
  ManualControl(string);
}

void ReadString(){
  
  string = "";
  while(Serial.available() > 0)
  {
    c =(char) Serial.read();
    if(c=='/'){
      break;
    }
    
    string += c;
    
    Serial.flush();
  }
  
}


void ManualControl(String data){
  if(string != "")
  {
    String word1 = getValue(data, '_', 0);
    String word2 = getValue(data, '_', 1);
    
    if(word1=="TH"){
      th = word2.toInt();
      if(th>=1100 && th<2390){
        th = word2.toInt();
        Current_TH = th;
        bldc_Throttle.writeMicroseconds(th); //actually write the value to the motor
        Serial.print("Throttle speed :");Serial.println(bldc_Throttle.read());
      }
    }
    
    if(word1=="RD"){
      rd = word2.toInt();
      if(rd>=1100 && rd<1900){
        Current_RD = rd;
        bldc_Rudder.writeMicroseconds(rd); //actually write the value to the motor
        Serial.print("Rudder :");Serial.println(word2);
      }
    }
    
    if(word1=="AI"){
      ai = word2.toInt();
      if(ai>=1100 && ai<1900){
        Current_AI = ai;
        bldc_Aileron.writeMicroseconds(ai); //actually write the value to the motor
        Serial.print("Aileron :");Serial.println(word2);
      }
    }
    
    if(word1=="EL"){
      el = word2.toInt();
      if(el>=1100 && el<1900){
        Current_EL = el;
        bldc_Elevator.writeMicroseconds(el); //actually write the value to the motor
        Serial.print("Elevator :");Serial.println(word2);
      }
    }
    
    if(word1=="AUX"){
      if(word2=="ON"){
        Auxiliary(true);
        Serial.println("Self-Level is ON");
      }
      else if(word2=="OFF"){
        Auxiliary(false);
        Serial.println("Self-Level is OFF");
      }
    }
    
    if(word1=="ARM"){
      if(Current_TH == 1100){
        ArmModel();
        isArmed = true;
      }
      else{
        Serial.println("MSG_Cannot Arm Model because it's already armed or the default values are not well initialized.");
      }
    }
    
    if(word1=="DARM"){
      if(Current_TH == 1100){
        DisArmModel();
        isArmed = false;
      }
      else{
        Serial.println("MSG_Cannot Disarm Model because it's already flying.");
      }
    }
  }
}
