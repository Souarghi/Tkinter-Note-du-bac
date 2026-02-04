#general_window
from tkinter import*
from tkinter import messagebox
        
def boutonG():
    global liste_Entry
    global liste_Entry2
    global Coef1er
    global CoefTerm
    global myframe

#Parametre fenetre
    general_window=Tk()
    general_window.resizable(False,False)
    general_window.title("Résultat du bac général 2022")
    general_window.iconbitmap('Capture-d’écran-2022-12-21-120922.ico')
    
#Scrool Bar proram
    general_canvas=Canvas(general_window,height=485,width=600,highlightthickness=0)
    general_canvas.pack(side=LEFT)
    yscrollbar=Scrollbar(general_window,orient ='vertical',command=general_canvas.yview)
    yscrollbar.pack(side=RIGHT,fill='y')
    general_canvas.configure(yscrollcommand=yscrollbar.set)
    general_canvas.bind('<Configure>', lambda e :general_canvas.configure(scrollregion=(0,0,830,830)))
    myframe=Frame(general_canvas, height=900,width=400,background="dark red")
    general_canvas.create_window((0,0),window=myframe,anchor='nw')

#Aide Calcule de moyenne annuelle 
    aidebar=Menu(general_window)
    aideHelp=Menu(aidebar,tearoff=0)
    aidebar.add_cascade(label="Comment calculer ma moyenne ?",menu=aideHelp)
    aideHelp.add_command(label="Calcul moyenne trimestriellle :",command=aide)
    general_window.config(menu=aidebar)
        
#Liste Matiere, Note, Coef
    MatierePrem=["LV1 1er","LV2 1er","Histoire-Géo 1er","E.Scientifique 1er","EMC 1er","Spé 1er","Français Oral","Français Ecrit"]
    Coef1er=[3,3,3,3,1,8,5,5]
    liste_Entry=[None]*8
    MatiereTerm=["LV1 Term","LV2 Term","Histoire-Géo Term","E.Scientifique Term","EPS","EMC Term","Spé 1","Spé 2","Philosophie","Grand Oral"]
    CoefTerm=[3,3,3,3,6,1,16,16,8,10]
    liste_Entry2=[None]*10

#Programme Epreuve PREMIERE
    for i in range(len(MatierePrem)): 
        Canvas_P=Canvas(myframe,bg="dark blue",bd=6)
        Canvas_P.grid(row=4+i,column=0,padx=5,pady=5)
        liste_Entry[i]=Entry(Canvas_P, font=('Arial',10),bd=6)
        liste_Entry[i].grid(row=1,column=1,padx=5,pady=5)
        text_P=Label(Canvas_P,text= MatierePrem[i] ,bg='dark blue',fg='white', font=('arial',10))
        text_P.grid(row=0 ,column=0,padx=5,pady=5)
        coef_P = Label(Canvas_P, text=str(Coef1er[i]) ,bg='dark blue',fg='white',font=('arial',10))
        coef_P.grid(row=0,column=1,padx=5,pady=5)
        moyenne_P=Label(Canvas_P,text='Moyenne Annuelle',bg='grey',fg='dark blue',font=('arial',10))
        moyenne_P.grid(row=1,column=0,padx=5,pady=5)

#Programme Epreuve TERMINAL
    for j in range(len(MatiereTerm)): 
        Canvas_T= Canvas(myframe,bg="dark blue",bd=6)
        Canvas_T.grid(row=4+j,column=3,padx=5,pady=5)
        liste_Entry2[j]=Entry(Canvas_T, font=('Arial',10),bd=6)
        liste_Entry2[j].grid(row=1,column=1,padx=5,pady=5)
        texte_T =Label(Canvas_T,text= MatiereTerm[j] ,bg='dark blue',fg='white', font=('arial',10))
        texte_T.grid(row=0 ,column=0,padx=5,pady=5)
        coef_T=Label(Canvas_T,text=str(CoefTerm[j]),bg='dark blue',fg='white',font=('arial',10))
        coef_T.grid(row=0,column=1,padx=5,pady=5)
        moyenne_T=Label(Canvas_T,text='Moyenne Annuelle',bg='grey',fg='dark blue',font=('arial',10))
        moyenne_T.grid(row=1,column=0,padx=5,pady=5) 
    
