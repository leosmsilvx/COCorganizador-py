from tkinter import *
import tkinter as tk
#This program was made for "https://centrooestecap.com.br/resultados-cc/" to just ctrl+c and ctrl+v
#And show to me the numbers organized
#It was so simple so I made it using tkinter
def main():
    
    def organize():
        win = Tk()
        
        win.title("AutoPC")
        win.geometry("765x150+100+100")
        
        lista = []
        num = int(ed.get())
        while(num > 0):
            addlista = ((num) % 100)
            num = int((num)//100)
            lista.append(addlista)

        lista.sort(key=int)
        numbers = Label(win, text="Organized numbers:\n{}".format(str(lista)[1:-1])) # To remove the brackets
        numbers.place(x=60,y=20)

        bto = Button(win, width=10, text="Ok", command=win.destroy)
        bto.place(x=334, y=90)

        win.mainloop()
        winm.destroy()
    
            
    winm = Tk()

    winm.title("AutoPC")
    winm.geometry("425x150+100+100")
    winm.iconphoto(True, tk.PhotoImage(file='icon.png'))


    lb = Label(winm, text="Welcome to AutoPC\n\n\n\nType the numbers to organize")
    lb.place(x=130,y=40)

    ed = Entry(winm)
    ed.place(x=110,y=70)
    ed.focus_force()

    bto = Button(winm, width=6, text="Ok", command=organize)
    bto.place(x=240, y=67)

    winm.mainloop()

if __name__ == '__main__':
    main()

        
