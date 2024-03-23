words=['apple','electric','mobile','sea','door','flowers','jury','places','zimbabwe','korean','spain',
'jellyfish','traitor','logarithm','meter','word','suggest','correct','impulse','shower','clothes', 
'after', 'afternoon', 'again', 'against', 'age', 'agency', 'agenda', 'agent', 'aggressive', 'ago', 'boss', 
'both', 'bother', 'bottle', 'bottom', 'boundary', 'bowl', 'box', 'campaign', 'campus', 'can', 'Canadian', 
'cancer', 'candidate', 'cap', 'capability', 'capable', 'commercial', 'commission', 'commit', 'commitment', 'committee', 
'common', 'communicate', 'communication', 'community']
def labelslider():
    global count,sliderWords
    text='Welcome To Typing Speed Game'
    if(count>= len(text)):
        count=0
        sliderWords=''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(300,labelslider)
def time():
    global timeleft,score,miss
    if (timeleft>0):
        timeleft -=1
        timeLabelcount.configure(text=timeleft)
        timeLabelcount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit ={} | Miss = {} | Total Score = {} '.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timeLabelcount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelcount.configure(text=score)
def startGame(event):
    global score,miss
    if(timeleft == 60):
        time( )
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score +=1
        scoreLabelcount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox
######################## root method
root=Tk()
root.geometry('800x500+250+100')
root.configure(bg='purple')
root.title('Typing Speed Game')
######################## variables
score=0
timeleft=60
count=0
sliderWords=''
miss=0
######################## label method
fontLabel=Label(root,text='',font=('arial',25,'italic bold'),bg='purple',fg='white',width=40)
fontLabel.place(x=1,y=10)
labelslider()
random.shuffle(words)
wordLabel=Label(root,text=words[0],font=('arial',40,'italic bold'))
wordLabel.place(x=315,y=100)
scoreLabel=Label(root,text='Your score : ',font=('arial',25,'italic bold'),bg='violet',fg='black')
scoreLabel.place(x=10,y=100)
scoreLabelcount=Label(root,text=score,font=('arial',25,'italic bold'),bg='violet',fg='black')
scoreLabelcount.place(x=80,y=150)
timerLabel=Label(root,text='Time left : ',font=('arial',25,'italic bold'),bg='violet',fg='black')
timerLabel.place(x=600,y=96)
timeLabelcount=Label(root,text=timeleft,font=('arial',25,'italic bold'),bg='violet',fg='black')
timeLabelcount.place(x=685,y=150)
gamePlayDetailLabel=Label(root,text='Type Word And Hit Enter',font=('arial',20,'italic bold'),bg=
'purple',fg='violet')
gamePlayDetailLabel.place(x=200,y=300)
######################### entry method
wordEntry=Entry(root,font=('arial',30,'bold'),bd=10,justify='center')
wordEntry.place(x=175,y=200)
wordEntry.focus_set()
#####################
root.bind('<Return>',startGame)
root.mainloop()