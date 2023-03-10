<h1 align="center">Rasa_RocketChat</h1>
<h3 align="center">
Passo a passo de como realizar uma integração do Rocket.Chat com Rasa.
</h3>
<p align="center">
<img src = https://img.shields.io/badge/RASA-Chatbot-blueviolet>
<img src = https://img.shields.io/badge/Rocket.Chat-Canal-red>
<img src = https://img.shields.io/badge/Docker%20Compose-Deploy-blue>
<img src = https://img.shields.io/badge/Banco-Mongo-brightgreen>
<img src = https://img.shields.io/badge/Python-Linguagem-orange>
</p>
---

<p align="center">
<img src = https://img.shields.io/badge/Rasa-blueviolet?style=for-the-badge>
</p>

<img align="right" height="230" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">

## 1. Setup - [Rasa](https://rasa.com/docs/rasa/) 
### 1.1 Configuração do Bot
* Configure o `credentials.yml` de acordo com o bot criado no passo 2.3
  ```sh
  rocketchat:
    user: "rasa_bot"
    password: "rasa_bot"
    server_url: "http://rocketchat:3000"
  ```

### 1.2 Configuração do Actions
* Configure o `endpoints.yml` de acordo com seu ambiente
  ```sh
  # Configuração para ambiente docker
  action_endpoint:
    url: "http://actions:5055/webhook"
  ```

---
<p align="center">
<img src = https://img.shields.io/badge/Rocket.Chat-F5455C?style=for-the-badge&logo=rocket.chat&logoColor=white>
</p>

## 2. Setup - [Rocket.Chat](https://developer.rocket.chat/) 
### 2.1 Acessando a aplicação e iniciando os containers
```sh
docker-compose up -d
```

Acesse http://localhost:3000/

### 2.2 Configuração do Workspace 
```
Nome de usuário: admin
senha: admin
Servidor: Standalone
```

### 2.3 Configuração do Bot 
Siga **Administration** > **Users** > **+ New**.
```
Name: Rasa Chatbot 
Username: rasa_bot
Email: rasa_bot@email.com
Password: rasa_bot
Roles: bot
```

### 2.4 Configuração do WebHook
Siga **Administration** > **Integrations** > **+ New** > **Outgoing**.
```
Event Trigger: Message Sent
Enabled: true
Name: Rasa WebHook 
Channel: #general
URLs: http://rasa:5005/webhooks/rocketchat/webhook
Post as: rasa_bot
```

Siga **Advanced Settings**.
```
Retry Failed Url Calls: false
```
---
