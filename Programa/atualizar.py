from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import banco
def Id():
    Varcontrole = 1
    if entryId.get() == "":
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        Varcontrole = 0
        return Varcontrole
    try:
        Varcontrole = entryId.get()
        return Varcontrole
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        Varcontrole = 0
        return Varcontrole
    
def Nome():
    if entryNome.get()=="":
        messagebox.showinfo(title = "ERRO", message = "Digite nome para atualizar")
        return
    try:
        resId = Id()
        if resId == 0:
            return
        vquery = "UPDATE tb_nomes SET nome = " + "\'" + entryNome.get() + "\' WHERE id=" + resId
        banco.dml(vquery)
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        return
    entryNome.delete(0, END)
def Fone():
    if entryFone.get()=="":
        messagebox.showinfo(title = "ERRO", message = "Digite o telefone para atualizar")
        return
    try:
        resId = Id()
        if resId == 0:
            return
        vquery = "UPDATE tb_nomes SET fone=" + "\'" + entryFone.get() + "\' WHERE id=" + resId
        banco.dml(vquery)
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        return
    entryFone.delete(0, END)
def Email1():
    if entryEmail1.get()=="":
        messagebox.showinfo(title = "ERRO", message = "Digite o email1 para atualizar")
        return
    try:
        resId = Id()
        if resId == 0:
            return
        vquery = "UPDATE tb_nomes SET email1=" + "\'" + entryEmail1.get() + "\' WHERE id=" + resId
        banco.dml(vquery)
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        return
    entryEmail1.delete(0, END)
def Email2():
    if entryEmail2.get()=="":
        messagebox.showinfo(title = "ERRO", message = "Digite o email2 para atualizar")
        return
    try:
        resId = Id()
        if resId == 0:
            return
        vquery = "UPDATE tb_nomes SET email2 =" + "\'" + entryEmail2.get() + "\' WHERE id=" + resId
        banco.dml(vquery)
    except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao atualizar")
        return
    entryEmail2.delete(0, END)
app1 = Tk()
app1.title("Atualizar")
app1.geometry("240x270")
quadroAtualizar = LabelFrame(app1, text = "Atualizar")
quadroAtualizar.pack(fill = "both", expand = "yes", padx = 10, pady = 5)
entryNome = Entry(quadroAtualizar)
entryFone = Entry(quadroAtualizar)
entryEmail1 = Entry(quadroAtualizar)
entryEmail2 = Entry(quadroAtualizar)
entryId = Entry(quadroAtualizar)
Label(quadroAtualizar, text = "Digite o Id abaixo:", background = "#dde", foreground = "#009", anchor = W).place(x = 5, y = 180)
entryNome.place(x = 5,y = 5)
entryFone.place(x = 5,y = 50)
entryEmail1.place(x = 5,y = 105)
entryEmail2.place(x = 5,y = 155)
entryId.place(x = 5, y = 215)
btn_Nome = Button(quadroAtualizar, text = "Nome", command = Nome)
btn_Fone = Button(quadroAtualizar, text  = "Fone", command = Fone)
btn_Email1 = Button(quadroAtualizar, text = "Email1", command = Email1)
btn_Email2 = Button(quadroAtualizar, text = "Email2", command = Email2)
btn_Nome.place(x = 135, y = 0)
btn_Fone.place(x = 135, y = 50)
btn_Email1.place(x = 135, y = 100)
btn_Email2.place(x = 135, y = 150)
app1.mainloop()