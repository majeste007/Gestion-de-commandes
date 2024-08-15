"""
    Gestion des commandes des clients
"""

from subprocess import call
from tkinter import *
from tkinter import ttk, Tk
from tkinter.messagebox import *
import mysql.connector

BGCOLOR = "#164159"

#ajouter dans la table
def ajouterTable():
    num_table = txttable.get()
    nbre_chaise = txtchaise.get()
    s_etat = 'Libre'
    maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
    meConnect = maBase.cursor()
    try:
        rSql = "INSERT INTO r_table(numero_table, nombre_chaise,etat) VALUES(%s,%s,%s)"
        val = (num_table,nbre_chaise,s_etat)
        meConnect.execute(rSql, val)
        maBase.commit()
        showinfo("Information","Table Ajouter")
        root.destroy()
        call(['python','main.py'])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()

def supprimerTable():
    num_table = txttable.get()
    maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
    meConnect = maBase.cursor()
    try:
        rSql = "DELETE FROM r_table WHERE numero_table=%s"
        val = (num_table,)
        meConnect.execute(rSql, val)
        maBase.commit()
        showinfo("Information","Table suppimer")
        root.destroy()
        call(['python','main.py'])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()



#ajouter dans la Aliment
def ajouterAliment():
    codeAliment = txtCodeAliment.get()
    nomAliment = txtNomAliment.get()
    prixAliment = txtPrixAliment.get()
    maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
    meConnect = maBase.cursor()
    try:
        rSql = "INSERT INTO aliment(code_aliment, nom_aliment,prix_aliment) VALUES(%s,%s,%s)"
        val = (codeAliment,nomAliment,prixAliment)
        meConnect.execute(rSql, val)
        maBase.commit()
        showinfo("Information","Aliment Ajouter")
        root.destroy()
        call(['python','main.py'])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()

def supprimerAliment():
    codeAliment = txtCodeAliment.get()
    maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
    meConnect = maBase.cursor()
    try:
        rSql = "DELETE FROM aliment WHERE code_aliment=%s"
        val = (codeAliment,)
        meConnect.execute(rSql, val)
        maBase.commit()
        showinfo("Information","Aliment suppimer")
        root.destroy()
        call(['python','main.py'])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()







root = Tk()

root.title("RESTO")
root.geometry("1350x700+2+20")
root.resizable(False,False)
root.configure(background=BGCOLOR)

# Formlaire d'enregistrement des tables
lbltitre = Label(root,text="Formulaire d'enregistrement des tables", font=('Sans Serif',18), background=BGCOLOR, foreground='#ffffff')
lbltitre.place(x=-5,y=10, width=600)

lbltable= Label(root,text="Numero de table", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lbltable.place(x=10,y=70, width=200)

txttable = Entry(root, bd=4, font=("Arial",14))
txttable.place(x=200, y=70, width=150)

lblchaise= Label(root,text="Nombre de chaise", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblchaise.place(x=10,y=120, width=200)

txtchaise = Entry(root, bd=4, font=("Arial",14))
txtchaise.place(x=200, y=120, width=150)

btnEnreTable = Button(root, text="Enregistrer", font=('Arial ',14),background=BGCOLOR, foreground='#fff',command=ajouterTable)
btnEnreTable.place(x=100,y=170, width=150)

btnSuppTable = Button(root, text="Supprimer", font=('Arial ',14),background=BGCOLOR, foreground='#fff', command=supprimerTable)
btnSuppTable.place(x=300,y=170, width=150)

# tables
table = ttk.Treeview(root, columns=(1,2,3), height=10, show='headings')
table.place(x=550, y=60, width=800, height=200)

# les entêtes
table.heading(1, text="NUMERO DE TABLE")
table.heading(2, text="NOMBRE DE CHAISE")
table.heading(3, text="ETAT")

#les dimensions de colonne
table.column(1, width=50)
table.column(2, width=50)
table.column(3, width=100)

###Afficher les informations de la table
maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
meConnect = maBase.cursor()
meConnect.execute("SELECT * FROM r_table")
for row in meConnect:
    table.insert('',END,value=row)
maBase.close()

###################################################################################################################
# Formlaire d'enregistrement des aliments
lblTitreAliment = Label(root,text="Formulaire d'enregistrement des aliments", font=('Sans Serif',18), background=BGCOLOR, foreground='#ffffff')
lblTitreAliment.place(x=-5,y=300, width=600)

lblCodeAliment= Label(root,text="Code aliment", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblCodeAliment.place(x=10,y=360, width=150)
txtCodeAliment = Entry(root, bd=4, font=("Arial",14))
txtCodeAliment.place(x=200, y=360, width=150)

lblNomAliment= Label(root,text="Nom aliment ", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblNomAliment.place(x=10,y=400, width=150)
txtNomAliment = Entry(root, bd=4, font=("Arial",14))
txtNomAliment.place(x=200, y=400, width=300)

lblPrixAliment= Label(root,text="Prix aliment ", font=('Sans Serif ',14),background=BGCOLOR, foreground='#fff')
lblPrixAliment.place(x=10,y=440, width=150)
txtPrixAliment = Entry(root, bd=4, font=("Arial",14))
txtPrixAliment.place(x=200, y=440, width=150)


#bouton de validation de l'aliment
btnEnreAliment = Button(root, text="Enregistrer", font=('Arial ',14),background=BGCOLOR, foreground='#fff',command=ajouterAliment)
btnEnreAliment.place(x=100,y=500, width=150)
btnSuppAliment = Button(root, text="Supprimer", font=('Arial ',14),background=BGCOLOR, foreground='#fff',command=supprimerAliment)
btnSuppAliment.place(x=300,y=500, width=150)

# bouton divers
btnActuAliment = Button(root, text="Actualiser", font=('Arial ',14),background=BGCOLOR, foreground='#fff')
btnActuAliment.place(x=100,y=570, width=150)

btnComAliment = Button(root, text="Commander", font=('Arial ',14),background=BGCOLOR, foreground='#fff')
btnComAliment.place(x=300,y=570, width=150)

# tables
aliment = ttk.Treeview(root, columns=(1,2,3), height=10, show='headings')
aliment.place(x=550, y=340, width=800, height=340)

# les entêtes
aliment.heading(1, text="Code Aliment".upper())
aliment.heading(2, text="Nom aliment".upper())
aliment.heading(3, text="Prix aliment".upper())

#les dimensions de colonne
aliment.column(1, width=50)
aliment.column(2, width=50)
aliment.column(3, width=100)
###Afficher les informations de la table
maBase = mysql.connector.connect(host='localhost',user='root',password='',database='resto')
meConnect = maBase.cursor()
meConnect.execute("SELECT * FROM aliment")
for row in meConnect:
    aliment.insert('',END,value=row)
maBase.close()




root.mainloop()

