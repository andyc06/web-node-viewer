from pathlib import Path
import os
import re
from itertools import groupby


def img_dir_to_dict(image_dir):
    
    image_path = Path(image_dir)
    
    # list of posix paths for png files
    images = image_path.glob("*.png")
    
    # initialize the empty outer list
    all_image_attributes = []
    
    for filename in images:
        base_filename = os.path.basename(filename)  # extract the filename from the posix path
        m = re.match(r"node(?P<node_id>.*)__angle_(?P<angle>.*).png", base_filename)  # extract numbers from templated filename that Blender produces
        node_id = int(m.group("node_id"))  # comes out as a string, but needs to be an int
        angle = int(m.group("angle"))
    
        image_attribute = [node_id, angle, base_filename]
    
        # this gives a flat list of lists for the properties of each node image
        all_image_attributes.append(image_attribute)
    
    # sort list of lists by first element
    # python should already be doing this but make it explicit just in case
    all_image_attributes.sort(key=lambda x: x[0])
    
    '''
    target format:
    'images': {0: 'node4__angle_0.png', 90: 'node4__angle_90.png', 180: 'node4__angle_180png', 270: 'node4__angle_270.png'}
    '''

    # initialize a final empty dict to hold angle & filename dicts keyed by node_id
    final_dict = {}
    
    # group by node_id to nest the angle and base_filename dict as the value of each node_id key
    for key, group in groupby(all_image_attributes, lambda x: x[0]):
        inner_dict = {img_attribute[1]: img_attribute[2] for img_attribute in group} # make a dict for each group of angles
        final_dict[key] = inner_dict

    return final_dict
