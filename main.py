from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur SmartGuardian Cloud 🌩️"}

@app.post("/api/alerte")
def alerte(type: str, lieu: str):
    return {"message": f"Alerte reçue : {type} à {lieu}"}
