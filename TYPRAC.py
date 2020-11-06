import random
import msvcrt
import time
import os

print("TYPRAC - made by Shantanu Kapse")
msvcrt.getch()
print("Make sure that you know touch typing i.e. which key should be pressed by which finger,")
print("It'll help to make your practice better.")
msvcrt.getch()
print("You can stop anytime by pressing '0'")
msvcrt.getch()


A = 'qwertyuiop'
B = 'asdfghjkl'
C = 'zxcvbnm'
s = 0
t = 0

def f(X):
    while True:
        global t
        global s
        global t1
        t += 1
        r = random.choice(X)
                      
        if t == L + 1:
            t2 = time.time()
            print("Your score =" ,s ,"out of", t-1 )
            print("Accuracy =" , round(100*s/(t-1),2) ,"%")
            print("Time taken =" , round(t2-t1 , 2) ,"seconds")
            speed = (t-1)/(t2-t1)
            print("speed = ", round(speed , 2) , "~", round(speed) , "key(s) / sec")
            print("try this level again? (y/n)")
            p = msvcrt.getch().decode('utf-8')
            if p == 'n':                    
                break
            else :      #resetting the values 
                t = 1
                s = 0
                t1 = time.time()
                    
        print(r)
        n = msvcrt.getch().decode('utf-8')    
        if n == '0' :
            t2 = time.time()
            print("Your score =" ,s ,"out of", t-1 )
            if t != 1:
                print("Accuracy =" , round(100*s/(t-1),2) ,"%")
            print("Time taken =" , round(t2-t1 , 2) ,"seconds")
            speed = (t-1)/(t2-t1)
            print("speed = ", round(speed , 2) , "~", round(speed) , "key(s) / sec")
            print("try this level again? (y/n)")
            p = msvcrt.getch().decode('utf-8')
            if p == 'n':                   
                break
            else :      #resetting the values 
                t = 0
                s = 0
                t1 = time.time()
                    
        if n == r :
            s = s + 1
        if n != r and n != '0' :
            if n == 'y' and r == 'y':
                pass
            else :
                print("wrong")
    
    
    
while True:
    L = int(input("Enter the max limit of letters you wanna practice in each level : " ))
    print("press '1' for qwerty row only")
    print("press '2' for asdf row only")
    print("press '3' for zxcvb row only")
    print("press '4' for qwerty and asdf rows")
    print("press '5' for asdf and zxcvb rows")
    print("press '6' for the whole keyboard")
    print("press '0' to stop afterwards")
    
    i = msvcrt.getch().decode('utf-8')  
    t1 = time.time()
    
    if i == '1':
        f(A)
            
    if i == '2':
        f(B)
    
    if i == '3':
        f(C)
        
    if i == '4':
        f(A + B)
        
    if i == '5':
        f(B + C)
        
    if i == '6':
        f(A + B + C)
    
    
    
    print("choose another level?    (y/n)")
    d = msvcrt.getch().decode('utf-8')
    if d == 'n':
        break
    else:
        s = 0
        t = 0
        os.system('cls')
        
    
