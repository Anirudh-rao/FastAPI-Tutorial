from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str="Bob"):
	return {"message": f"Hello {name}"}
    