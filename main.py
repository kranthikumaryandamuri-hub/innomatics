from fastapi import FastAPI

app = FastAPI(title="Kranthi's API")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name():
    return {"name": "Kranthi Kumar"}

@app.get("/batch")
def read_batch():
    return {"batch": "555-B"}