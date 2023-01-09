// ####  Código Principal  ####################################################################
#include "Arduino.h"
#include "WiFi.h"
#include <HTTPClient.h>
#include "ESPAsyncWebServer.h"
#include <SPI.h>     //INCLUSÃO DE BIBLIOTECA
#include "MFRC522.h" //INCLUSÃO DE BIBLIOTECA

#define LED_PIN 2

#define SS_PIN 5  // PINO SDA
#define RST_PIN 0 // PINO DE RESET

#define SIZE_BUFFER 18
#define MAX_SIZE_BLOCK 16

// esse objeto 'chave' é utilizado para autenticação
MFRC522::MIFARE_Key key;
// código de status de retorno da autenticação
MFRC522::StatusCode status;

MFRC522 mfrc522(SS_PIN, RST_PIN); // PASSAGEM DE PARÂMETROS REFERENTE AOS PINOS

const char *ssid = "Erick";
const char *password = "@abcdefgh";

const char *serverHelloWorld = "http://192.168.229.33/";
const char *serverGetUserByCode = "http://192.168.229.33/confirmCode/";

unsigned long previousMillis = 0;
const long interval = 5000;

// Definindo um servidor na porta 80
AsyncWebServer server(80);

String serverResponse;

String httpGETRequest(const char *serverName);

char *awaitAndGetTag();

void openLock();

String code;

char arr[10];

void setup()
{
  pinMode(LED_PIN, OUTPUT);

  digitalWrite(LED_PIN, 1);

  Serial.begin(115200);
  delay(1000);

  SPI.begin();        // INICIALIZA O BARRAMENTO SPI
  mfrc522.PCD_Init(); // INICIALIZA MFRC522

  WiFi.mode(WIFI_STA); // Optional
  WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(100);
  }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());

  server.on("/code", HTTP_GET, [](AsyncWebServerRequest *request)
            { request->send_P(200, "text/plain", awaitAndGetTag()); });
  server.on("/open", HTTP_GET, [](AsyncWebServerRequest *request)
            { openLock();
                  request->send_P(200, "text/plain", "Ok"); });

  // cors
  DefaultHeaders::Instance().addHeader("Access-Control-Allow-Origin", "*");
  server.begin();
}

void loop()
{
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval)
  {
    // Check WiFi connection status
    if (WiFi.status() == WL_CONNECTED)
    {
      // serverResponse = httpGETRequest(serverHelloWorld);
      // Serial.println("Server Message: " + serverResponse);

      // save the last HTTP GET Request
      previousMillis = currentMillis;
    }
    else
    {
      Serial.println("WiFi Disconnected");
    }
  }

  // Aguarda a aproximacao do cartao
  if (!mfrc522.PICC_IsNewCardPresent())
  {
    return;
  }
  // Seleciona um dos cartoes
  if (!mfrc522.PICC_ReadCardSerial())
  {
    return;
  }

  byte uidSize = sizeof(mfrc522.uid.uidByte);

  // initialise character array
  memset(arr, 0, sizeof(arr));

  for (int cnt = 0; cnt < uidSize; cnt++)
  {
    // convert byte to its ascii representation
    sprintf(&arr[cnt * 2], "%02X", mfrc522.uid.uidByte[cnt]);
  }

  // instrui o PICC quando no estado ACTIVE a ir para um estado de "parada"
  mfrc522.PICC_HaltA();
  // "stop" a encriptação do PCD, deve ser chamado após a comunicação com autenticação, caso contrário novas comunicações não poderão ser iniciadas
  mfrc522.PCD_StopCrypto1();

  char *get_user_by_passcode_url = (char *)malloc(strlen(serverGetUserByCode) + strlen(arr) + 1);

  int tempLength = strlen(serverGetUserByCode) + strlen(arr);

  memcpy(get_user_by_passcode_url, serverGetUserByCode, strlen(serverGetUserByCode));
  memcpy(get_user_by_passcode_url + strlen(serverGetUserByCode), arr, strlen(arr) + 1);

  Serial.println(get_user_by_passcode_url);

  String payload = httpGETRequest(get_user_by_passcode_url);

  Serial.println(payload);

  if (payload == "1")
  {
    openLock();
  }
  else
  {
    Serial.println("Usuário não cadastrado.");
  }
}

