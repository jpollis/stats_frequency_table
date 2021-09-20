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

first_limit = width
second_limit = width*2
third_limit = width*3
fourth_limit = width*4
fifth_limit = width*5

first_lower_lim = first_limit - first_limit
second_lower_lim = second_limit - first_limit
third_lower_lim = third_limit - first_limit
fourth_lower_lim = fourth_limit - first_limit
fifth_lower_lim = fifth_limit - first_limit

for num in real_nums:
	if num < first_limit:
		first_class.append(num)
	elif num >= first_limit and num < second_limit:
		second_class.append(num)
	elif num >= second_limit and num < third_limit:
		third_class.append(num)
	elif num >= third_limit and num < fourth_limit:
		fourth_class.append(num)
	elif num >= fourth_limit and num < fifth_limit:
		fifth_class.append(num)

# print(first_class)

class_frequency = {

	"first_class_frequency": [first_lower_lim, first_limit, first_class],
	"second_class_frequency": [second_lower_lim, second_limit, second_class],
	"third_class_frequency": [third_lower_lim, third_limit, third_class],
	"fourth_class_frequency": [fourth_lower_lim, fourth_limit, fourth_class],
	"fifth_class_frequency": [fifth_lower_lim, fifth_limit, fifth_class]

	}

for key in class_frequency:
	print(
		f"{len(class_frequency[key][2])} items between {class_frequency[key][0]} and {class_frequency[key][1]}: {class_frequency[key][2]}")


for key in class_frequency:
	print(f'{int(class_frequency[key][0])} - {int(class_frequency[key][1])}: {len(class_frequency[key][2])}')