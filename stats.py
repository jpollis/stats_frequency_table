###create a random range of numbers, 0-70###
###create frequency distribution based on 5 classes###
###determine frequency of each class###

from random import randint

base_nums = list(range(70))
real_nums = []
for num in base_nums:
	real_nums.append(randint(0,70))
real_nums.sort()
# print(real_nums)
# print(len(real_nums))

###create classes and limits based on the returned width####

width = len(real_nums) / 5
# print(width)

first_class = []
second_class = []
third_class = []
fourth_class = []
fifth_class = []

first_limit = width*2
second_limit = width*3
third_limit = width*4
fourth_limit = width*5

for num in real_nums:
	if num < width:
		first_class.append(num)
	elif num >= width and num < first_limit:
		second_class.append(num)
	elif num >= first_limit and num < second_limit:
		third_class.append(num)
	elif num >= second_limit and num < third_limit:
		fourth_class.append(num)
	elif num >= third_limit and num < fourth_limit:
		fifth_class.append(num)

# print(first_class)

class_frequency = {

	"first_class_frequency": first_class,
	"second_class_frequency": second_class,
	"third_class_frequency": third_class,
	"fourth_class_frequency": fourth_class,
	"fifth_class_frequency": fifth_class

	}

for key in class_frequency:
	print(f"{len(class_frequency[key])} items in this class: {class_frequency[key]}")