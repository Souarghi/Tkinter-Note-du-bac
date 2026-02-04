#Tkinter Final Projet: menu_window pronote

from tkinter import*
from general import*
from techno import *

#Fenetre
menu_window=Tk()
menu_window.resizable(False,False)
menu_window.geometry('400x240')
menu_window.title("Résultat du bac2022")
menu_window.iconbitmap('cyclades-logo.ico')
image=PhotoImage(file="OIP-_1_.gif")
fond=Label(menu_window,image=image)
fond.place(x=0,y=0)

#BAC menu
texte2= Label(menu_window,text="  BAC 2022",bg="white",fg='dark blue', font=("Algerian",30))
texte2.grid(row=0,column=1)
bacG=Button(menu_window,text="Général",font=("Helvertica",16),bg="dark red",fg='black',relief="raised",command=boutonG)
bacG.grid(row=5,column=0,padx=2)
bacT=Button(menu_window,text="Techno",font=("Helvertica",16),bg="blue",fg='black',relief="raised",command=boutonT)
bacT.grid(row=5,column=2)

#BAC boucle IMPORTANT
menu_window.mainloop()