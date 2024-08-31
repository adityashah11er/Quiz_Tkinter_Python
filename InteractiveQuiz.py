import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox

root = tk.Tk()
root.geometry('720x500')
root.minsize(200,200)
root.maxsize(2000,2000)


questions = ["int(0.5*77) is: ","Which of the Following is a Back-End Language?","Who invented 0?","What Sport did Kobe Bryant excel at?","How many minutes in 10.5 hours?","What pigment gives Plants the Green color?","Mean of the Data (11,22,33) is: "]
options = [["38","39","40","37","38"],["JavaScript","HTML","CSS","Python","Python"],["Archimedis","Aryabhatta","Pythagoras","Aristotle","Aryabhatta"],["Football","Cricket","Basketball","Golf","Basketball"],["640","630","605","700","630"],["Chlorophyll","Iron Oxide","Amalgam","Orange Juice","Chlorophyll"],["11","22","33","20","22"]]


frame = tk.Frame(root, padx=10, pady=10,bg='black')
question_label = tk.Label(frame,height=5, width=35,bg='Maroon',fg="White", 
                          font=('Yu Gothic', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="black",fg='White', variable=v1, font=('Yu Gothic', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="black",fg='White', variable=v2, font=('Yu Gothic', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="black",fg='White', variable=v3, font=('Yu Gothic', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="black",fg='White', variable=v4, font=('Yu Gothic', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='yellowgreen', font=('Yu Gothic', 20), 
                        command = lambda : displayNextQuestion())


frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0


def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'




displayNextQuestion()

root.mainloop()