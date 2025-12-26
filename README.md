# 👋 Olá, eu sou Gabriel

Bem-vindo ao meu portfólio! Aqui mantenho meus projetos, estudos e experimentos envolvendo **programação**, **visão computacional**, **desenvolvimento web**, **automação**, **mobile** e **dados**.

---

# 📁 Projetos

---

## 🔹 Projeto 1 — Dashboard de Logins (Streamlit)

📊 **Descrição**  
Dashboard interativo para análise de acessos, incluindo filtros por período, usuários, horários e métricas essenciais para monitoramento.

🛠 **Tecnologias Utilizadas**
- Python  
- Streamlit  
- Pandas  
- Plotly  

🎥 **Demonstração:**  
[👉 Assista ao vídeo](https://youtube.com/shorts/GUm2AFITHSo?feature=share)

📁 **Código-fonte:**  
[Clique para acessar](https://github.com/gabrielbarcelospederzini-commits/Meu-portifolio/commit/0f8f84db631f09ee617f96af4cfb60eb23402484)

---

## 🔹 Projeto 2 — Sistema de Monitoramento Inteligente com IA

Aplicação desenvolvida com **Python, Flask, YOLOv8 e PostgreSQL** para detecção em tempo real de pessoas, carros, cachorros e outros objetos.  
O sistema registra automaticamente eventos no banco de dados, oferece streaming de vídeo e permite controle total da câmera via interface web.

### 🚀 Funcionalidades
✔ Detecção em tempo real com YOLOv8  
✔ Streaming de vídeo via Flask  
✔ Registro automático de eventos no PostgreSQL  
✔ Logs contendo:
- Objeto detectado  
- Status da câmera  
- Timestamp  
✔ API com rotas para:
- Status da detecção  
- Histórico recente  
- Ativar/desativar câmera  
✔ Front-end simples com atualização automática  
✔ Arquitetura modular e escalável  

### 🧠 Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| Python | Linguagem principal |
| Flask | Backend e rotas HTTP |
| OpenCV | Captura e tratamento de frames |
| YOLOv8 | Detecção de objetos |
| PostgreSQL | Banco de dados |
| dotenv | Variáveis de ambiente |
| NumPy | Manipulação de matrizes/imagens |

📁 **Código-fonte:**  
[Clique para acessar](https://github.com/gabrielbarcelospederzini-commits/Meu-portifolio/commit/a7ede6d68cabd6123382dae89c4e47a7d3eca34c)

---

## 🔹 Projeto 3 — Chatbot Integrado com Google Sheets (ArcelorMittal)

Chatbot construído a partir de um fluxograma, integrado ao Google Sheets para registro e consulta de informações em tempo real.  
O objetivo é automatizar processos internos e aumentar a eficiência operacional.

### 🧩 Competências demonstradas
- Python — lógica de conversação  
- Integração com Google Sheets API  
- Consumo de APIs REST  
- Automação de processos  
- Modelagem de fluxos conversacionais  

### 🔍 Funcionalidades já disponíveis
- **Controle de Acesso** (Segurança Empresarial) — registro de solicitações  
- **Restaurante** (Infraestrutura) — consultas e registros  

🔗 **Acesse o chatbot:**  
https://share.chatling.ai/s/Y697PN5QKnAQ6Aa

🖼 **Fluxograma:**  
![Fluxograma](https://arcelormittal-my.sharepoint.com/:i:/g/personal/gabriel_pederzini_arcelormittal_com_br/IQDjlFvctny-Q5oZK_iUWWzvAeYPB3wU6bEUcJONCjsTJUE?e=Ra70SD)

---

# Notevision (MoneyFind)

## 📱 Visão Geral

Notevision é um aplicativo desenvolvido para auxiliar deficientes visuais a identificar cédulas de dinheiro usando modelos de aprendizado de máquina em tempo real. Construído com React Native e TensorFlow Lite, o aplicativo oferece uma solução acessível e eficiente para reconhecer notas monetárias através da câmera do dispositivo.

## ✨ Funcionalidades

- **Detecção precisa**: Usa a câmera do dispositivo para detectar dinheiro instantaneamente.
- **Capacidade Offline**: Executa modelos TensorFlow Lite localmente no dispositivo.
- **Feedback de Áudio**: Anuncia o valor detectado.

## 🛠️ Tecnologias Utilizadas

- **Frontend**: React Native, TypeScript
- **Motor de ML**: TensorFlow Lite (modelos `.tflite`), YoloV8
- **Plataforma**: Android (atualmente)

## 📂 Estrutura do Projeto

```
moneyfind/
├── backend/           # Modelos de ML (arquivos tflite)
├── frontend/          # Código fonte do aplicativo React Native
│   ├── android/       # Arquivos nativos do projeto Android
│   ├── App.tsx        # Ponto de entrada principal da aplicação
│   └── assets/        # Imagens e outros ativos estáticos
└── README.md          # Documentação do projeto
```

## 🚀 Começando

### Pré-requisitos

- Node.js & npm/yarn
- Java Development Kit (JDK)
- Android Studio & Android SDK
- React Native CLI

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/modasby/moneyfind.git
   cd moneyfind
   ```

2. **Instale as dependências**
   ```bash
   cd frontend
   npm install
   # ou
   yarn install
   ```

### Executando o App

1. **Inicie o Metro Bundler**
   ```bash
   cd frontend
   npm start
   ```

2. **Execute no Android**
   Abra um novo terminal e execute:
   ```bash
   cd frontend
   npm run android
   ```

## 🤖 Modelos de Machine Learning

O aplicativo usa modelos `.tflite` localizados no diretório `backend/`.
- `model.tflite`: Modelo de detecção primário.
- `best_float32.tflite`: Modelo de ponto flutuante otimizado.


------

# 📊 Analisador Inteligente de Arquivos (CSV / Excel)

Aplicação web interativa desenvolvida com **Streamlit** para análise rápida e visual de arquivos **CSV e Excel**, permitindo explorar grandes volumes de dados de forma simples, eficiente e totalmente online.

---

## 🚀 Funcionalidades

- 📂 Upload de arquivos CSV e Excel  
- 🔍 Filtro por palavra-chave em todas as colunas  
- 📈 Estatísticas descritivas automáticas  
- ⚠️ Identificação de valores nulos por coluna  
- 📊 Visualizações automáticas:
  - Distribuição de colunas numéricas
  - Contagem de valores categóricos  
- ⬇️ Download dos dados filtrados em Excel  
- ⚡ Suporte a arquivos grandes (7.000+ linhas)  
- 🌐 Aplicação 100% online (não depende do computador do usuário)

---

## 🧠 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de **automatizar análises exploratórias de dados**, reduzindo o trabalho manual com planilhas e acelerando a geração de insights.

É aplicável em diversos contextos, como:
- Análises empresariais
- Validação de bases de dados
- Exploração inicial de datasets
- Apoio a áreas como **RH, Financeiro, Vendas, Operações e TI**

---

## 🛠️ Tecnologias Utilizadas

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 🌍 Demonstração Online

O aplicativo está hospedado na nuvem e pode ser acessado diretamente pelo navegador.

> Basta fazer o upload de um arquivo para iniciar a análise.

---

## 📌 Diferenciais

- Interface simples e intuitiva  
- Foco em automação de processos  
- Performance otimizada com cache  
- Tratamento de erros  
- Projeto pronto para uso em ambiente corporativo  
- Deploy em nuvem (Streamlit Cloud)

---

## 📁 Estrutura do Projeto

```text
Analise-arquivos/
├── ANALISES.py
├── requirements.txt
└── README.md

Link do app: https://meu-portifolio-eqnqhargeuzetq3dsgvhv9.streamlit.app/
---




# 🌐 Site Portfólio Pessoal

## 📌 Visão Geral
Site portfólio desenvolvido para apresentar meus projetos, habilidades e informações profissionais de forma clara, moderna e organizada.  
O projeto serve como vitrine técnica para recrutadores e como base para evolução contínua da minha presença online como desenvolvedor.

---

## ✨ Funcionalidades
- Página inicial com apresentação profissional  
- Seção dedicada a projetos  
- Layout limpo, moderno e responsivo  
- Estrutura escalável para novas páginas e funcionalidades  

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **Jinja2**
- **Git & GitHub**

---

## 📂 Estrutura do Projeto
site-portfolio/
├── app.py # Arquivo principal da aplicação Flask
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
│
├── static/
│ ├── style.css # Estilos do site
│ └── img/ # Imagens e assets
│
└── templates/
└── index.html # Página principal do portfólio

yaml
Copiar código

---

## 🚀 Objetivo do Projeto
- Centralizar meus projetos em um único site  
- Demonstrar boas práticas em desenvolvimento web  
- Criar uma base sólida para futuras melhorias  
- Facilitar o acesso de recrutadores ao meu trabalho  

---

## 📌 Status do Projeto
EM ANDAMENTO  
🔧 Em constante evolução para melhorias visuais, novas seções e deploy online

---

## 🛣️ Roadmap (Próximas Evoluções)
- Deploy em ambiente online  
- Adição de novos projetos  
- Melhorias em UX/UI  
- Integração com LinkedIn e GitHub  

---

## 👨‍💻 Autor
**Gabriel Pederzini**  
Desenvolvedor de Software focado em criar soluções modernas, eficientes e escaláveis.







📫 Contato

📸 Instagram: @Gabrielpederzini__

🔗 LinkedIn: https://www.linkedin.com/in/gabriel-pederzini-844304296

📧 E-mail: gabrielbarcelospederzini@gmail.com
