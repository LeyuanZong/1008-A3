from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    ordered_list = []
    x_calculator = Percentiles()
    y_calculator = Percentiles()
    z_calculator = Percentiles()

    for point in my_coordinate_list:
        x_calculator.add_point(point[0])
        y_calculator.add_point(point[1])
        z_calculator.add_point(point[2])

    rootX = x_calculator.ratio(0,0)
    rootY = y_calculator.ratio(0,0)
    rootZ = z_calculator.ratio(0,0)
    
    
    ordered_list = my_coordinate_list

    return ordered_list
