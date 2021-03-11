import sqlite3
from tkinter import *
from PIL import ImageTk,Image
import diccionario
import three_options_test
import prueba_audio
import four_options_test
from tkinter import *
from PIL import ImageTk,Image
from random import randint,shuffle
from time import sleep
from tkinter import messagebox
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import simpleaudio as sa

root=Tk()
root.title('Vocabulary DiegApp')
root.config(bg='red',bd=35,relief='ridge')
root.geometry('645x410')
root.resizable(False,False)
root.iconbitmap('eng.ico')

backcount=4
bolstart=0
con=0
refresh1=6
lista2=[]
word=[]
option2=[]
option3=[]
option4=[]
score=0
buttons=[]
questions=0
database=sqlite3.connect('dictionary')
cursor1=database.cursor()
for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
	lista2.append(x)
cursor1.close()
def reset():
	global backcount
	backcount=4
	global bolstart
	bolstart=0
	global con
	con=0
	global refresh1
	refresh1=6
	global lista2
	lista2=[]
	global word
	word=[]
	global option2
	option2=[]
	global option3
	option3=[]
	global option4
	option4=[]
	global score
	score=0
	global buttons
	buttons=[]
	global questions
	questions=0
	global database
	database=sqlite3.connect('dictionary')
	global cursor1
	cursor1=database.cursor()
	for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
		lista2.append(x)
	cursor1.close()
	stop()
