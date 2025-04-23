import tkinter as tk
from view.tarefa_view import TarefaView
from database.conexao import inicializar_banco

if __name__ == "__main__":
    inicializar_banco()

    root = tk.Tk()
    app = TarefaView(root)
    root.mainloop()