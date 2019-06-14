import random

#n = int(input("Number of times die is rolled: "))
n=[0,10,39,500000,1000000000]
num=1
for val in n:
	if(0<val<100000000):
		print(val)
		dice = list(range(1,7))
		name = 'problem_1.1_test'+str(num)
		with open(name+'.txt', 'w') as f:
			for x in range(val):
				index = random.randint(0,5)
				#print(dice[index])
				f.write('%d' % dice[index]+'\n')
	else:
		print("Invalid dice roll entry\n")
	num+=1
#print(dice)
