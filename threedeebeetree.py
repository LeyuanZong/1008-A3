from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I

    # 8 directions
    x0y0z0: BeeNode|None = None
    x0y0z1: BeeNode|None = None
    x0y1z0: BeeNode|None = None
    x0y1z1: BeeNode|None = None
    x1y0z0: BeeNode|None = None
    x1y0z1: BeeNode|None = None
    x1y1z0: BeeNode|None = None
    x1y1z1: BeeNode|None = None

    subtree_size: int = 1

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        
        # if point is the current key, return current node
        if self.key == point:
            return self
        
        # else calculate the direction of point is supposed to be in,
        # then return the node in that direction of the current node

        elif self.key[0] < point[0]:
            if self.key[1] < point[1]:
                if self.key[2] < point[2]:
                    return self.x1y1z1
                
                else:
                    return self.x1y1z0
                
            else:
                if self.key[2] < point[2]:
                    return self.x1y0z1
                
                else:
                    return self.x1y0z0
        
        else:
            if self.key[1] < point[1]:
                if self.key[2] < point[2]:
                    return self.x0y1z1
                
                else:
                    return self.x0y1z0
                
            else:
                if self.key[2] < point[2]:
                    return self.x0y0z1
                
                else:
                    return self.x0y0z0


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        
        return self.get_tree_node_by_key_aux(self.root, key)
    
    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:

        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        
        elif key == current.key:
            return current
        
        # access directions according to the x, y, z coords relative to the current node
        elif key[0] < current.key[0]:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    return self.get_tree_node_by_key_aux(current.x0y0z0, key)
                
                else:
                    return self.get_tree_node_by_key_aux(current.x0y0z1, key)
                
            else:
                if key[2] < current.key[2]:
                    return self.get_tree_node_by_key_aux(current.x0y1z0, key)
                
                else:
                    return self.get_tree_node_by_key_aux(current.x0y1z1, key)
                
        else:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    return self.get_tree_node_by_key_aux(current.x1y0z0, key)
                
                else:
                    return self.get_tree_node_by_key_aux(current.x1y0z1, key)
                
            else:
                if key[2] < current.key[2]:
                    return self.get_tree_node_by_key_aux(current.x1y1z0, key)
                
                else:
                    return self.get_tree_node_by_key_aux(current.x1y1z1, key)


    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item = item, subtree_size = 1)
            self.length += 1

        
        # access deeper node, the direction calculated by 
        # the x, y, z coords relative to the current node

        elif key[0] < current.key[0]:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    current.x0y0z0 = self.insert_aux(current.x0y0z0, key, item)
                    current.subtree_size += 1

                elif key[2] >= current.key[2]:
                    current.x0y0z1 = self.insert_aux(current.x0y0z1, key, item)
                    current.subtree_size += 1

            elif key[1] >= current.key[1]:
                if key[2] < current.key[2]:
                    current.x0y1z0 = self.insert_aux(current.x0y1z0, key, item)
                    current.subtree_size += 1

                elif key[2] >= current.key[2]:
                    current.x0y1z1 = self.insert_aux(current.x0y1z1, key, item)
                    current.subtree_size += 1

        elif key[0] >= current.key[0]:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    current.x1y0z0 = self.insert_aux(current.x1y0z0, key, item)
                    current.subtree_size += 1

                elif key[2] >= current.key[2]:
                    current.x1y0z1 = self.insert_aux(current.x1y0z1, key, item)
                    current.subtree_size += 1

            elif key[1] >= current.key[1]:
                if key[2] < current.key[2]:
                    current.x1y1z0 = self.insert_aux(current.x1y1z0, key, item)
                    current.subtree_size += 1

                elif key[2] >= current.key[2]:
                    current.x1y1z1 = self.insert_aux(current.x1y1z1, key, item)
                    current.subtree_size += 1
        
        else:  # key == current.key
            return ValueError('Inserting duplicate item')
        
        return current


    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        lst = [current.x0y0z0, current.x0y0z1, current.x0y1z0, current.x0y1z1, current.x1y0z0, current.x1y0z1, current.x1y1z0, current.x1y1z1]

        for d in lst:
            if d != None:
                return False
            
        return True


