#!/usr/bin/python3
import random

random_num = random.randint(-10,10)

if random_num ==0:
	status = "zero" 
elif random_num >0:
	status = "positive"
else:
	status = "negativ"

result = "{} is {}"

print(result.format(random_num,status))
