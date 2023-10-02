import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
rez = pd.DataFrame({"human":[int(x=="human") for x in lst], "robot":[int(x=="robot") for x in lst]})
rez
