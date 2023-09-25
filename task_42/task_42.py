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
       "total_rooms" : s[3],
       "total_bedrooms" : s[4],
       "population" : int(float(s[5])),
       "households" : int(float(s[6])),
       "median_income" : s[7],
       "median_house_value" : int(float(s[8])),
       }
    california_housing.append(cht)

min_population = min([h["population"] for h in california_housing])

max_households = max([h["households"] for h in california_housing if h["population"] == min_population])
print(max_households)




