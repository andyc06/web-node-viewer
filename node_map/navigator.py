from operator import add


class NodeNavigator():
    '''
    ^
    |
    Y+ 
      X+ -->
    heading   coordinate
                  change
      ◄    270    -1, 0
      ►     90     1, 0
      ▲      0     0, 1
      ▼    180     0, -1
    '''
    
    heading_movements = {
        0: [0, 1],
        45: [1, 1],
        90: [1, 0],
        135: [1, -1],
        180: [0, -1],
        225: [-1, -1],
        270: [-1, 0],
        315: [-1, 1],
    }

    def __init__(self, node_dict):
        self.nodes = node_dict
    

    def node_to_xy(self, node_id):
        try:
            # Find node based on id value
            n = next((d for d in self.nodes if d.get("id") == node_id), None)

            # Get coordinates from node
            c = n.get("coordinates")
            return c

        except:
            return None  # FIXME: Conditionally returning None might be an anti-pattern
    

    def xy_to_node(self, coordinates):
        try:
            # return the id of the node with the given coordinates (provided as a list)
            n = next((d for d in self.nodes if d.get("coordinates") == coordinates), None)
            return n.get("id")
        
        except:
            return None


    def node_info(self, node_id):
        '''Return the dictionary for the given node'''
        try:
            # return the id of the node with the given coordinates (provided as a list)
            n = next((d for d in self.nodes if d.get("id") == node_id), None)
            return n
        
        except:
            return None


    def get_node_image_name(self, node_id, heading):
        n = self.node_info(node_id)
        image_name = n["images"][heading]
        return image_name


    def move_forward(self, node_id, heading):
        # assumes that the node_id and heading are valid (handle errors here in the future)
        start_coordinates = self.node_to_xy(node_id)
        movement = self.heading_movements[heading]
        end_coordinates = list(map(add, start_coordinates, movement))

        end_node = self.xy_to_node(end_coordinates)
        if end_node == None: # had to add this as a quick fix because node 1, heading 180 returns None for some reason :( 
            return node_id
        else:
            return end_node
    
    
    def list_node_angles(self, node_id):
        node = self.node_info(node_id)
        angles = node["images"]
        sorted_angles = sorted(angles.keys())
        return sorted_angles


    def rotate(self, node_id, start_heading, direction):
        '''Return the new heading after rotating at the specified node in the given direction
        Note on directions:
        clockwise = 1
        counter-clockwise = -1
        '''
        # Note that this doesn't handle errors right now
        angle_list = self.list_node_angles(node_id)
        
        # Convert start heading to angle index
        start_angle_index = angle_list.index(start_heading)

        # Add the direction to the start angle index to get the pre-modulo "ending index" 
        target_index_after_rotate = start_angle_index + direction

        # Modulo with the index length to wraparound the index if out of bounds
        end_angle_index = target_index_after_rotate % len(angle_list)

        # Finally, return the angle value at that index
        return angle_list[end_angle_index]
