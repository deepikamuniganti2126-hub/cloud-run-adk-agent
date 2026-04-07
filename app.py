from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello 👋 I am your Cloud Run app!"}

@app.get("/agent")
def agent():
    return {"response": "This is your ADK agent running 🚀"}