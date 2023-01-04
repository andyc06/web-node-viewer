# main.py
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# node navigation & helpers
#import node_map.navigator as nav
from node_map.startup_helpers import run_map_startup
#from node_map.img_to_angle_dict import img_dir_to_dict

# map startup
world_map = run_map_startup()

origins = [
    "*",
]

class Travel(BaseModel):
    direction: str
    current_node_id: int
    current_heading: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GET isn't really used for this app
@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/travel/")
async def do_travel(travel: Travel):
    direction = travel.direction
    current_node_id = travel.current_node_id
    current_heading = travel.current_heading

    # default to new = current unless changed in case logic
    new_node_id = current_node_id
    new_heading = current_heading

    if direction == "forward":
        new_node_id = world_map.move_forward(current_node_id, current_heading)
        # heading changes aren't currently implemented in move_forward
    elif direction == "counterclockwise":
        new_heading = world_map.rotate(current_node_id, current_heading, -1)
        # node doesn't change when rotating
    elif direction == "clockwise":
        new_heading = world_map.rotate(current_node_id, current_heading, 1)
        # node doesn't change when rotating
    elif direction == "here":
        pass

    node_image = world_map.get_node_image_name(new_node_id, new_heading)

    response = {}
    response.update({
        "node_id":new_node_id,
        "heading":new_heading,
        "node_image":node_image,
        })
    
    return response
