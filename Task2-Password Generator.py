
# Random Password Generator

from tkinter import*
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(Length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

    #password=random.sample(all,password_length)
    #passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
root = Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordlabel= Label(root,text='Password Generator', font=('times new roman',20,'bold'), bg='gray20',fg='white')
passwordlabel.grid(pady=10)

weakradioButton= Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton= Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton= Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

Lengthlabel= Label(root,text='Password Generator', font=('Font',20,'bold'), bg='gray20',fg='white')
Lengthlabel.grid(pady=5)

Length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
Length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font='Font', command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font='Font')
passwordField.grid(pady=5)

copyButton=Button(root,text='Copy',font='Font')
copyButton.grid(pady=5)

root.mainloop()