from database.conexao import conectar

class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

        def __str__(self):
            status = "Concluída" if self.concluida else "Pendente"
            return f"{self.id} - {self.descricao} [{status}]"
        
def criar(descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, decricao, concluida FROM tarefas")
    tarefas = [Tarefa(*row) for row in cursor.fetchall()] 
    conn.close()
    return tarefas

    """
    Explicação:
    Cursor esta percorrendo as linhas do banco com for, o (*) é operador de desenpacotamento em python, se row for uma tupla ele vai tranformar nisso (1, "Estudar python", "Estudo", 0 )
    Tarefa(*row) - Esta criando uma nova instancias da classe, passando os valores como argumentos para o construtor da classe Tarefa
    """  

def atualizar_concluida(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close() 

def excluir(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE from tarefas WHERE id = ?", (id))  
                                                                  


