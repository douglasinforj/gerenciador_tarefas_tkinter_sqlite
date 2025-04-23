import sqlite3

def conectar():
    return sqlite3.connect("tarefa.db")

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT NOT NULL,
                   concluida INTEGER DEFAUL 0 
                   )
    """)

    conn.commit()
    conn.close()    