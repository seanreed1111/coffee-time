import datetime
import random
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict

DrinkSize = Enum("DrinkSize", "SHORT TALL GRANDE")
MerchSize = Enum("MerchSize", "SMALL MEDIUM LARGE")
Season = Enum("Season", "SPRING SUMMER FALL WINTER")
PlainCoffeeProducts = Enum(
    "PlainCoffeeProducts",
    [
        "espresso_hot",
        "cappuccino_hot",
        "latte_hot",
        "coffee_hot",
        "cappuccino_iced",
        "latte_iced",
        "coffee_iced",
    ],
)
SpecialtyCoffeeProducts = Enum(
    "SpecialtyCoffeeProducts",
    [
        "carmel_cappuccino_hot",
        "mocha_cappuccino_hot",
        "white_chocolate_cappuccino_hot",
        "carmel_cappuccino_iced",
        "mocha_cappuccino_iced",
        "white_chocolate_cappuccino_iced",
    ],
)


# print(list(SpecialtyCoffeeProducts)) 

'''
for every drink
for every size
for every season
there is a price
price[drink][size][season]
'''

# use this as a separate test for unpacking dicts with enums
# price = defaultdict(dict)
# i = 0
# for product in list(PlainCoffeeProducts):
#     price[product] = defaultdict(dict)
#     for size in list(DrinkSize):
#         price[product][size] = defaultdict(dict)
#         for season in list(Season):
#             price[product][size][season] = i^2
#             i = i + 1

# df = pd.read_excel("prices.xlsx", header=1)
# print(df)
# print(df.info())
rng = np.random.default_rng()
# assign store numbers to each customer
# assign regular or specialty to each customer
# assign probability of food to each customer
# specialty purchasers buy more food than regular coffee people
# assign probability of merch to each customer
# specialty purchasers buy more merch than regular coffee people
# merch must be bought same day as food or drink

# start with beginning date
# customers are either alive or dead on that date
# assign store numbers to each customer
# pick customer number from alive customers
# pick store number (each customer number has 2,3, or 4 different store ids )
# pick three stores from store list w/o replacement and save in defaultdict
# store number is a defaultdict(list) where list is their potential store ids
# pick season (Spring Summer Fall Winter)
# pick DOW (Weekday Weekend)
# pick date
# plain or specialty coffee product (each customer prefers plain or specialty but can choose both)
# product id
# number of units 1,2,3 each customer usually buys 1 but can buy more [0.55, 0.35, 0.10]
# drink size SML


rng.choice(list(DrinkSize))