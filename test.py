import numpy as np 

""" Assignment 01 """
# numbers_list = [i*10 for i in range(0,10)]
# numbers_array = np.array(numbers_list)

# print(f"dimension: {numbers_array.ndim}")
# print(f"Shape: {numbers_array.shape}")
# print(f"Size: {numbers_array.size}")
# print(f"type: {numbers_array.dtype}")
# ------------------------------------------------------------------------------

""" Assignment 02 """
# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers_array = np.array(numbers)
# print(numbers_array.dtype)

# ----------------------------------
""" Assignment 03 
numpy functions:
zeros
ones
arange
linspace
reshpe"""


# zeros
# numbers = np.zeros(10)
# numbers[0]= 1
# numbers[9] = 10
# print(numbers)

# ------------------------------------

# numbers = np.ones(3)
# addition = numbers * 100
# print(addition)

# ---------------------------------------
# arange 

# numbers = np.arange(20)
# addition = numbers * 10
# print(addition)

# -------------------------------------------
#lin space 
# numbers = np.linspace(1,10,6)
# print(numbers)

# ------------------------------------------

# random numbers generations 
"""for to generate the random numbers we have to initialize the random number generatio"""

# rng = np.random.default_rng()
# numbers = rng.random(10)
# print(numbers)

# -------------------------------------------
""" assignment 3"""
# rng = np.random.default_rng(12345)
# ages_array = rng.integers(0,100,100)
# print(ages_array)
#------------------------------------------------

# products = np.array(['fruits','vegetables','cerial','dairy','eggs','snacks','beaverages','coffee','tea','spices'])
# daily_prod = products.reshape(2,5)

# #print(daily_prod[:,2:])

# numbers = np.arange(1,21)
# digits = numbers.reshape(2,10)
# print(digits[-1,-3:])

# ----------------------------------------
# ages = np.array([5, 10, 15, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

# youth_ages = ages[1:4]
# adult_ages = ages[4:14]
# senior_ages = ages[14:]

# print(f"Youth_ages:{youth_ages},Adult_ages:{adult_ages},Senior_ages:{senior_ages}")
# ---------------------------------------------------------------------

# table_selection = int(input("enter table: "))
# limit = int(input("limit: "))

# table_limit = np.arange(1,limit+1)
# table_data = table_limit * table_selection
# print(table_data.reshape(10,1))

# --------------------------------------------
# rng = np.random.default_rng()
# numbers = rng.integers(1,10000,7)
# print(numbers)

#v------------------------------------------
""" To Find the age dofference between two arrays """
# town_a_ages = np.array([25, 45, 70, 34, 58])
# town_b_ages = np.array([30, 55, 65, 40, 60])

# age_differences = town_b_ages - town_a_ages

# print(age_differences)

# ----------------------------------------------------------
# numbers = np.linspace(0,10,3)
# print(numbers)
# ------------------------------------------------
# This is updated file 