#BOUTON VALIDER NOTE
    valider=Button(myframe,text='Valider',fg='black',font=('arial',15),relief="raised",command=moy)
    valider.grid(row=12,column=0)
    
#IMPORTANT
    general_window.mainloop()

#Programme aide calcul trimestre
def aide():
    global note
    global trimeste
    global aide
    #fenetre aide
    aide=Tk()
    aide.resizable(False,False)
    aide.title("Calcul moyenne trimestriellle:")
    #liste trimestre
    trimestre=["Trimestre 1","Trimestre 2","Trimestre 3"]
    note=[None]*3
    #creation des blocs trimestre 
    for i in range(3): 
        Canva=Canvas(aide,bg="dark blue")
        Canva.grid(row=4+i,column=0,padx=5,pady=5)
        note[i]=Entry(Canva, font=('Arial',10))
        note[i].grid(row=1,column=1,padx=5,pady=5)
        textm=Label(Canva,text= trimestre[i] ,bg='dark blue',fg='white', font=('arial',10))
        textm.grid(row=0 ,column=0,padx=5,pady=5)
        moyennem=Label(Canva,text='Moyenne Trimestrielle',bg='grey',fg='dark blue',font=('arial',10))
        moyennem.grid(row=1,column=0,padx=5,pady=5)

    #Calule moyenne aide
    def moy2():
        global note
        global trimeste
        global aide
        try:
            som=0
            for i in range(3):
                n=float(note[i].get())
                som=som+n
            an=som/3
            Result2=Label( aide ,text=str(an), fg='black',font=('arial',10))
            Result2.grid(row=12,column=1)
        except :
            messagebox.showinfo("Erreur","Remplissez tout avant de valider !")
    #BOUTON VALIDER NOTE
    valider=Button(aide,text='Valider',fg='black',font=('arial',15),relief="raised",command=moy2)
    valider.grid(row=12,column=0)

#Programme moyenne BAC
def moy():
    global liste_Entry
    global liste_Entry2
    global Coef1er
    global CoefTerm
    global myframe
    coeftot=0
    g=0
    try:
        for i in range (len(Coef1er)):
            n= float(liste_Entry[i].get())
            coef= Coef1er[i]
            coeftot=coeftot+coef
            g= g+(n*coef)
        for i in range(len(CoefTerm)):
            n=float(liste_Entry2[i].get())
            coef=CoefTerm[i]
            coeftot=coeftot+coef
            g= g+(n*coef)
    except :
            messagebox.showinfo("Erreur","Remplissez tout avant de valider !")
#Calcule du resultat
    moyenneBG=g/coeftot
    if moyenneBG>=16:
        Result=Label(myframe,text=("Felicitation ! Vous avez votre Bac MENTION TRES BIEN:",moyenneBG), fg='black',font=('arial',10))
        Result.grid(row=13,column=0)
    elif moyenneBG>=14:
        Result=Label(myframe,text=("Felicitation ! Vous avez votre Bac MENTION BIEN:",moyenneBG), fg='black',font=('arial',10))
        Result.grid(row=13,column=0)
    elif moyenneBG>=12:
        Result=Label(myframe,text=("Felicitation ! Vous avez votre Bac MENTION ASSEZ BIEN:",moyenneBG), fg='black',font=('arial',10))
        Result.grid(row=13,column=0)
    elif moyenneBG>=10:
        Result=Label(myframe,text=("Felicitation ! Vous avez votre Bac sans mention:",moyenneBG), fg='black',font=('arial',10))
        Result.grid(row=13,column=0)
    else:
        Result=Label(myframe,text=("Malheureusement vous n'etes pas ADMIS:",moyenneBG), fg='black',font=('arial',10))
        Result.grid(row=13,column=0)