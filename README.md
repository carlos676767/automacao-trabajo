
# Projeto de Automação com Selenium, Captura de Tela e Bot Telegram

Este projeto automatiza o acesso a um site, realiza login, tira screenshots, corta uma imagem da tela, e envia essa imagem via Telegram usando um bot. Também conta com monitoramento de inatividade e agendamento para rodar periodicamente.

---

## Sumário

* [Descrição Geral](#descrição-geral)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Como Usar](#como-usar)
* [Descrição dos Arquivos e Classes](#descrição-dos-arquivos-e-classes)
* [Dependências](#dependências)
* [Variáveis de Ambiente](#variáveis-de-ambiente)
* [Agendamento e Monitoramento de Inatividade](#agendamento-e-monitoramento-de-inatividade)
* [Bot Telegram (Node.js)](#bot-telegram-nodejs)

---

## Descrição Geral

Este sistema realiza as seguintes funções:

* Abre um navegador Chrome usando Selenium, acessa uma URL protegida por login
* Digita email e senha para autenticação
* Tira uma screenshot da página, redimensiona o zoom para 50%
* Corta uma região específica da imagem (recorte da tela)
* Executa um script Node.js que envia a imagem para um chat do Telegram via bot
* Roda automaticamente a cada 5 minutos
* Monitora inatividade do computador e gera um clique para evitar bloqueio

---

## Estrutura do Projeto

```
.
├── index.py          # Script principal em Python (Selenium + automação)
├── bot.js            # Script Node.js para envio da imagem no Telegram
├── .env              # Arquivo de variáveis de ambiente (URL, credenciais, token do bot)
├── fs.png            # Imagem gerada do screenshot (cortada)
├── README.md         # Este arquivo
```

---

## Como Usar

1. Clone o repositório

2. Instale as dependências Python (recomendo usar um virtualenv):

   ```bash
   pip install selenium python-dotenv pillow pygetwindow schedule idle_time pyautogui
   ```

3. Instale as dependências Node.js para o bot Telegram:

   ```bash
   npm install telegraf dotenv
   ```

4. Configure o arquivo `.env` com as variáveis necessárias (veja seção abaixo)

5. Execute o script Python principal:

   ```bash
   python index.py
   ```

---

## Descrição dos Arquivos e Classes

### `index.py`

* **Classes e Funções:**

  * `Hours`: fornece método para retornar data e hora atual formatada.

  * `CutImage`: método estático para cortar a imagem `fs.png` numa região definida.

  * `Browser`: controla o navegador Chrome com Selenium.

    * `open_browser()`: abre o navegador, acessa URL, faz login, tira screenshot, chama corte e o bot.
    * `escribeText(text)`: digita um texto seguido de ENTER.
    * `okKespass()`: envia ENTER (usado para confirmar login).
    * `screenShotAndZoom()`: diminui zoom da página para 50%, tira screenshot, fecha navegador e chama corte + bot.

  * `IdleScreen`: monitora tempo ocioso do computador e envia clique para evitar bloqueio.

  * `CroonJoob`: agenda a execução de `Browser.open_browser()` a cada 5 minutos usando `schedule`.

---

## Dependências

* Python 3.x
* Selenium
* python-dotenv
* Pillow (PIL)
* pygetwindow
* schedule
* idle\_time
* pyautogui
* Node.js (para executar o bot.js)
* Telegraf (Node.js Telegram bot framework)

---

## Variáveis de Ambiente (`.env`)

Configure as seguintes variáveis no arquivo `.env` na raiz do projeto:

```
URLSECRET=https://exemplo.com/login
EMAILSECRET=seu-email@exemplo.com
PASSWORLD=sua-senha-secreta
BOT_SECRET=token_do_bot_telegram
CHAT_ID=id_do_chat_telegram
```

* `URLSECRET`: URL da página de login.
* `EMAILSECRET`: email usado para login.
* `PASSWORLD`: senha usada para login.
* `BOT_SECRET`: token do bot Telegram.
* `CHAT_ID`: ID do chat Telegram para enviar a mensagem.

---

## Agendamento e Monitoramento de Inatividade

* O script roda `Browser.open_browser()` a cada 5 minutos para capturar e enviar atualizações.
* O `IdleScreen` monitora se o computador está ocioso (3 minutos) e simula um clique para evitar bloqueio de tela.

---

## Bot Telegram (Node.js)

O arquivo `bot.js` usa a biblioteca [Telegraf](https://telegraf.js.org/) para enviar a imagem cortada para o Telegram.

* Formata a data/hora atual para legenda da foto.
* Envia a imagem `fs.png` para o chat definido no `.env`.
* Se houver erro, reinicia o script Python para tentar novamente.

