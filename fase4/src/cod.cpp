#include <DHT.h>                  // Biblioteca para o sensor DHT22
#include <Wire.h>                 // Biblioteca para comunicação I2C
#include <LiquidCrystal_I2C.h>    // Biblioteca para o display LCD I2C

// Configuração do display LCD (Endereço 0x27, 20 colunas, 4 linhas)
LiquidCrystal_I2C lcd(0x27, 20, 4);

// Definição dos pinos
#define PINO_DHT 19          // Pino do DHT22
#define TIPO_DHT DHT22       // Tipo do sensor DHT
#define PINO_LDR 32          // Umidade do solo
#define PINO_RELE 21         // Controle do relé
#define PINO_POTASSIO 34     // Simular nível de potássio
#define PINO_FOSFORO 35      // Simular nível de fósforo

// Limites médios ideais
const int LIMITE_IDEAL_POTASSIO = 60;  // mg/dm³
const int LIMITE_IDEAL_FOSFORO = 15;  // mg/dm³

// Objeto DHT para o sensor
DHT dht(PINO_DHT, TIPO_DHT);

void setup() {
  Serial.begin(115200); // Inicialização do Monitor Serial
  dht.begin();          // Inicializa o sensor DHT

  // Configuração da comunicação I2C com pinos personalizados
  Wire.begin(18, 17); // SDA no GPIO18 e SCL no GPIO17

  // Configuração do display LCD
  lcd.begin(20, 4);      // display com 20 colunas e 4 linhas
  lcd.backlight();       // luz de fundo do LCD
  lcd.setCursor(0, 0);
  lcd.print("Inicializando...");
  delay(5000);           // Pausa para inicialização
}

void loop() {
  // Leitura dos sensores
  int valorUmidadeSolo = analogRead(PINO_LDR);
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  int nivelPotassio = analogRead(PINO_POTASSIO);
  int nivelFosforo = analogRead(PINO_FOSFORO);

  // Normalização dos valores
  int umidadeSoloPercent = map(valorUmidadeSolo, 0, 4095, 0, 100);
  int nivelPotassioMgDm3 = map(nivelPotassio, 0, 4095, 0, 100);
  int nivelFosforoMgDm3 = map(nivelFosforo, 0, 4095, 0, 30);

  // Controle da bomba de irrigação
  bool bombaLigada = umidadeSoloPercent < 30;
  digitalWrite(PINO_RELE, bombaLigada ? HIGH : LOW);

  // Envio de dados para o Serial Plotter com rótulos
  Serial.print("Temperatura(C):");
  Serial.print(temperatura);
  Serial.print(",Umidade(%):");
  Serial.print(umidade);
  Serial.print(",Solo(%):");
  Serial.print(umidadeSoloPercent);
  Serial.print(",Potassio(mg/dm3):");
  Serial.print(nivelPotassioMgDm3);
  Serial.print(",Fosforo(mg/dm3):");
  Serial.println(nivelFosforoMgDm3);

  // Exibição no LCD
  lcd.clear();
  lcd.setCursor(0, 0); // Linha 1
  lcd.printf("Temp:%.1fC Umid:%.1f%%", temperatura, umidade);
  lcd.setCursor(0, 1); // Linha 2
  lcd.printf("Umid.Solo:%d%%", umidadeSoloPercent);
  lcd.setCursor(0, 2); // Linha 3
  lcd.printf("P:%dmg K:%dmg", nivelFosforoMgDm3, nivelPotassioMgDm3);
  lcd.setCursor(0, 3); // Linha 4
  lcd.printf("Bomba:%s", bombaLigada ? "Ligada" : "Desligada");

  // Exibição no Monitor Serial
  Serial.println("===== Leitura Atualizada =====");
  Serial.printf("Temperatura: %.2f °C\n", temperatura);
  Serial.printf("Umidade Relativa: %.2f %%\n", umidade);
  Serial.printf("Umidade do Solo: %d %%\n", umidadeSoloPercent);
  Serial.printf("Potássio: %d mg/dm³ (Ideal: >%d mg/dm³)\n", nivelPotassioMgDm3, LIMITE_IDEAL_POTASSIO);
  Serial.printf("Fósforo: %d mg/dm³ (Ideal: >%d mg/dm³)\n", nivelFosforoMgDm3, LIMITE_IDEAL_FOSFORO);
  Serial.printf("Estado da Bomba: %s\n", bombaLigada ? "Ligada" : "Desligada");

  if (nivelPotassioMgDm3 < LIMITE_IDEAL_POTASSIO) {
    Serial.println("Nível de potássio abaixo do ideal! Verifique a suplementação.");
  }
  if (nivelFosforoMgDm3 < LIMITE_IDEAL_FOSFORO) {
    Serial.println("Nível de fósforo abaixo do ideal! Verifique a suplementação.");
  }

  if (bombaLigada) {
    Serial.println("A bomba foi LIGADA devido à baixa umidade do solo.");
  } else {
    Serial.println("A bomba está DESLIGADA. Todos os níveis estão estáveis.");
  }
  Serial.println("=============================\n");

  delay(5000); // Atualização a cada 5 segundos
}