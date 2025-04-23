import tkinter as tk
from tkinter import messagebox
import controller.tarefa_controller as controller

class TarefaView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=5)

        tk.Button(master, text="Adicionar", command=self.adicionar).pack()
        tk.Button(master, text="Concluir", command=self.concluir).pack()
        tk.Button(master, text="Excluir", command=self.excluir).pack()

        self.lista = tk.Listbox(master, width=50)
        self.lista.pack(pady=10)

        self.atualizar_lista()

    def adicionar(self):
        desc = self.entry.get().strip()
        if desc:
            controller.adicionar_tarefa(desc)
            self.entry.delete(0, tk.END)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Digite a tarefa.")

    def concluir(self):
        index = self.lista.curselection()
        if index:
            tarefa = self.tarefas[index[0]]
            controller.marcar_concluida(tarefa.id)
            self.atualizar_lista()

    def excluir(self):
        index = self.lista.curselection()
        if index:
            tarefa = self.tarefas[index[0]]
            controller.excluir_tarefa(tarefa.id)
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        self.tarefas = controller.listar_tarefas()
        for tarefa in self.tarefas:
            self.lista.insert(tk.END, str(tarefa))
