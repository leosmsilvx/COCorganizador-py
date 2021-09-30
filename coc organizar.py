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

        canvas = tk.Canvas(win, height=1000, width=1000, bg="#4f4f4f")
        canvas.pack()
        
        lista = []
        num = int(ed.get())
        while(num > 0):
            addlista = ((num) % 100)
            num = int((num)//100)
            lista.append(addlista)

        lista.sort(key=int)
        numbers = Label(win, bg="#4f4f4f", fg="#eee",text="Organized numbers:\n{}".format(str(lista)[1:-1])) # To remove the brackets
        numbers.place(x=60,y=20)

        bto = Button(win, width=10, text="Ok", command=win.destroy, bg="#4f4f4f", fg="#eee")
        bto.place(x=334, y=90)

        win.mainloop()
        winm.destroy()
    
        
    try:
        winm = Tk()
        winm.iconphoto(True, tk.PhotoImage(file='icon.png'))
    except:
        winm.destroy()
        winm = Tk()

    winm.title("AutoPC")
    winm.geometry("425x150+100+100")

    canvas = tk.Canvas(winm, height=1000, width=1000, bg="#4f4f4f")
    canvas.pack()
    
    lb = Label(winm, text="Welcome to AutoPC\n\n\n\nType the numbers to organize", bg="#4f4f4f", fg="#eee")
    lb.place(x=130,y=40)

    ed = Entry(winm, bg="#707070", fg="#eee")
    ed.place(x=110,y=70)
    ed.focus_force()

    bto = Button(winm, width=6, text="Ok", command=organize, bg="#707070", fg="#eee")
    bto.place(x=240, y=67)

    winm.mainloop()

if __name__ == '__main__':
    main()

        
