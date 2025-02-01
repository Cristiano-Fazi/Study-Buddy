from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/dummy")
def dummy_endpoint():
    return {"message": "This is a dummy endpoint"}