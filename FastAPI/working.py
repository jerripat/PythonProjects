from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"message": "This is a simple API developed using FastAPI."}