import pandas as pd

data = {
	'apples': [4, 2, 6, 5],
	'bananas': [1, 3, 2, 6]
}

purchases = pd.DataFrame(data)
print(purchases)
print(purchases.loc['Lee'])

"""
Output
apples     2
bananas    3
Name: Lee, dtype: int64
"""
# print(purchases.loc['Lee'])