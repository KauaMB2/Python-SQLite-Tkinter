from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
import os
import banco
pastaApp = os.path.dirname(__file__) #Encontra a localização do arquivo no PC
def atualizarApp():
    app.update()
def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values = i)
def inserir():
    if vnome.get()=="" or vfone.get()=="" or vemail1.get()=="" or vemail2.get() == "":
        messagebox.showinfo(title = "ERRO", message = "Digite todos os dados")
        return
    try:
        vquery = "INSERT INTO tb_nomes(nome, fone, email1, email2)VALUES('" + vnome.get() + "','" + vfone.get() + "','" + vemail1.get() + "','" + vemail2.get() + "')"
        banco.dml(vquery)
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao inserir")
        return
    popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vemail1.delete(0, END)
    vemail2.delete(0, END)
    vnome.focus()
def deletar():
    try:
        vid = 1
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        vid = valores[0]
        vquery = "DELETE FROM tb_nomes WHERE id = " + vid
        banco.dml(vquery)
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title = "ERRO", message = "Escolha um item para ser deletado")
def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes WHERE nome LIKE '%" + vnomepesquisar.get() + "%'"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values = i)
    vnomepesquisar.delete(0, END)
def atualizar():
    exec(open(pastaApp+"\\atualizar.py").read())
app = Tk()
app.title("BancoDeDados1.0")
app.geometry("600x500")
quadroGrid = LabelFrame(app, text = "Contatos")
quadroGrid.pack(fill = "both", expand = "yes", padx = 10, pady = 10)
tv = ttk.Treeview(quadroGrid, columns = ('id', 'nome',"fone", "email1",'email2'), show = 'headings')
tv.column('id', minwidth = 0, width = 30)
tv.column('nome', minwidth = 0, width = 150)
tv.column('fone', minwidth = 0, width = 100)
tv.column('email1', minwidth = 0, width = 100)
tv.column('email2', minwidth = 0, width = 100)
tv.heading('id', text = 'ID')
tv.heading('nome', text = 'NOME')
tv.heading('email1', text = 'EMAIL1')
tv.heading('email2', text = 'EMAIL2')
tv.heading('fone', text = 'TELEFONE')
tv.pack()
popular()
quadroInserir = LabelFrame(app, text = "Inserir Novos Contatos")
quadroInserir.pack(fill = "both", expand = "yes", padx = 10, pady = 5)
lbnome = Label(quadroInserir, text = "Nome")
lbnome.pack(side = "left")
lbnome.place(x = 0, y = 0)
vnome = Entry(quadroInserir)
vnome.pack(side = "left", padx = 10)
vnome.place(x = 41, y = 0)
lbfone = Label(quadroInserir, text = "Fone")
lbfone.pack(side = "left")
vfone = Entry(quadroInserir)
vfone.pack(side = "left", padx = 10, pady = 10)
Email1 = Label(quadroInserir, text = "Email1")
Email1.pack(side = "left")
Email1.place(x = 175, y = 0)
vemail1 = Entry(quadroInserir)
vemail1.pack(side = "left", padx = 20, pady = 10)
vemail1.place(x = 236, y = 0)
Email2 = Label(quadroInserir, text = "Email2")
Email2.pack(side = "left")
vemail2 = Entry(quadroInserir)
vemail2.pack(side = "left", padx = 20, pady = 10)
btn_inserir = Button(quadroInserir, text = "Inserir", command = inserir)
btn_deletar = Button(quadroInserir, text  = "Deletar", command = deletar)
btn_deletar.place(x = 388, y = -5)
btn_inserir.pack(side = "left", padx = 10)
quadroPesquisar = LabelFrame(app, text = "Pesquisar Contatos")
quadroPesquisar.pack(fill = "both", expand = "yes", padx= 10, pady = 10)
lbid =Label(quadroPesquisar, text = "Nome")
lbid.pack(side = "left")
vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side = "left", padx = 10)
btn_pesquisar = Button(quadroPesquisar, text = "Pesquisar", command = pesquisar)
btn_pesquisar.pack(side = "left", padx = 10)
btn_todos = Button(quadroPesquisar, text = "Mostrar Todos", command = popular)
btn_todos.pack(side = "left", padx = 10)
app.mainloop()