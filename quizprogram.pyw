from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import Tk, Frame, Label, Button

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        ttk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        ttk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        ttk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        ttk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="" + str(right) + " of " + str(number_of_questions) + " questions\n answered right!", font=('Coral', 30)).pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = ThemedTk(theme="radiance")
window.title('Quiz Application')
window.iconbitmap('quiz.ico')
window.geometry("400x300+520+0")
window.resizable(0,0)
button = ttk.Button(window, text="Start", command=askQuestion)
button.pack()
window.mainloop()
