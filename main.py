from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message:" "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q:str = None):
  print(f"fastapi gave me item_id: {item_id}")
  print(f"fastapi gave me a: {q}")
  return {"item_id": item_id, "query" : q}