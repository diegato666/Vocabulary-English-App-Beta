from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

def dictionarystart():
	
	lista=[('entire','todo'),('groovy','maravilloso'),('hauled','arrastrado'),('soaring','altisimo(Dios)')]


		


	def functiondictionay():
		def exitoption():
					
			try:
				database=sqlite3.connect('dictionary')
				cursor1=database.cursor()

				cursor1.execute('''
					CREATE TABLE SHEET (
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					WORD VARCHAR(50) ,
					MEANING VARCHAR(150))
					''')

				cursor1.executemany('INSERT INTO SHEET VALUES (NULL,?,?)', lista)

				database.commit()
				database.close()
			except:
				pass



		frame1=Frame()
		frame1.place(x=0,y=0)
		lienzo=Canvas(frame1,width=571,height=336)
		imagen=ImageTk.PhotoImage(Image.open('bandera.jpg'))
		lienzo.create_image(0,0,anchor=NW,image=imagen)
		lienzo.pack()

		texto=Listbox(frame1)
		scrolly=Scrollbar(frame1,command=texto.yview,width=18)
		scrolly.place(in_=texto, relx=1, relheight=1, bordermode="outside")
		texto.config(width=47,height=21)
		texto.place(x=270)






		#def insertwords():
		def function2():

			
			#punto='.'
			lista2=[]
			lista3=[]
			listamuestra=[]
			database=sqlite3.connect('dictionary')
			cursor1=database.cursor()
			for x in cursor1.execute('SELECT ID,WORD,MEANING FROM SHEET ORDER BY WORD '):
				lista2.append(x)
			for x in lista2:
				y=(x[0],'.',x[1].capitalize(),':',x[2].capitalize())
				listamuestra.append(y)
			print(listamuestra)
			for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
				lista3.append(x)
			'''print('lista2',lista2)
			print('lista3',lista3)	'''
			cursor1.execute('DROP TABLE SHEET')
			cursor1.execute('''
				CREATE TABLE SHEET (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				WORD VARCHAR(50) ,
				MEANING VARCHAR(150))
				''')
			cursor1.executemany('INSERT INTO SHEET VALUES ( NULL,?,?)', lista3)

			database.commit()
			database.close()
			database=sqlite3.connect('dictionary')
			cursor1=database.cursor()
			
			'''print('lista2',lista2)
			print('lista3',lista3)'''

			'''wordslist=[]
			meaninglist=[]
			numberlist=[]
			for fill in lista2:
				wordslist.append(fill[1])
				meaninglist.append(fill[2])
				numberlist.append(fill[0])'''


			
			listamuestra.reverse()

			texto=Listbox(frame1)
			scrolly=Scrollbar(frame1,command=texto.yview,width=18)
			scrolly.place(in_=texto, relx=1, relheight=1, bordermode="outside")
			texto.config(width=47,height=21)
			texto.place(x=270)
			

			
			

			for listamuestra in listamuestra:
				texto.insert(0,listamuestra)
			'''cursor1.fetchall()
			database.commit()
			database.close()'''



			



			
			
		function2()		



		introwordlabel=Label(frame1,text='Intro word you want to add:')	
		introwordlabel.place(x=10,y=10)
		introwordlabel.config(width=25,height=1,bg='red',font=('Comic Sans MS',11))

		introword=StringVar(frame1)
		introword1=Entry(frame1,textvariable=introword)
		introword1.config(width=30,font=('Comic Sans MS',10))
		introword1.place(x=10,y=50)

		intromeaninglabel=Label(frame1,text='Intro meaning:')	
		intromeaninglabel.place(x=10,y=85)
		intromeaninglabel.config(width=20,height=1,bg='red',font=('Comic Sans MS',11))

		intromeaning=StringVar(frame1)
		intromeaning1=Entry(frame1,textvariable=intromeaning)
		intromeaning1.config(width=30,font=('Comic Sans MS',10))
		intromeaning1.place(x=10,y=120)


		def addwordbutton():

			print('---------')
			addindictionary=[(introword.get(),intromeaning.get())]

			if introword.get()=='':
				messagebox.showwarning('Vocabulary App','Empty field!!!')

			elif intromeaning.get()=='':
				messagebox.showwarning('Vocabulary App','Empty field!!!')


			else:
				lista4=[]
				database=sqlite3.connect('dictionary')
				cursor1=database.cursor()
				
				for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
					lista4.append(x)
				#print('lista4',lista4)
				database.commit()
				database.close()
				con=0
				for compare in lista4:
					if introword.get()==compare[0] and intromeaning.get()==compare[1]:
						con+=1
						messagebox.showwarning('Vocabulary App','You are repiting the same word and meaning!!!')
						introword.set('')
						intromeaning.set('')
					
						
			if con==0:		
				database=sqlite3.connect('dictionary')
				cursor1=database.cursor()
				cursor1.executemany('INSERT INTO SHEET VALUES (  NULL,?,?)', addindictionary)
				database.commit()
				database.close()		
				introword.set('')
				intromeaning.set('')
				function2()		
			else:
				introword.set('')
				intromeaning.set('')	
					
						
		addword=Button(frame1,text='Add word',command=addwordbutton)
		addword.place(x=10,y=150)
		addword.config(width=10,height=1,bg='blue',font=('Comic Sans MS',9))
		def deletefields2():
			introword.set('')
			intromeaning.set('')
		 	
		delatefields=Button(frame1,text='Delete fields',command=deletefields2)
		delatefields.place(x=100,y=150)
		delatefields.config(width=15,height=1,bg='blue',font=('Comic Sans MS',9))	

		def deleteintro():
			print('deleteintro')
			lista5=[]

			
			try:
				if deleteword.get()!=0:
					database=sqlite3.connect('dictionary')
					cursor1=database.cursor()
					
					for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
						lista5.append(x)

					if len(lista5)<=10:
						messagebox.showwarning('Vocabulary App','I need at least fifteen words to work!!!')

					else:
						print('lista5',lista5)
						print('lista5delete',lista5[deleteword.get()-1])

							
						lista5.remove(lista5[deleteword.get()-1])
						print('lista5',lista5)
						cursor1.execute('DROP TABLE SHEET')
						cursor1.execute('''
							CREATE TABLE SHEET (
							ID INTEGER PRIMARY KEY AUTOINCREMENT,
							WORD VARCHAR(50) ,
							MEANING VARCHAR(150))
							''')
						

						cursor1.executemany('INSERT INTO SHEET VALUES (  NULL,?,?)', lista5)
					database.commit()
					database.close()
			except:
				pass
			 
			 	
			deleteword.set('')

			function2()


			
		deleteword=IntVar(frame1)
		deleteword1=Entry(frame1,textvariable=deleteword)
		deleteword1.config(width=6,font=('Comic Sans MS',10))
		deleteword1.place(x=130,y=235)
			
		deletewordbutton=Button(frame1,text='Delete Word Nº:',command=deleteintro)
		deletewordbutton.place(x=10,y=230)
		deletewordbutton.config(width=15,height=1,bg='blue',font=('Comic Sans MS',9))



		exitdictionary=Button(frame1,text='Exit',command=frame1.destroy)
		exitdictionary.place(x=100,y=300)
		exitdictionary.config(width=10,height=1,bg='green',font=('Comic Sans MS',9))	
			


			


			





		mainloop()
	functiondictionay()






