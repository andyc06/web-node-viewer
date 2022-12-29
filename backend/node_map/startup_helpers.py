import yaml
import node_map.navigator as nav
from node_map.img_to_angle_dict import img_dir_to_dict


# map nav init
MAP_FILE = "./node_map/maps/beach.yaml"
IMAGE_DIR = "./static/img"


def load_map_file(f):
    """
    Load a node metadata YAML file and return it as a list of dictionaries
    One dictionary per node
    """
    with open(f, mode = "r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        node_dict = yaml.load(file, Loader = yaml.FullLoader)
    
    return node_dict


def update_images(node_dict_list, image_dict):
    # returns a list of dictionaries (1 per node)
    new_node_dict_list = []

    # for each dictionary in node dict list, update images key to new angle dictionary from folder scan process
    for d in node_dict_list:
        node_id = d.get("id")
        new_images = image_dict[node_id]
        d.update({"images":new_images})
        new_node_dict_list.append(d)
    
    return new_node_dict_list


def run_map_startup():
    # one time setup for the map logic
    # FastAPI main.py module runs this on startup

    # map setup
    n = load_map_file(MAP_FILE)  # n will be a list of dicts (1 per node)
    # scan the image directory and construct a dictionary of nodes/angles/filenames
    img_dict = img_dir_to_dict(IMAGE_DIR)
    # enrich the node dictionaries by adding the images dict to each
    updated_nodes = update_images(n, img_dict)
    # instantiate the world map using the enriched node data
    world_map = nav.NodeNavigator(updated_nodes)

    return world_map
