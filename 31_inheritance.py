from chef import Chef
from chinese_chef import Chinese_Chef


myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChinese_Chef = Chinese_Chef()
myChinese_Chef.make_chicken() # Inherited from chef.py
myChinese_Chef.make_fried_rice()
myChinese_Chef.make_special_dish() # Class overridden in chinese_chef.py so make_special_dish class is different from chef.py