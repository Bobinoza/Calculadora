from tkinter import *  # importa todos os modulos do Tkinter


class Calculadora:
    def __init__(self, master): # Construtor __init__, que vai conter dois parametros, o self que é objeto e o master que é o pai da aplicação.
        self.frame = Frame(master)
        self.frame.grid()
        self.dados = Entry(master, width=34)
        self.dados.grid(row=1, column=0)
        bts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "C"]
        r = 1  # Vai controlar qual linha cada botao vai ficar
        c = 0  # vai definir a coluna em que cada botão vai ficar
        for bt in bts:
            comando = lambda x=bt: self.calcular(x)
            self.botao = Button(self.frame, text=bt, width=6, command=comando)
            self.botao.grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def calcular(self, valor):
        if valor == "=":
            tudo = "123456789.+-*/"
            if self.dados.get()[0] not in tudo:  #  Este if serve para ver se não contem dados invalidos, como por exemplo uma letra.
                self.dados.insert(END, "Operação inválida!")
            try:
                resultado = eval(self.dados.get())
                self.dados.insert(END, "="+str(resultado))
            except:
                self.dados.insert(END, "Error!")
        elif valor == "C":
            self.dados.delete(0, END)  # Se o usuário apertar no C, faz apagar tudom, da posição 0 até o final (0, END)
        else:
            if "=" in self.dados.get():
                self.dados.delete(0, END)
            self.dados.insert(END, valor)

root = Tk()
root.title("Calculadora")
Calculadora(root)
root.mainloop()