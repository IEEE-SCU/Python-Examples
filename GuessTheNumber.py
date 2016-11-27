#Author:D4Vinci
#Just guess the number computer thinking in :D

import random
print "Welcome To Guess The Number Game By Karim Shoair"
print "Now You Will Try To Guess The Number I am Thinking In :)"
guessed=random.randint(1,20)
t=0
def right(num):
    print "Well Done!! You Guessed My Number After {} Times!!".format(num)
    exit
while t < 8 and t != "stop":
    gg=raw_input("Between (1-20)--> ")
    t+=1
    if int(gg) > int(guessed):
        print "Number Is Too High :) (Try Again)"
    if int(gg) < int(guessed):
         print "Number Is Too Low :) (Try Again)"
    if int(gg) == int(guessed):
        right(t)
        t="stop"
if t==8 or t>8 and t is not "stop":
    print "Too Much Time To Guess Try Much Harder My Number Is "+str(guessed)
