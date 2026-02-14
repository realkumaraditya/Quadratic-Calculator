from tkinter import *


def main() -> None:
    gui = Tk()
    gui.title("Quadratic Solver")
    gui.configure(bg="#000000")
    gui.geometry("500x300")

    def coefficient(x: float) -> float:
        if x.is_integer():
            return int(x)
        else:
            return x

    def answer() -> None:
        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())

        if a == 1:
            eq = "x\N{SUPERSCRIPT TWO} "
        elif a == -1:
            eq = "-x\N{SUPERSCRIPT TWO} "
        else:
            eq = f"{coefficient(a)}x\N{SUPERSCRIPT TWO} "
        if b == 1:
            eq += "+x "
        elif b == -1:
            eq += "-x "
        else:
            eq += f"{coefficient(b):+}x "

        eq += f"{coefficient(c):+} = 0"

        pans = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        nans = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        if pans.imag:
            pans = f"{pans.real:.2f} {pans.imag:+.2f}i"
        else:
            pans = f"{pans.real:.2f}"
        if nans.imag:
            nans = f"{nans.real:.2f} {nans.imag:+.2f}i"
        else:
            nans = f"{nans.real:.2f}"
        equation.set(eq)
        ansp.set(pans)
        ansn.set(nans)

    ansp = DoubleVar()
    ansn = DoubleVar()
    equation = StringVar()
    l1 = Label(
        gui,
        text="Enter the coefficient of x\N{SUPERSCRIPT TWO}: ",
        bg="#000000",
        fg="#FFFFFF",
    )
    l1.place(x=10, y=10)
    e1 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF")
    e1.place(x=250, y=10)

    l2 = Label(gui, text="Enter the coefficient of x: ", bg="#000000", fg="#FFFFFF")
    l2.place(x=10, y=50)
    e2 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF")
    e2.place(x=250, y=50)

    l3 = Label(gui, text="Enter the constant: ", bg="#000000", fg="#FFFFFF")
    l3.place(x=10, y=90)
    e3 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF")
    e3.place(x=250, y=90)

    l4 = Label(gui, text="First solution: ", bg="#000000", fg="#FFFFFF")
    l4.place(x=10, y=130)
    e4 = Label(gui, bd=2, textvariable=ansp, bg="#000000", fg="#FFFFFF")
    e4.place(x=250, y=130)

    l5 = Label(gui, text="Second solution: ", bg="#000000", fg="#FFFFFF")
    l5.place(x=10, y=170)
    e5 = Label(gui, bd=2, textvariable=ansn, bg="#000000", fg="#FFFFFF")
    e5.place(x=250, y=170)

    l6 = Label(gui, text="Equation:", bg="#000000", fg="#FFFFFF")
    l6.place(x=10, y=210)
    e6 = Label(gui, textvariable=equation, bg="#000000", fg="#FFFFFF")
    e6.place(x=250, y=210)

    button = Button(gui, text="Solve", command=answer, bg="#000000", fg="#FFFFFF")
    button.place(x=250, y=250)
    gui.mainloop()


if __name__ == "__main__":
    main()
