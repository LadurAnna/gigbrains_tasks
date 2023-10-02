"""Задача 42: Узнать какая максимальная households в зоне минимального значения population.
"""
f = open("california_housing_test.csv", "r", encoding="utf-8")
data = f.read()
f.close()

data = data.split("\n")[1:]

california_housing = []
for s in data:
    s = s.split(",")
    if len(s) < 9:
        continue
    cht = {"longitude": s[0],
       "latitude" : s[1],
       "housing_median_age" : s[2],
       "total_rooms" : int(float(s[3])),
       "total_bedrooms" : int(float(s[4])),
       "population" : int(float(s[5])),
       "households" : int(float(s[6])),
       "median_income" : s[7],
       "median_house_value" : int(float(s[8])),
       }
    california_housing.append(cht)

min_population = min([h["population"] for h in california_housing])

max_households = max([h["households"] for h in california_housing if h["population"] == min_population])
print(max_households)
"""Найти максимальный households среди тех домов, 
у которых total_rooms >= 200 и total_bedrooms >= 100"""

"""max_households2 = 0
for k in california_housing:
    if k["total_rooms"] >= 200 and k["total_bedrooms"] >= 100:
        households2 = k["households"]
        if households2 > max_households2:
            max_households2 = households2
print(max_households2)"""

max_households2 = max([k["households"] for k in california_housing if k["total_rooms"] >= 200 and k["total_bedrooms"] >=100 ])
print(max_households2)












