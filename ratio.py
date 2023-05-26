from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:

        # complexity: O(1)

        self.tree = BinarySearchTree()
    
    def add_point(self, item: T):
        """
        complexity best: O(CompK) inserts the item at the root.
        complexity worst: O(Compk * D) inserting at the bottom of the tree
        where D is the depth of the tree
        CompK is the complexity of comparing the keys
        Refer to __setitem__() in bst.BinarySearchTree
        """


        self.tree[item] = item
    
    def remove_point(self, item: T):
        """
        complexity best: O(CompK) delete the item at the root.
        complexity worst: O(Compk * D) delete at the bottom of the tree
        where D is the depth of the tree
        CompK is the complexity of comparing the keys
        Refer to __delitem__() in bst.BinarySearchTree
        """
        del self.tree[item]

    def ratio(self, x, y):
        """
        complexity best: O(D)
        complexity worst: O(D + R)
        Refer to get_range() in bst.BinarySearchTree
        """
        
        # converting percentage into start and end of the values at range
        a = ceil(x/100* len(self.tree)) + 1
        b = len(self.tree) - ceil(y/100* len(self.tree))

        return self.tree.get_range(a, b)


if __name__ == "__main__":
    import random
    def test_removal():
        random.seed(2938742)
        p = Percentiles()
        points = [4, 9, 14, 15, 16, 82, 87, 91, 92, 99]
        random.shuffle(points)
        for point in points:
            p.add_point(point)
        p.remove_point(4)
        p.remove_point(92)

        res = p.ratio(13, 10)
        print(set(res), [15, 16, 82, 87, 91])

        p.remove_point(82)
        res = p.ratio(13, 10)
        print(set(res), [14, 15, 16, 87, 91])

    test_removal()
    

