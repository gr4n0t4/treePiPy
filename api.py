from fastapi import FastAPI
from pydantic import BaseModel
from tasks import spiral, random_led, top_down, sides



app = FastAPI()


class Item(BaseModel):
    name: str
    reverse: bool

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/tree")
async def tree(item: Item):
    if item.name == 'spiral':
        spiral.delay()
    elif item.name == 'random_led':
        random_led.delay()
    elif item.name == 'top_down':
        if not item.reverse:
            top_down.delay(True)
        else:
            top_down.delay(False)
    elif item.name == 'sides':
        if not item.reverse:       
            sides.delay(True)
        else:
            sides.delay(False)
    return item