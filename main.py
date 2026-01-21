from fastapi import FastAPI
from app.routes.issues import router as issues_router
app = FastAPI()
app.include_router(issues_router)

items = [1, 2, 3]

@app.get("/")
def read_root():
  return {"message:" "Hello World"}


@app.get("/items")
def get_items():
  return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
  for item in items:
    if(item == item_id):
      return item
  return {"error found"}
  

@app.post("/items")
def post_item(item : int):
  items.append(item)
  return items