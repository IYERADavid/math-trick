import random
import  operator
import time
import pyttsx3

def random_problem():
    operators ={
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv,
    }

    num_1= random.randint(7,15)
    num_2= random.randint(7,15)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1,num_2)
    print('what is '+ str(num_1)+ str(operation)+ str(num_2) +'?')
    return answer        
 

def ask_questions():
    answer = random_problem()
    user = float (input())
    return user == answer

def caller():
    print("we are on "+time.asctime())
    name =raw_input("what is your name:")
    print("you have less than 20 seconds for each question\n if you take more than 20 seconds\n we will not count marks of that question")
    print ("hey lets start math game now")
    print("-----------------------------------\n")
    score = 0
    marks = 0
    time.sleep(6)
    for i in range(4):
        time.sleep(4)
        start=time.time()
        stan=time.time()
        if ask_questions() == True:
            score +=1
            marks +=1
            print('correct')    

            sound =pyttsx3.init()

            rate =sound.getProperty("rate")
            sound.setProperty("rate",5)
            volume = sound.getProperty("volume")
            sound.setProperty("volume",1)
            #voices = sound.getProperty("voices")
            #sound.setProperty("voice",voices[1].id) 
            say = "correct"
            sound.say(say)
            sound.runAndWait()
            sten=time.time()  

            if sten-stan >= 21:
                sound =pyttsx3.init()

                rate =sound.getProperty("rate")
                sound.setProperty("rate",5)
                volume = sound.getProperty("volume")
                sound.setProperty("volume",1)
                #voices = sound.getProperty("voices")
                #sound.setProperty("voice",voices[1].id) 
                say = "but your time is finished"
                sound.say(say)
                sound.runAndWait()    
        else:
            marks +=1
            print('Wrong')    

            sound =pyttsx3.init()

            rate =sound.getProperty("rate")
            sound.setProperty("rate",5)
            volume = sound.getProperty("volume")
            sound.setProperty("volume",1)
            #voices = sound.getProperty("voices")
            #sound.setProperty("voice",voices[1].id) 
            say = "wrong"
            sound.say(say)
            sound.runAndWait()
        end=time.time()
        print("used time to answer:",end-start,"seconds")
        if end-start >= 21:    
            score -=1
        
    print("your total score is " + str(score) + "/" + str(marks))

    if score > marks/2:
        print(name + " you win")

        sound =pyttsx3.init()

        rate =sound.getProperty("rate")
        sound.setProperty("rate",5)
        volume = sound.getProperty("volume")
        sound.setProperty("volume",1)
        #voices = sound.getProperty("voices")
        #sound.setProperty("voice",voices[1].id) 

        say = name + " you win" 
        sound.say(say)
        sound.runAndWait()
    else:
        print(name +" you lose")
        sound =pyttsx3.init()

        rate =sound.getProperty("rate")
        sound.setProperty("rate",5)
        volume = sound.getProperty("volume")
        sound.setProperty("volume",1) 
        #voices = sound.getProperty("voices")
        #sound.setProperty("voice",voices[1].id) 

        say = name + " you lose" 
        sound.say(say)
        sound.runAndWait()

caller() 