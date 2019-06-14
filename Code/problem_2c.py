import random
import numpy as np
import matplotlib.pyplot as plt
#n = int(input("Number of times die is rolled: "))
n=[0,10,39,500000,1000000000]
num=1
for val in n:
	values=[0,0,0,0,0,0]
	dice = list(range(1,7))
	if(0<val<100000000):
		print(val) 
		name = 'problem_2_c_test'+str(num)
		#with open(name+'.txt', 'w') as f:
		count = 0
		while count<val:
			index = np.random.randint(0,2)
			if(index == 0):
				#print(dice[2])
				index = np.random.randint(0,2)
				if index==0:
					values[index]+=1
					count+=1
				else:
					index = np.random.randint(0,6)
					values[index]+=1 
					count+=1
			else:
				count+=1
				#print(dice[-1])
				index = np.random.randint(1,6)
				values[index]+=1

		value=np.array(values)
		#print(value)
		value = value/val
		print(value)
		dice =np.array(dice) 
		plt.bar(dice, value, 0.8)
		plt.ylabel("Probability")
		plt.xlabel("Dice Face")
		plt.title("Histogram")
		plt.axis([1,6,0,1])
		plt.show()
	else:
		print("Invalid dice roll entry\n")
	num+=1
#print(dice)
	

