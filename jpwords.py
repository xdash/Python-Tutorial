import random
import time
import sys
import os

arr = list()
i = 0

f = open(sys.path[0]+"/jpwords.txt","r")
for line in open(sys.path[0]+"/jpwords.txt"):
	line = f.readline()
	arr.append(line)
	i=i+1
f.close

while True:
	os.system("clear")
	print arr[random.randint(0,i)]
	time.sleep(2)

