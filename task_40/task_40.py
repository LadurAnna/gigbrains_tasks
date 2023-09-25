

"""Задача 40: Работать с файлом california_housing_train.csv,
который находится в папке sample_data. Определить среднюю 
стоимость дома, где кол-во людей от 0 до 500 (population)."""

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
       "households" : s[6],
       "median_income" : s[7],
       "median_house_value" : int(float(s[8])),
       }
    california_housing.append(cht)

sum_value = 0
n = 0
for hous in california_housing:
    if hous["population"] >= 0 and hous["population"] <= 500:
       n +=1
       sum_value +=  hous["median_house_value"]

print()
print("avege: ", float(sum_value)/n)


