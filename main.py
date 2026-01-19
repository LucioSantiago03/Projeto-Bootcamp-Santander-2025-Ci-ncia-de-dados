from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

users = [
    {
        'id': 1,
        'name': 'Iron Man',
        'news': ['Gênio bilionário que utiliza armaduras tecnológicas para proteger o mundo.']
    },
    {
        'id': 2,
        'name': 'Captain America',
        'news': ['Super soldado símbolo de liderança, coragem e justiça.']
    },
    {
        'id': 3,
        'name': 'Thor',
        'news': ['Deus do Trovão de Asgard, empunha o martelo Mjölnir e protege os nove reinos.']
    },
    {
        'id': 4,
        'name': 'Black Widow',
        'news': ['Ex-espiã altamente treinada, especialista em combate e inteligência.']
    },
    {
        'id': 5,
        'name': 'Spider-Man',
        'news': ['Herói jovem com habilidades aracnídeas que equilibra vida pessoal e heroísmo.']
    }
]

@app.get("/users")
def get_users():
    return users

@app.get("/")
def home():
    return {"message": "API funcionando "}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user

@app.post("/users/{user_id}/news")
def add_news(user_id: int, news: str):
    for user in users:
        if user["id"] == user_id:
            user["news"].append(news)
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"message": "Usuário removido com sucesso"}
    
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.get("name", user["name"])
            user["news"] = updated_user.get("news", user["news"])
            return user

    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.patch("/users/{user_id}")
def patch_user(user_id: int, data: dict):
    for user in users:
        if user["id"] == user_id:
            for key, value in data.items():
                user[key] = value
            return user

    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.post("/chat")
def chat(mensagem: str):
    resposta = chat_ia(mensagem)
    return resposta