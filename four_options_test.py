import sqlite3
from random import randint,shuffle
from tkinter import *
from PIL import ImageTk,Image
from random import randint,shuffle
from time import sleep
from tkinter import messagebox
from time import sleep,time
import simpleaudio as sa

'''root=Tk()
root.title('Vocabulary DiegApp')
root.config(bg='red',bd=35,relief='ridge')
root.geometry('645x410')
root.resizable(False,False)
root.iconbitmap('eng.ico')'''
backcount=4
bolstart=0
exit=0
refresh1=6
lista2=[]
word=[]
option2=[]
option3=[]
option4=[]
score=0
buttons=[]
sound3=1
database=sqlite3.connect('dictionary')
cursor1=database.cursor()
for x in cursor1.execute('SELECT WORD,MEANING FROM SHEET ORDER BY WORD '):
	lista2.append(x)
cursor1.close()
	
def stop():
	frame3=Frame()
	frame3.place(x=0,y=0)
	def correct():
		def clear():
				
			label1.destroy()
			label2.destroy()
			easy.destroy()
			medium.destroy()
			hard.destroy()
			write.destroy()
			frame3.destroy()
			stop()			
		if word[1]==buttons[0]:
			
			
			easy=Button(frame3,text=buttons[0], state=DISABLED)
			easy.config(width=28,height=1)
			easy.config(bg='green',bd=10,relief='ridge')
			easy.config(font=('Comic Sans MS',11))
			easy.place(x=290,y=30)
			medium=Button(frame3,text=buttons[1], state=DISABLED)
			medium.config(width=28,height=1)
			medium.config(bg='red',bd=10,relief='ridge')
			medium.config(font=('Comic Sans MS',11))
			medium.place(x=290,y=90)
			hard=Button(frame3,text=buttons[2], state=DISABLED)
			hard.config(width=28,height=1)
			hard.config(bg='red',bd=10,relief='ridge')
			hard.config(font=('Comic Sans MS',11))
			hard.place(x=290,y=150)
			write=Button(frame3,text=buttons[3], state=DISABLED)
			write.config(width=28,height=1)
			write.config(bg='red',bd=10,relief='ridge')
			write.config(font=('Comic Sans MS',11))
			write.place(x=290,y=210)
		elif word[1]==buttons[1]:
			
			easy=Button(frame3,text=buttons[0], state=DISABLED)
			easy.config(width=28,height=1)
			easy.config(bg='red',bd=10,relief='ridge')
			easy.config(font=('Comic Sans MS',11))
			easy.place(x=290,y=30)
			medium=Button(frame3,text=buttons[1], state=DISABLED)
			medium.config(width=28,height=1)
			medium.config(bg='green',bd=10,relief='ridge')
			medium.config(font=('Comic Sans MS',11))
			medium.place(x=290,y=90)
			hard=Button(frame3,text=buttons[2], state=DISABLED)
			hard.config(width=28,height=1)
			hard.config(bg='red',bd=10,relief='ridge')
			hard.config(font=('Comic Sans MS',11))
			hard.place(x=290,y=150)
			write=Button(frame3,text=buttons[3], state=DISABLED)
			write.config(width=28,height=1)
			write.config(bg='red',bd=10,relief='ridge')
			write.config(font=('Comic Sans MS',11))
			write.place(x=290,y=210)
		elif word[1]==buttons[2]:
			
			easy=Button(frame3,text=buttons[0], state=DISABLED)
			easy.config(width=28,height=1)
			easy.config(bg='red',bd=10,relief='ridge')
			easy.config(font=('Comic Sans MS',11))
			easy.place(x=290,y=30)
			medium=Button(frame3,text=buttons[1], state=DISABLED)
			medium.config(width=28,height=1)
			medium.config(bg='red',bd=10,relief='ridge')
			medium.config(font=('Comic Sans MS',11))
			medium.place(x=290,y=90)
			hard=Button(frame3,text=buttons[2], state=DISABLED)
			hard.config(width=28,height=1)
			hard.config(bg='green',bd=10,relief='ridge')
			hard.config(font=('Comic Sans MS',11))
			hard.place(x=290,y=150)
			write=Button(frame3,text=buttons[3], state=DISABLED)
			write.config(width=28,height=1)
			write.config(bg='red',bd=10,relief='ridge')
			write.config(font=('Comic Sans MS',11))
			write.place(x=290,y=210)
		else:
			
			easy=Button(frame3,text=buttons[0], state=DISABLED)
			easy.config(width=28,height=1)
			easy.config(bg='red',bd=10,relief='ridge')
			easy.config(font=('Comic Sans MS',11))
			easy.place(x=290,y=30)
			medium=Button(frame3,text=buttons[1], state=DISABLED)
			medium.config(width=28,height=1)
			medium.config(bg='red',bd=10,relief='ridge')
			medium.config(font=('Comic Sans MS',11))
			medium.place(x=290,y=90)
			hard=Button(frame3,text=buttons[2])
			hard.config(width=28,height=1, state=DISABLED)
			hard.config(bg='red',bd=10,relief='ridge')
			hard.config(font=('Comic Sans MS',11))
			hard.place(x=290,y=150)
			write=Button(frame3,text=buttons[3])
			write.config(width=28,height=1, state=DISABLED)
			write.config(bg='green',bd=10,relief='ridge')
			write.config(font=('Comic Sans MS',11))
			write.place(x=290,y=210)
		frame3.after(1200,clear)







	




	def a():
		global word
		global option2
		global option3
		global option4
		global buttons
		global lista2
		

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

		

	a()	
	
	


	lienzo=Canvas(frame3,width=571,height=336)
	imagen=ImageTk.PhotoImage(Image.open('bandera.jpg'))
	lienzo.create_image(0,0,anchor=NW,image=imagen)
	lienzo.pack()

	label1=Label(frame3,text='What does it mean?')
	label1.config(width=20,height=1)
	label1.config(bg='red')
	label1.config(font=('Comic Sans MS',15))
	label1.place(x=30,y=70)

	label2=Label(frame3,text=word[0])
	label2.config(width=15,height=1)
	label2.config(bg='green')
	label2.config(font=('Comic Sans MS',20))
	label2.place(x=30,y=130)
	def correct1():
		if   word[1]==buttons[0]:
			wave_obj = sa.WaveObject.from_wave_file("right.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
		else:
			wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
		correct()

	def correct2():
		answer=2
		if  word[1]==buttons[1]:
			wave_obj = sa.WaveObject.from_wave_file("right.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()
		else:
			wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()	

	def correct3():
		
		if  word[1]==buttons[2]:
			wave_obj = sa.WaveObject.from_wave_file("right.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()
		else:
			wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()
	def correct4():
		
		if  word[1]==buttons[3]:
			wave_obj = sa.WaveObject.from_wave_file("right.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()
		else:
			wave_obj = sa.WaveObject.from_wave_file("wrong.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			correct()
	easy=Button(frame3,text=buttons[0],command=correct1)
	easy.config(width=28,height=1)
	easy.config(bg='blue',bd=10,relief='ridge')
	easy.config(font=('Comic Sans MS',11))
	easy.place(x=290,y=30)
	medium=Button(frame3,text=buttons[1],command=correct2)
	medium.config(width=28,height=1)
	medium.config(bg='blue',bd=10,relief='ridge')
	medium.config(font=('Comic Sans MS',11))
	medium.place(x=290,y=90)
	hard=Button(frame3,text=buttons[2],command=correct3)
	hard.config(width=28,height=1)
	hard.config(bg='blue',bd=10,relief='ridge')
	hard.config(font=('Comic Sans MS',11))
	hard.place(x=290,y=150)
	write=Button(frame3,text=buttons[3],command=correct4)
	write.config(width=28,height=1)
	write.config(bg='blue',bd=10,relief='ridge')
	write.config(font=('Comic Sans MS',11))
	write.place(x=290,y=210)
	def exit1():
		frame3.destroy()
	exitbuttom=Button(frame3,text='Exit',command=exit1)
	exitbuttom.config(width=7,height=1,bg='grey',bd=5,relief='ridge',font=('Comic Sans MS',10))
	exitbuttom.place(x=30,y=290)

	frame3.mainloop()


		

		
	
		

			


		
		
				
				
			

			

			







	

	







			

	


			
		
		
		

			
		
			



	
	





