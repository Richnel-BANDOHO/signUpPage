
import tkinter


fenBout=tkinter.Tk()

a=int(fenBout.winfo_screenwidth())
z=int(fenBout.winfo_screenheight())

larFenBout=400
lonFenBout=100

#fonction permettant de placé un élément au centre de l'ecran

def Middle(largeurEcran,longueurEcran,larFenetre,longFenetre):

    #declaration variable interne
	largeurEcran=int(largeurEcran)
	longueurEcran=int(longueurEcran)


	larFenetre=int(larFenetre)
	longueurEcran=int(longueurEcran)

	#debut fonction

	pos1=(largeurEcran/2)-(larFenetre/2)
	pos1=int(pos1)
	pos2=(longueurEcran/2)-(longFenetre/2)
	pos2=int(pos2)
	position="{}x{}+{}+{}".format(larFenetre,longFenetre,pos1,pos2)

	return position


#Fonction traduction
#Translate function

def traduction(mot,langue):

	mot=str(mot)
	langue=str(langue)

	#Les clés doivent être uniquement en minuscule
	
	dictionnaire={
		"prénom":"FirstName",
		"nom":"Name",
		"mot de passe":"Password",
		"page d'inscription":"Sign up page",
		"Tous les champs doivent être remplis.":"All fields must be completed.",
		"Confirmer le mot de passe":"Confirm password",
		"E-mail":"E-mail",
		"Nom d'utilisateur":"user name",
		"Entreprise": "Company",
		"Envoyer":"Submit"

		}
		
	if mot in dictionnaire:

		if langue=="fr":
			motTraduit=mot
		elif langue=="en":
			motTraduit=dictionnaire[mot]
	else:
		motTraduit="Le mot saisit n'as pas encore de traduction veuillez ajouter une traduction ou enlever"

	return motTraduit.capitalize()


#Commentaire français:  fonction qui fait appel a la fenêtre principale
#English commentary :main window function



def mainWindow(lang):

	langue=str(lang)


	app =tkinter.Tk()

	x=int(app.winfo_screenwidth())
	y=int(app.winfo_screenheight())
	larFen=400
	lonFen=600

#Déclaration des labels
#Label declaration 
	
	topText=tkinter.Label(app,text=traduction("Tous les champs doivent être remplis.",langue))
	
	labelFirstName=tkinter.Label(app,text=traduction("nom",langue))

	
	labPass=tkinter.Label(app,text=traduction("mot de passe",langue))
	labelLastName=tkinter.Label(app,text=traduction("prénom",langue))
	confPass=tkinter.Label(app,text=traduction("Confirmer le mot de passe",langue))
	userName=tkinter.Label(app,text=traduction("Nom d'utilisateur",langue))
	emailC=tkinter.Label(app,text=traduction("E-mail",langue))
	CompanyName=tkinter.Label(app,text=traduction("Entreprise",langue))


#declaration des Entry
#Entry declaration
	wid=64

	entrer=tkinter.Entry(app,width=wid)
	entrerMP=tkinter.Entry(app,show="*",width=wid)
	entrerPrenom=tkinter.Entry(app,width=wid)
	entryConfPass=tkinter.Entry(app,show="*",width=wid)
	entryUserName=tkinter.Entry(app,width=wid)
	entryEmail=tkinter.Entry(app,width=wid)
	entryCompany=tkinter.Entry(app,width=wid)

#declaration bouton Envoyer
#Send button declaration

		
	def sendMessage():

#Developpement de la fonction cryptage en cours
#Development of the "cryptage" fonction in progress

		def cryptage(word):
			word=str(word)
			return word

		
		a=cryptage(entrer.get())
		b=cryptage(entrerPrenom.get())
		c=cryptage(entrerMP.get())
		d=cryptage(entryConfPass.get())
		e=cryptage(entryUserName.get())
		f=cryptage(entryEmail.get())
		g=cryptage(entryCompany.get())

		for i in "abcd":

			if str(i)== None:
				print("veuillez saisir toutes les cases")

			else:
				print("Nom:{}\n\nPrénom:{}\n\nMot de passe:{}\n\nMot de passe Confirmer:{}\n\nNom d'utilisateur:{}\n\nE-mail:{}\n\nEntreprise:{}".format(a,b,c,d,e,f,g))
		

		#app.destroy()
		


	btnSend=tkinter.Button(app,width=int(wid/2),text=traduction("Envoyer",langue),command=sendMessage)

#disposition bouton Envoyer
#send button declaration
	
	posis1=(larFen/2)
	posis2=posis1-(wid/4)
	posis=posis2/2
	
	btnSend.place(x=posis,y=520)


#disposition des labels
#Label layout
	topText.place(x=5,y=20)
	labelFirstName.place(x=5,y=70)
	labelLastName.place(x=5,y=130)
	labPass.place(x=5,y=194)
	confPass.place(x=5,y=260)
	userName.place(x=5,y=320)
	emailC.place(x=5,y=380)
	CompanyName.place(x=5,y=440)
	


#disposition des Entry
#Entry layout
	hei=25

	entrer.place(x=5,y=90,height=hei)
	entrerPrenom.place(x=5,y=150,height=hei)
	entrerMP.place(x=5,y=215,height=hei)
	entryConfPass.place(x=5,y=280,height=hei)
	entryUserName.place(x=5,y=340,height=hei)
	entryEmail.place(x=5,y=400,height=hei)
	entryCompany.place(x=5,y=460,height=hei)


	app.geometry(Middle(x,y,larFen,lonFen))

	#app['background']='green'
	app.title(traduction("page d'inscription",langue))
	fenBout.destroy()

	app.mainloop()




def onclickFr():
	mainWindow("fr")
	
	
def onclickEn():
	mainWindow("en")
	





#fenBout.geometry("{}x{}".format(larFenBout,lonFenBout))

fenBout.geometry(Middle(a,z,larFenBout,lonFenBout))


btnFr=tkinter.Button(fenBout,text="Français",width=100,command=onclickFr)
btnEn=tkinter.Button(fenBout,text="English",width=100,command=onclickEn)

btnFr.pack(pady=5)
btnEn.pack()


fenBout.mainloop()