def stop():
	global root
	global bolstart
	global questions
	frame3=Frame()
	frame3.place(x=0,y=0)
	lienzo1=Canvas(frame3,width=571,height=336)
	imagen1=ImageTk.PhotoImage(Image.open('bandera.jpg'))
	lienzo1.create_image(0,0,anchor=NW,image=imagen1)
	lienzo1.pack()

	

	
	
	if questions<30:

		def start():
			global bolstart
			global root
			if bolstart==0:

				
				framestart1=Frame()
				framestart1.place(x=0,y=0)
				lienzo1=Canvas(framestart1,width=571,height=336)
				imagen1=ImageTk.PhotoImage(Image.open('bandera.jpg'))
				lienzo1.create_image(0,0,anchor=NW,image=imagen1)
				lienzo1.pack()				
				backcount2=Label(framestart1,text='Are you ready?')
				backcount2.config(width=15,height=1,bg='red',font=('Comic Sans MS',25))
				backcount2.place(x=120,y=150)
				
				
				bolstart+=1
				framestart1.after(3000,start)
			
				print('destroy')

				mainloop()
				


				
			
				
			elif bolstart==1:


				framestart2=Frame()
				framestart2.place(x=0,y=0)
				lienzo1=Canvas(framestart2,width=571,height=336)
				imagen1=ImageTk.PhotoImage(Image.open('bandera.jpg'))
				lienzo1.create_image(0,0,anchor=NW,image=imagen1)
				lienzo1.pack()
				backcount3=Label(framestart2,text='Let´s beginning!!!')
				backcount3.config(width=15,height=1,bg='red',font=('Comic Sans MS',25))
				backcount3.place(x=120,y=150)
				bolstart=2

				backcount3.after(3000,stop)
				mainloop()
		start()	
		print('post')
		def function1():
			global label3
			global refresh1
			global score

			mainframe.destroy()
			refresh1=6
			if buttons[0]==word[1]:
				wave_obj = sa.WaveObject.from_wave_file("right.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				score+=1
				print(score)
				stop()
			else:
				wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				stop()
		def function2():
			global label3
			global refresh1
			global score

			mainframe.destroy()
			refresh1=6
			if buttons[1]==word[1]:
				wave_obj = sa.WaveObject.from_wave_file("right.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				score+=1
				print(score)
				stop()
			else:
				wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				stop()
		def function3():
			global label3
			global refresh1
			global score

			mainframe.destroy()
			refresh1=6
			if buttons[2]==word[1]:
				wave_obj = sa.WaveObject.from_wave_file("right.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				score+=1
				print(score)
				stop()
			else:
				wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				stop()
		def function4():
			global label3
			global refresh1
			global score

			mainframe.destroy()
			refresh1=6
			if buttons[3]==word[1]:
				wave_obj = sa.WaveObject.from_wave_file("right.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				score+=1
				print(score)
				stop()
			else:
				wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				stop()



		

		def a():

			global word
			global option2
			global option3
			global option4
			global buttons
			global lista2
			global questions
			questions+=1

			shuffle(lista2)
			word=lista2[0]
			option2=lista2[1]
			option3=lista2[2]
			option4=lista2[3]
			print(word[1],option2[1],option3[1],option4[1])
			label=word[0]
			lista2.pop(0)
			buttons=[word[1],option2[1],option3[1],option4[1]]
			shuffle(buttons)

			
			print('buttons',word,buttons[0],buttons[1],buttons[2],buttons[3])

		def refresh3():
			global refresh1
			
			if refresh1!=0:
				refresh1-=1
				label3=Label(mainframe,text=refresh1)
				label3.config(width=5,height=1,bg='red',font=('Comic Sans MS',25))
				label3.place(x=110,y=190)
				print('refresh3')
					
				mainframe.after(1000,refresh3)
				mainloop()
			else:
				refresh1-=1
			
				label3=Label(mainframe,text=refresh1)
				label3.config(width=5,height=1,bg='red',font=('Comic Sans MS',25))
				label3.place(x=110,y=190)
				wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
				play_obj = wave_obj.play()
				play_obj.wait_done()
				refresh1=6
			
				stop()
				mainloop()
				
			

		a()	
		
		
		
		mainframe=Frame(root)
		mainframe.place(x=0,y=0)
		lienzo=Canvas(mainframe,width=571,height=336)
		imagen=ImageTk.PhotoImage(Image.open('bandera.jpg'))
		lienzo.create_image(0,0,anchor=NW,image=imagen)
		lienzo.pack()
		

		label1=Label(mainframe,text='What does it mean?')
		label1.config(width=20,height=1)
		label1.config(bg='red')
		label1.config(font=('Comic Sans MS',15))
		label1.place(x=30,y=70)

		label2=Label(mainframe,text=word[0])
		label2.config(width=15,height=1)
		label2.config(bg='green')
		label2.config(font=('Comic Sans MS',20))
		label2.place(x=30,y=130)
		easy=Button(mainframe,text=buttons[0],command=function1)
		easy.config(width=28,height=1)
		easy.config(bg='blue',bd=10,relief='ridge')
		easy.config(font=('Comic Sans MS',11))
		easy.place(x=290,y=30)
		medium=Button(mainframe,text=buttons[1],command=function2)
		medium.config(width=28,height=1)
		medium.config(bg='blue',bd=10,relief='ridge')
		medium.config(font=('Comic Sans MS',11))
		medium.place(x=290,y=90)
		hard=Button(mainframe,text=buttons[2],command=function3)
		hard.config(width=28,height=1)
		hard.config(bg='blue',bd=10,relief='ridge')
		hard.config(font=('Comic Sans MS',11))
		hard.place(x=290,y=150)
		write=Button(mainframe,text=buttons[3])
		write.config(width=28,height=1,command=function4)
		write.config(bg='blue',bd=10,relief='ridge')
		write.config(font=('Comic Sans MS',11))
		write.place(x=290,y=210)
		def exit4():


			mainframe.destroy()
			main1()
			print('exit4')
		
		exitbuttom=Button(mainframe,text='Exit',command=exit4)
		exitbuttom.config(width=7,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
		exitbuttom.place(x=30,y=290)
		def restartbutton():


			mainframe.destroy()
			reset()


			

		restartbutton1=Button(mainframe,text='Restart',command=restartbutton)
		restartbutton1.config(width=7,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
		restartbutton1.place(x=120,y=290)
		if con==0:
			print('con')
			refresh3()
		mainloop()

	else:
		print('else')
		score4=score,'/30'
		score2=[]
		score1=[]
		score1.append(score)
		try:
			database=sqlite3.connect('scoredata')
			cursor1=database.cursor()

			cursor1.execute('''
				CREATE TABLE SCORE (
				score INTEGER )
				''')


			database.commit()
			database.close()
		except:
			pass
		database=sqlite3.connect('scoredata')
		cursor1=database.cursor()

		cursor1.execute('INSERT INTO SCORE VALUES (?)',score1)

		for x in cursor1.execute('SELECT * FROM SCORE  '):
			score2.append(x)
		database.commit()	
		database.close()
		if len(score2)>15:
			score3=score2[len(score2)-15:len(score2)]
		else:
			score3=score2[:]
		def restartbutton():
			reset()
		frame7=Frame()
		frame7.place(x=0,y=0)

		lienzo=Canvas(frame7,width=571,height=336)
		imagen=ImageTk.PhotoImage(Image.open('bandera.jpg'))
		lienzo.create_image(0,0,anchor=NW,image=imagen)
		lienzo.pack()
		def chart():
			print('score3',score3)
			frame8=Frame()
			frame8.place(x=260,y=20)
			df1=DataFrame(score3)
			grafico=plt.Figure(figsize=(6,5),dpi=50)
			barras=grafico.add_subplot(111)
			bar1=FigureCanvasTkAgg(grafico,frame8)
			bar1.get_tk_widget().pack(side=LEFT,fill=BOTH)
			df1.plot(kind='bar',legend=True,ax=barras)
			barras.set_title('Your progress')
			bar1.draw()
		chart() 
		def deletechart1():
			score3=[0]
			frame8=Frame()
			frame8.place(x=260,y=20)
			df1=DataFrame(score3)
			grafico=plt.Figure(figsize=(6,5),dpi=50)
			barras=grafico.add_subplot(111)
			bar1=FigureCanvasTkAgg(grafico,frame8)
			bar1.get_tk_widget().pack(side=LEFT,fill=BOTH)
			df1.plot(kind='bar',legend=True,ax=barras)
			barras.set_title('Your progress')
			bar1.draw()
			database=sqlite3.connect('scoredata')
			cursor1=database.cursor()
			cursor1.execute('DROP TABLE SCORE')
			cursor1.execute('''
				CREATE TABLE SCORE (
				score INTEGER )
				''')
			database.close()
		backcount2=Label(frame7,text='Your score is:')
		backcount2.config(width=12,height=1,bg='red',font=('Comic Sans MS',20))
		backcount2.place(x=10,y=90)
		backcount2=Label(frame7,text=score4)
		backcount2.config(width=8,height=1,bg='red',font=('Comic Sans MS',20))
		backcount2.place(x=30,y=150)
		def exit1():

			frame7.destroy()
			#frame8.destroy()
			main1()
		exitbuttom=Button(frame7,text='Exit',command=exit1)
		exitbuttom.config(width=7,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
		exitbuttom.place(x=30,y=290)

		restartbutton1=Button(frame7,text='Restart',command=restartbutton)
		restartbutton1.config(width=7,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
		restartbutton1.place(x=120,y=290)

		deletechart=Button(frame7,text='Delete chart',command=deletechart1)
		deletechart.config(width=15,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
		deletechart.place(x=350,y=290)
	mainloop()       
def main1():
	global root
	frame1=Frame()
	frame1.place(x=0,y=0)
	lienzo=Canvas(frame1,width=571,height=336)
	imagen=ImageTk.PhotoImage(Image.open('bandera.jpg'))
	lienzo.create_image(0,0,anchor=NW,image=imagen)
	lienzo.pack()	
	label11=Label(frame1,text='What do you want to do?')
	label11.config(width=20,height=1)
	label11.config(bg='red')
	label11.config(font=('Comic Sans MS',15))
	label11.place(x=30,y=130)
	easy1=Button(frame1,text='Three Options',command=three_options_test.stop)
	easy1.config(width=28,height=1)
	easy1.config(bg='DarkGoldenrod3',bd=10,relief='ridge')
	easy1.config(font=('Comic Sans MS',11))
	easy1.place(x=290,y=30)
	medium1=Button(frame1,text='Four Options',command=four_options_test.stop)
	medium1.config(width=28,height=1)
	medium1.config(bg='DarkGoldenrod3',bd=10,relief='ridge')
	medium1.config(font=('Comic Sans MS',11))
	medium1.place(x=290,y=100)

	test=Button(frame1,text='Test',command=reset)
	test.config(width=28,height=1)
	test.config(bg='DarkGoldenrod3',bd=10,relief='ridge')
	test.config(font=('Comic Sans MS',11))
	test.place(x=290,y=170)
	write1=Button(frame1,text='Dictionary',command=diccionario.dictionarystart)
	write1.config(width=28,height=1)
	write1.config(bg='DarkGoldenrod3',bd=10,relief='ridge')
	write1.config(font=('Comic Sans MS',11))
	write1.place(x=290,y=240)
	'''write1=Button(frame1,text='About')
	write1.config(width=18,height=1)
	write1.config(bg='DeepSkyBlue2',bd=10,relief='ridge')
	write1.config(font=('Comic Sans MS',11))
	write1.place(x=330,y=270)'''
	mainloop()		
main1()
	
	
	

	
	
	
			
				
					
		
					
	
	 	
	
	

		
		

						
					
					

			
		 
		 	
		

		


		
	

	

		
		
			
	







	
		
		
		

		
		

		
	




	

		
		
		


		



		
		
	


	


		



	


	