void openLock()
{
  digitalWrite(LED_PIN, 0);
  Serial.println("Aberto");
  delay(3000);
  digitalWrite(LED_PIN, 1);
  Serial.println("Fechado");
}

String httpGETRequest(const char *serverName)
{
  WiFiClient client;
  HTTPClient http;

  // Your Domain name with URL path or IP address with path
  http.begin(client, serverName);

  // Send HTTP POST request
  int httpResponseCode = http.GET();

  String payload = "--";

  if (httpResponseCode > 0)
  {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else
  {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}

char *awaitAndGetTag()
{

  Serial.println("Waiting for input...");

  while (true)
  {
    // Aguarda a aproximacao do cartao
    if (!mfrc522.PICC_IsNewCardPresent())
    {
      continue;
    }
    // Seleciona um dos cartoes
    if (!mfrc522.PICC_ReadCardSerial())
    {
      continue;
    }

    byte uidSize = sizeof(mfrc522.uid.uidByte);

    // initialise character array
    memset(arr, 0, sizeof(arr));

    for (int cnt = 0; cnt < uidSize; cnt++)
    {
      // convert byte to its ascii representation
      sprintf(&arr[cnt * 2], "%02X", mfrc522.uid.uidByte[cnt]);
    }

    Serial.println(arr);

    // instrui o PICC quando no estado ACTIVE a ir para um estado de "parada"
    mfrc522.PICC_HaltA();
    // "stop" a encriptação do PCD, deve ser chamado após a comunicação com autenticação, caso contrário novas comunicações não poderão ser iniciadas
    mfrc522.PCD_StopCrypto1();
    break;
  }

  return arr;
}

// ####  RFID BASE CODE  ##########################################################

// #include "Arduino.h"
// #include <SPI.h>     //INCLUSÃO DE BIBLIOTECA
// #include "MFRC522.h" //INCLUSÃO DE BIBLIOTECA

// #define SS_PIN 5  // PINO SDA
// #define RST_PIN 0 // PINO DE RESET

// #define SIZE_BUFFER 18
// #define MAX_SIZE_BLOCK 16

// // esse objeto 'chave' é utilizado para autenticação
// MFRC522::MIFARE_Key key;
// // código de status de retorno da autenticação
// MFRC522::StatusCode status;

// MFRC522 mfrc522(SS_PIN, RST_PIN); // PASSAGEM DE PARÂMETROS REFERENTE AOS PINOS

// void setup()
// {
//   Serial.begin(9600); // INICIALIZA A SERIAL
//   SPI.begin();        // INICIALIZA O BARRAMENTO SPI
//   mfrc522.PCD_Init(); // INICIALIZA MFRC522
// }

// void loop()
// {
//   // Aguarda a aproximacao do cartao
//   if (!mfrc522.PICC_IsNewCardPresent())
//   {
//     return;
//   }
//   // Seleciona um dos cartoes
//   if (!mfrc522.PICC_ReadCardSerial())
//   {
//     return;
//   }

//   for (byte i = 0; i < mfrc522.uid.size; i++)
//   {
//     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
//     Serial.print(mfrc522.uid.uidByte[i], HEX);
//   }

//   // instrui o PICC quando no estado ACTIVE a ir para um estado de "parada"
//   mfrc522.PICC_HaltA();
//   // "stop" a encriptação do PCD, deve ser chamado após a comunicação com autenticação, caso contrário novas comunicações não poderão ser iniciadas
//   mfrc522.PCD_StopCrypto1();
// }

// ##  LED With input time interval  ###########################################

// To Start a typeable monitor in platformio run: pio device monitor --eol=CRLF --echo --filter send_on_enter

// #include "Arduino.h"

// static const int app_cpu = 1;

// static const int led_pin = 2;

// // Settings
// static const uint8_t buf_len = 20;

// // Globals
// static int led_delay = 500; // ms

// void taskSerialRead(void *parameter)
// {

//   char c;
//   char buf[buf_len];
//   uint8_t idx = 0;

//   // Clear whole buffer
//   memset(buf, 0, buf_len);

//   while (1)
//   {

//     // Read characters from serial
//     if (Serial.available() > 0)
//     {
//       c = Serial.read();

//       // Update delay variable and reset buffer if we get a newline character
//       if (c == '\n')
//       {
//         led_delay = atoi(buf);
//         Serial.print("Updated LED delay to: ");
//         Serial.println(led_delay);
//         memset(buf, 0, buf_len);
//         idx = 0;
//       }
//       else
//       {

//         // Only append if index is not over message limit
//         if (idx < buf_len - 1)
//         {
//           buf[idx] = c;
//           idx++;
//         }
//       }
//     }
//   }
// }
// void toggleLED(void *parameter)
// {
//   while (1)
//   {
//     digitalWrite(led_pin, HIGH);
//     vTaskDelay(led_delay / portTICK_PERIOD_MS);
//     digitalWrite(led_pin, LOW);
//     vTaskDelay(led_delay / portTICK_PERIOD_MS);
//   }
// }

// void setup()
// {
//   Serial.begin(9600);

//   pinMode(led_pin, OUTPUT);

//   // Task to run forever
//   //  xTaskCreate in vanilla FreeRTOS. However, in this library,
//   //  xTaskCreate run the task in any available core while
//   //  xTaskCreatePinnedToCore runs the task in an specific core
//   xTaskCreatePinnedToCore(
//       toggleLED,    // Function to be called
//       "Toogle LED", // Name of The Task
//       1024,         // Stack Size (bytes in ESP32, words in FreeRTOS)
//       NULL,         // Parameter to pass to function
//       1,            // Task Priority (0 to configMAX_PRIORITIES - 1)
//       NULL,         // task handle (a pointer to get status and terminate task)
//       app_cpu       // How many cores to use
//   );

//   xTaskCreatePinnedToCore(
//       taskSerialRead, // Function to be called
//       "Toogle LED",   // Name of The Task
//       1024,           // Stack Size (bytes in ESP32, words in FreeRTOS)
//       NULL,           // Parameter to pass to function
//       1,              // Task Priority (0 to configMAX_PRIORITIES - 1)
//       NULL,           // task handle (a pointer to get status and terminate task)
//       app_cpu         // How many cores to use
//   );

//   // In vanilla FreeRTOS, it's necessary to call vTaskStartScheduler() in main after setting up tasks.
//   // However, esp32 already uses a modified version of FreeRTOS to run the setup and loop function and
//   // initializes the FreeRTOS functions

//   // Delete "setup and loop" task
//   vTaskDelete(NULL);
// }

// void loop()
// {
// }

// #######  Demo Preemption  ####################################################

// #include "Arduino.h"

// static const int app_cpu = 1;

// static const int led_pin = 2;

// const char msg[] = "Erick Mandando Mensagem Usando RTOS";

// static TaskHandle_t task_1 = NULL;
// static TaskHandle_t task_2 = NULL;

// // Task: print to Serial Terminal with lower priority
// void task1(void *parameter)
// {
//   int msg_len = strlen(msg);

//   while (1)
//   {
//     Serial.println();
//     // Not sending the entire string at once to avoid it being stored
//     // in the serial buffer
//     for (int i = 0; i < msg_len; i++)
//     {
//       Serial.print(msg[i]);
//     }
//     Serial.println();
//     vTaskDelay(1000 / portTICK_PERIOD_MS);
//   }
// }

// // Task: print to Serial Terminal with higher priority
// void task2(void *parameter)
// {
//   while (1)
//   {
//     Serial.print('*');
//     vTaskDelay(100 / portTICK_PERIOD_MS);
//   }
// }

// void setup()
// {
//   // Slow rate to let the preemption occur
//   Serial.begin(300);

//   // Wait a moment to start to see the preemption
//   vTaskDelay(1000 / portTICK_PERIOD_MS);
//   Serial.println();
//   Serial.println("---- FreeTOS Preemption Demo ----");

//   Serial.print("Setup and loop running on core");
//   Serial.print(xPortGetCoreID());
//   Serial.print(" with priority ");
//   Serial.print(uxTaskPriorityGet(NULL));

//   // Task to run forever
//   //  xTaskCreate in vanilla FreeRTOS. However, in this library,
//   //  xTaskCreate run the task in any available core while
//   //  xTaskCreatePinnedToCore runs the task in an specific core
//   xTaskCreatePinnedToCore(
//       task1,         // Function to be called
//       "Print Frase", // Name of The Task
//       1024,          // Stack Size (bytes in ESP32, words in FreeRTOS)
//       NULL,          // Parameter to pass to function
//       1,             // Task Priority (0 to configMAX_PRIORITIES - 1)
//       &task_1,       // task handle (a pointer to get status and terminate task)
//       app_cpu        // How many cores to use
//   );

//   xTaskCreatePinnedToCore(
//       task2,        // Function to be called
//       "Print Star", // Name of The Task
//       1024,         // Stack Size (bytes in ESP32, words in FreeRTOS)
//       NULL,         // Parameter to pass to function
//       2,            // Task Priority (0 to configMAX_PRIORITIES - 1)
//       &task_2,      // task handle (a pointer to get status and terminate task)
//       app_cpu       // How many cores to use
//   );

//   // In vanilla FreeRTOS, it's necessary to call vTaskStartScheduler() in main after setting up tasks.
//   // However, esp32 already uses a modified version of FreeRTOS to run the setup and loop function and
//   // initializes the FreeRTOS functions
// }

// void loop()
// {
//   for (int i = 0; i < 3; i++)
//   {
//     vTaskSuspend(task_2);
//     vTaskDelay(2000 / portTICK_PERIOD_MS);
//     vTaskResume(task_2);
//     vTaskDelay(2000 / portTICK_PERIOD_MS);
//   }

//   if (task_1 != NULL)
//   {
//     Serial.println("Deleting task 1");
//     vTaskDelete(task_1);
//     task_1 = NULL;
//   }
// }

// ####  Blink in RTOS  #################################################################################################

// #include "Arduino.h"

// static const int app_cpu = 1;

// static const int led_pin = 2;

// void toggleLED(void *parameter)
// {
//   while (1)
//   {
//     digitalWrite(led_pin, HIGH);
//     vTaskDelay(500 / portTICK_PERIOD_MS); // vTaskDelay expects the number of ticks instead of time in milliseconds (1 tick = 1ms)
//     digitalWrite(led_pin, LOW);
//     vTaskDelay(500 / portTICK_PERIOD_MS);
//   }
// }

// void setup()
// {
//   pinMode(led_pin, OUTPUT);

//   // Task to run forever
//   //  xTaskCreate in vanilla FreeRTOS. However, in this library,
//   //  xTaskCreate run the task in any available core while
//   //  xTaskCreatePinnedToCore runs the task in an specific core
//   xTaskCreatePinnedToCore(
//       toggleLED,    // Function to be called
//       "Toogle LED", // Name of The Task
//       1024,         // Stack Size (bytes in ESP32, words in FreeRTOS)
//       NULL,         // Parameter to pass to function
//       1,            // Task Priority (0 to configMAX_PRIORITIES - 1)
//       NULL,         // task handle (a pointer to get status and terminate task)
//       app_cpu       // How many cores to use
//   );

//   // In vanilla FreeRTOS, it's necessary to call vTaskStartScheduler() in main after setting up tasks.
//   // However, esp32 already uses a modified version of FreeRTOS to run the setup and loop function and
//   // initializes the FreeRTOS functions
// }

// void loop()
// {
// }

// ##################################################################################################################
