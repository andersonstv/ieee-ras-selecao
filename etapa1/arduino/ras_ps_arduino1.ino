void setup()
{
  
}

// Funcao de piscar o led, dado um tempo determinado
void blink(int time){
  digitalWrite(12, HIGH);
  delay(time);
  digitalWrite(12, LOW);
  delay(time);
}

void loop()
{
  blink(500); // Pisca o led por 0,5s
  
  blink(1000); // Pisca o led por 1s
  
  blink(5000); // Pisca o led por 5s
}