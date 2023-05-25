from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def emeraldValue(self) -> int:
        if self.capacity <= self.volume:
            return self.nutrient_factor * self.capacity
        else:
            return self.nutrient_factor * self.volume

    def __gt__(self, other):
        return self.emeraldValue() > other.emeraldValue()
    
    def __lt__(self, other):
        return self.emeraldValue() < other.emeraldValue()
    
    def __ge__(self, other):
        return self.emeraldValue() >= other.emeraldValue()

    def __le__(self, other):
        return self.emeraldValue() <= other.emeraldValue()
    


class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.beehives = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Best and Worst case: O(N) where N is the number of beehives in hive_list
        Since we know the beehives we are adding and we have them in a list, we can just use the beehives array as the heap and 'heapify'
        the given list and since we iterate through the list to shift all the beehives 1 index to the right, the overall time complexity 
        is O(N)
        """
        self.beehives = MaxHeap(len(hive_list), hive_list)
    
    def add_beehive(self, hive: Beehive):
        """
        Best and Worst Case: O(logN)
        We use the MaxHeap method to add BeeHive objects and since MaxHeap add() method complexity is O(logN) in best and worst case,
        the overall complexity of this method is O(logN)

        """
        
        self.beehives.add(hive)
    
    def harvest_best_beehive(self) -> float:
        """
        Best Case and Worst Case: O(logN)
        self.beehives.get_max() and self.beehives.add() is O(logN) and the rest of the code is comparison, assignment and arithmetics operations
        which are O(1). The time complexity depends on the complexity of the MaxHeap methods, add and get_max and since both methods are O(logN)
        in best case and worse case and computation of comparison magic methods gt, lt, ge and le are O(1), overall complexity is O(logN)

        """
        
        emeralds = 0
        besthive = self.beehives.get_max()

        if besthive.volume <= besthive.capacity:
            emeralds = besthive.volume * besthive.nutrient_factor   
            return emeralds
        
        honey = min(besthive.capacity, besthive.volume)
        emeralds = honey * besthive.nutrient_factor
        besthive.volume -= besthive.capacity

        self.beehives.add(besthive)
        return emeralds
