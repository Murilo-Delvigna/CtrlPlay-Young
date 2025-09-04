
import tkinter 

# Criando a janela principal
janela = tkinter.Tk()
janela.title(" Janela")
janela.geometry("300x200")  # Largura x Altura

# Adicionando um rótulo
def clique():
    label.config(text="Parabens você ganhou!")

# Executando o loop principal
label = tkinter.Label(janela, text= "Ola usuario !", font=('Arial',14))
label.pack(pady=20)

botao = tkinter.Button(janela, text = 'Clique Aqui', command= clique)
botao.pack()
janela.mainloop()
