from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.tree = BinarySearchTree()
    
    def add_point(self, item: T):
        self.tree[item] = item
    
    def remove_point(self, item: T):
        del self.tree[item]

    def ratio(self, x, y):
        
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
    
