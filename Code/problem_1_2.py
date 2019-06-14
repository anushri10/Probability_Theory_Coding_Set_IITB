import random
import numpy as np
#n = int(input("Number of times die is rolled: "))
n=[0,10,39,500000,1000000000]
num=1
for val in n:
	if(0<val<100000000):
		print(val)
		choices = [1,2,3,4,5,6]
		dice = list(range(1,7))
		weights_1 = [0.09,0.09,0.50,0.10,0.15,0.07] 
		name = 'problem_1.2_test'+str(num)
		with open(name+'.txt', 'w') as f:
			count = 0
			while count<val:
				rnd_1 = np.random.choice(choices, p=weights_1)
				f.write('%d' % rnd_1)  #50% is 3
				index = np.random.randint(0,2)
				if(index == 0):
					index = np.random.randint(0,6)
					f.write('%d' % dice[index]) 		#more than 50% 6
					index = np.random.randint(0,2)		#following if-else block for less than 50% 1
					if index==0:
						f.write('%d' % dice[index]+'\n')
					else:
						index = np.random.randint(0,6)
						f.write('%d' % dice[index]+'\n')
					count+=1
				else:
					count+=1
					#print(dice[-1],'\n')
					f.write('%d' % dice[-1])		#ensuring this 50% has 6
					index = np.random.randint(1,6)
					f.write('%d' % dice[index]+'\n')	#ensuring this 50% has no 1		
	else:
		print("Invalid dice roll entry\n")
	num+=1
#print(dice)
