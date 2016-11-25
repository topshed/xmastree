int led1[] = {6,7};
int led2[] = {7,6};
int led3[] = {7,4};
int led4[] = {4,7};
int led5[] = {5,4};
int led6[] = {4,5};
int led7[] = {6,5};
int i;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.

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
// the loop function runs over and over again forever
void loop() {
  
  all_off();
  gen_on(led1);
  delay(100);
  all_off();
  gen_on(led2);
  delay(100);
  gen_on(led3);
  delay(100);
  gen_on(led4);
  delay(100);
  gen_on(led5);
  delay(100);
  gen_on(led6);
  delay(100);
  gen_on(led7);
  delay(100);
}
