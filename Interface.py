from tkinter import *
import wahadlo as wah
from PIL import Image, ImageTk
from tkinter import messagebox as mbox

root = Tk()
entry = "#dfe4d7"
background = "#b9d0c0"
button = "#dae7dd"
g = Entry(root, width=3, bg=entry, font=('Arial', 15))
l1 = Entry(root, width=3, bg=entry, font=('Arial', 15))
l2 = Entry(root, width=3, bg=entry, font=('Arial', 15))
m1 = Entry(root, width=3, bg=entry, font=('Arial', 15))
m2 = Entry(root, width=3, bg=entry, font=('Arial', 15))
th1 = Entry(root, width=3, bg=entry, font=('Arial', 15))
th2 = Entry(root, width=3, bg=entry, font=('Arial', 15))
t = Entry(root, width=3, bg=entry, font=('Arial', 15))


def start():
    global root, g, l1, l2, m1, m2, th1, th2, t
    if g.get() != '' and l1.get() != '' and l2.get() != '' and m1.get() != '' and m2.get() != '' and th1.get() != '' and th2.get() != '' and t.get() != '':
        gf = float(g.get())
        l1f = float(l1.get())
        l2f = float(l2.get())
        m1f = float(m1.get())
        m2f = float(m2.get())
        th1f = float(th1.get())
        th2f = float(th2.get())
        tf = float(t.get())
        root.quit()
        wah.go(gf, l1f, l2f, m1f, m2f, th1f, th2f, tf)
        main()
    else:
        mbox.showerror("Błąd",
                       "Wpisz wszystkie dane")


def about():
    top = Toplevel(root)
    top.geometry("790x343")
    top.title("About")
    top.resizable(0, 0)
    top.configure(bg=background)
    img = ImageTk.PhotoImage(Image.open("wahadlo.png"))
    panel = Label(top, image=img)
    panel.image = img
    panel.place(x=0, y=0)
    label = Label(top, text="Podwójne wahadło jest systemem, który ", bg=background, font=('Arial', 15))
    label.place(x=380)

    label = Label(top, text="ukazuje chaotyczne, praktycznie niemożliwe ", bg=background, font=('Arial', 15))
    label.place(x=380, y=30)


    label = Label(top, text="do przewidzenia ruchy. Jest powszechnie ", bg=background, font=('Arial', 15))
    label.place(x=380, y=60)


    label = Label(top, text="wykorzystywane w edukacji, badaniach oraz ", bg=background, font=('Arial', 15))
    label.place(x=380, y=90)


    label = Label(top, text="analizie zdarzeń chaotycznych. Przykładowo,", bg=background, font=('Arial', 15))
    label.place(x=380, y=120)

    label = Label(top, text="za pomocą podwójnego wahadła tworzy się ", bg=background, font=('Arial', 15))
    label.place(x=380, y=150)

    label = Label(top, text="mechanizmy zabezpieczające przed ", bg=background, font=('Arial', 15))
    label.place(x=380, y=180)

    label = Label(top, text="trzęsieniami ziemi.", bg=background, font=('Arial', 15))
    label.place(x=380, y=210)

def main():
    global root, g, l1, l2, m1, m2, th1, th2
    root.title('Double Pendulum')
    window_width = 410
    window_height = 360
    root.geometry('{}x{}'.format(window_width, window_height))
    position_right = int((root.winfo_screenwidth() / 2) - (window_width / 2))
    position_down = int((root.winfo_screenheight() / 2) - (window_height / 2))
    root.geometry("+{}+{}".format(position_right, position_down))
    root.resizable(0, 0)
    root.configure(bg=background)

    label = Label(root, text="g[m/s^2] (przyspieszenie grawitacyjne):", bg=background, font=('Arial', 15))
    label.place(x=10, y=2)
    g.place(x=360, y=3)

    label = Label(root, text="l1[m] (długość pierwszego wahadła):", bg=background, font=('Arial', 15))
    label.place(x=10, y=37)
    l1.place(x=360, y=38)

    label = Label(root, text="l2[m] (długość drugiego wahadła):", bg=background, font=('Arial', 15))
    label.place(x=10, y=72)
    l2.place(x=360, y=73)

    label = Label(root, text="m1[kg] (masa pierwszego wahadła):", bg=background, font=('Arial', 15))
    label.place(x=10, y=107)
    m1.place(x=360, y=108)

    label = Label(root, text="m2[kg] (masa drugiego wahadła):", bg=background, font=('Arial', 15))
    label.place(x=10, y=142)
    m2.place(x=360, y=143)

    label = Label(root, text="th1[°] (pierwszy kąt startowy):", bg=background, font=('Arial', 15))
    label.place(x=10, y=178)
    th1.place(x=360, y=179)

    label = Label(root, text="th2[°] (drugi kąt startowy):", bg=background, font=('Arial', 15))
    label.place(x=10, y=213)
    th2.place(x=360, y=214)

    label = Label(root, text="t[s] (czas symulacji):", bg=background, font=('Arial', 15))
    label.place(x=10, y=248)
    t.place(x=360, y=249)

    btn = Button(root, text="Start", command=start, bg=button, font=('Arial', 20), compound=LEFT, width=5)
    btn.place(x=80, y=296)

    btn = Button(root, text="O wahadle", command=about, bg=button, font=('Arial', 20), compound=LEFT, width=9)
    btn.place(x=180, y=296)
    root.mainloop()


main()
