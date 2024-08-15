from subprocess import call
from tkinter import *
from tkinter import ttk, Tk
from tkinter.messagebox import *
import mysql.connector


BGCOLOR = "#164159"

root = Tk()

root.title("RESTO")
root.geometry("1350x700+2+20")
root.resizable(False,False)
root.configure(background=BGCOLOR)

#formulaire de commande
lbltitre = Label(root,text="Formulaire d'enregistrement des tables", font=('Sans Serif',18), background=BGCOLOR, foreground='#ffffff')
lbltitre.place(x=-5,y=10, width=600)

lblaliment= Label(root,text="Code aliment", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblaliment.place(x=10,y=70, width=200)
txtaliment = Entry(root, bd=4, font=("Arial",14))
txtaliment.place(x=230, y=70, width=150)

lblQte= Label(root,text="Quantité", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblQte.place(x=10,y=120, width=200)
txtQte = Entry(root, bd=4, font=("Arial",14))
txtQte.place(x=230, y=120, width=150)

lblNumTable= Label(root,text="Numero de table", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblNumTable.place(x=10,y=180, width=200)
txtNumTable = Entry(root, bd=4, font=("Arial",14))
txtNumTable.place(x=230, y=180, width=150)

btnEnreCMD = Button(root, text="Enregistrer", font=('Arial ',14),background=BGCOLOR, foreground='#fff')
btnEnreCMD.place(x=10,y=240, width=150)

btnAnnulCMD = Button(root, text="Annuler", font=('Arial ',14),background=BGCOLOR, foreground='#fff')
btnAnnulCMD.place(x=10,y=300, width=150)
txtAnnulCMD = Entry(root, bd=4, font=("Arial",14))
txtAnnulCMD.place(x=230, y=300, width=150, height=40)

btnLibererTBL = Button(root, text="LIBERER UNE TABLE", font=('Arial ',14),background=BGCOLOR, foreground='#fff')
btnLibererTBL.place(x=60,y=380, width=400)
#formulaire de commande
lblLiberer = Label(root,text="MONTANTS TOTAUX PAR TABLES", font=('Sans Serif',18), background=BGCOLOR, foreground='#ffffff')
lblLiberer.place(x=5,y=460, width=500)

# commande
commande = ttk.Treeview(root, columns=(1,2,3,4), height=10, show='headings')
commande.place(x=550, y=60, width=800, height=700)

# les entêtes
commande.heading(1, text="ID COMMANDE")
commande.heading(2, text="NUMERO DE LA TABLE")
commande.heading(3, text="COMMANDE")
commande.heading(4, text="QUANTITE")

#les dimensions de colonne
commande.column(1, width=50)
commande.column(2, width=50)
commande.column(3, width=100)
commande.column(4, width=100)


# Montant
montant = ttk.Treeview(root, columns=(1,2), height=10, show='headings')
montant.place(x=10, y=500, width=500, height=200)

# les entêtes
montant.heading(1, text="NUMERO DE LA TABLE")
montant.heading(2, text="MONTANT")

#les dimensions de colonne
montant.column(1, width=50)
montant.column(2, width=50)


root.mainloop()
