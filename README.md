
# 🚀 API de Mensagens Personalizadas com IA

Este projeto consiste em uma **API REST desenvolvida com FastAPI** que integra **Inteligência Artificial (IA)** para gerar **mensagens personalizadas para usuários (super-heróis)**.
O projeto foi desenvolvido inicialmente no **Google Colab** durante um bootcamp de Ciência de Dados e posteriormente organizado para publicação em um repositório GitHub como parte do portfólio.

---

## 🧠 Sobre o Projeto

A aplicação simula um sistema onde cada usuário representa um **super-herói**, e a IA é responsável por gerar **mensagens personalizadas** com base nas informações desse personagem.



O objetivo principal do projeto é demonstrar:

* Criação de uma API REST com FastAPI
* Integração com APIs externas de IA
* Geração de conteúdo dinâmico com Inteligência Artificial
* Organização de código para projetos reais e de portfólio

---

## 🛠️ Tecnologias Utilizadas

* 🐍 **Python**
* 🚀 **FastAPI** — Framework para criação de APIs
* 🌐 **Uvicorn** — Servidor ASGI
* 🤗 **Hugging Face API** — Geração de texto com IA
* 📦 **Requests** — Consumo de APIs externas
* 📓 **Google Colab** — Ambiente inicial de desenvolvimento
* 🧪 **Swagger UI** — Documentação automática da API

---

##  Como executar
Abra o notebook `Motivando` no Google Colab ou Jupyter Notebook e execute as células em ordem.

---

## 📁 Estrutura do Projeto

```
/
├── main.py              # Arquivo principal da API
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
└── .gitignore           # Arquivos ignorados pelo Git
```

---

## 🚀 Funcionalidades

* ✅ Criar usuários (super-heróis)
* 📄 Listar todos os usuários
* 🔍 Buscar usuário por ID
* ✏️ Editar dados de um usuário
* 🗑️ Remover usuário
* 🤖 Gerar mensagem personalizada com IA para cada usuário

---

## 🔗 Endpoints da API

| Método | Endpoint              | Descrição                          |
| ------ | --------------------- | ---------------------------------- |
| GET    | `/`                   | Rota inicial de teste              |
| GET    | `/users`              | Lista todos os usuários            |
| GET    | `/users/{id}`         | Busca usuário por ID               |
| POST   | `/users`              | Cria um novo usuário               |
| PUT    | `/users/{id}`         | Atualiza um usuário                |
| DELETE | `/users/{id}`         | Remove um usuário                  |
| GET    | `/users/{id}/message` | Gera mensagem personalizada com IA |

---

## ▶️ Como Executar o Projeto Localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd NOME_DO_REPOSITORIO
```

### 3️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv
```

Ativação:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

### 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Execute a API

```bash
uvicorn main:app --reload
```

---

## 🌐 Acessando a API

* API:

```
http://127.0.0.1:8000
```

* Documentação Swagger (interativa):

```
http://127.0.0.1:8000/docs
```

---

## 🤖 Integração com Inteligência Artificial

A API utiliza um **modelo de linguagem da Hugging Face** para gerar mensagens personalizadas.
O fluxo funciona assim:

1. O usuário é buscado pelo ID
2. As informações do usuário são transformadas em um prompt
3. O prompt é enviado para a API de IA
4. A resposta gerada é retornada ao cliente

---

## 🧪 Exemplo de Resposta da IA

Requisição:

```
GET /users/1/message
```

Resposta:

```json
{
  "user": "Homem de Ferro",
  "message": [
    {
      "generated_text": "Sua inteligência e liderança fazem de você um verdadeiro símbolo de inovação."
    }
  ]
}
```

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em **aprendizado prático**, abordando:

* APIs REST
* Integração com Inteligência Artificial
* Estruturação de projetos em Python
* Preparação de projetos para portfólio profissional

---

## 📚 Possíveis Melhorias Futuras

* Persistência de dados com banco de dados
* Autenticação de usuários
* Deploy em cloud (Render, Railway, Vercel)
* Testes automatizados
* Interface frontend consumindo a API

---

## 📜 Licença

Este projeto está sob a licença **MIT**.
Sinta-se livre para utilizar, modificar e compartilhar.

---

## 👨‍💻 Autor

Projeto desenvolvido por **Lúcio Queiroz**
Estudante de Ciência da Computação e entusiasta de Ciência de Dados e Inteligência Artificial 🚀




