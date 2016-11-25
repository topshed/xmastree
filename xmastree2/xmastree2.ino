int i;
int p;
int r;
int leds[7][2] ={
  {6,7},
  {7,6},
  {4,5},
  {7,4},
  {4,7},
  {5,4},
  {6,5}
};

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  randomSeed(analogRead(0));
}

void gen_on(int nodes[]){
  for (i = 4; i < 8;i++){
    pinMode(i, INPUT);
  }
  pinMode(nodes[0], OUTPUT);
  pinMode(nodes[1], OUTPUT);
  digitalWrite(nodes[0], HIGH);
  digitalWrite(nodes[1], LOW);
}

void all_off(){
  for (i = 4; i < 8;i++){
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
}

void led_seq(){
  for (p =0; p <7; p++){
  all_off();
  gen_on(leds[p]);
  delay(100);
  all_off();
  delay(100);
  }
}

void led_rand(){
  r = random(7);
  all_off();
  gen_on(leds[r]);
  delay(50);
  all_off();
  delay(50);
}
// the loop function runs over and over again forever
void loop() {
 led_rand();
}
