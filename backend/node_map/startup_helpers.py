import yaml
import node_map.navigator as nav

# map nav init
MAP_FILE = "./node_map/maps/beach-combined.yaml"


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


def run_map_startup():
    # one time setup for the map logic
    # FastAPI main.py module runs this on startup

    # map setup
    node_map = load_map_file(MAP_FILE)  # will be a list of dicts (1 per node)

    # instantiate the world map using the enriched node data
    world_map = nav.NodeNavigator(node_map)

    return world_map
