import time
import sys

	# 	012345
	# 0	********
	# 1	*	 
	# 2	*	 
	# 3	*	***	
	# 4	*	 *
	# 5	*	 *
	# 6 	********

for row in range(7):
	for col in range(6):
		if (col==0 or (col==4) and row>2):
			print '*',
		elif (((row==0 or row==6)and (col>0 and col<5)) or ((row==3)and(col==3 or col==5))):
			print '*',
		else:
			print ' ',

	print ''
	time.sleep(0.1)
