import csv

from src.constants import ID_STR
from src.utils.getLocations import get_locations
from src.utils.getPackages import get_packages

# ASSUMPTIONS
# TRUCKS CAN CARRY UP TO 16 PACKAGES
# AVERAGE SPEED OF TRUCKS IS 18MPH OR .3 MILES PER MINUTE
# IT TAKES JUST OVER 3 MINUTES TO TRAVEL ONE MILE
# DRIVERS LEAVE AT 8AM

# GET THE PACKAGES AND INFORMATION
packages, package_order = get_packages()
locations = get_locations()

print(locations)

# tree = SoSBinaryTree()
#
# tree.insert('Isaac', 84107)
# tree.insert('Hinckley', 84104)
# print(tree.get_root())
