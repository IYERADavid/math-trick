import random
import time

y=2
z=3
x=4
g=5

for i in range(1,11):
	print (str (y)+'x'+str(i)+'= '+str(y*i)+' |' +str (z)+'x'+str(i)+'= '+str(z*i)+' | ' +str (x)+'x'+str(i)+'= '+str(x*i)+' | ' +str (g) +'x'+str(i)+'= '+str(g*i)) 
	
time.sleep (7)
print ('10000000000'*1000000) 
	
def random_problem():
	num1=random. randint(1,5)
	num2=random. randint(1,5)
	answer =num1*num2
	dwerty=num1*num2
	print(' ' +str(num1)+'x'+str(num2)+ '\n|____|') 
	return answer
	
def qwestion() :
	answer =random_problem ()
	guess =float(input('your answer:'))
	return answer ==guess 
	
def ask_question() :
	score =0
	marks =0	
	qwerty =0
	print('--------------------------------------')
	print ('NB: you have less than 20 seconds to answer each qwestion')
	print ('so we will not count the marks of that question')
	special=time.time()
	for i in range (4):
		time.sleep(3)
		qwerty +=1
		print ('Q'+str(qwerty)+')') 
		start =time.time()
		sten=time.time()
		if qwestion() == True:
			print ('correct ') 
			score +=1
			marks +=1
			set=time.time()	
		else:
			print ('wrong')
			marks +=1
		end = time.time()
		print ('time used =', end-start, 'seconds') 
		print ('-------------------------------------')
		if set-sten >=21:
			print(' your time has already finished')
			print ('0 mark \n-------')
			score  -=1
	spenal=time.time()
	print('your total marks is'+str (score)+'/'+str (marks)) 
	print ('your total time used is ', spenal-special-12.53, 'seconds') 
	print ('.                  ')
		
	if score == marks:
		print ('Excellent') 
	elif score == marks-1:
		print ('very good')
	elif score >= marks/2+1 and not score >=marks-1:
		print ('good') 
	else:
		print ('poor marks?') 
		print ('') 
	print ('stay home , stay safe\n') 		
ask_question()
time. sleep(5)
#print ('10000000000'*1000000000) 
		