# Gerenciador de Tarefas  - Tkinter + SQLite

## Funcionalidades

- [x] **Adicionar Tarefa**
- [x] **Atribuir Categoria**
- [x] **Marcar como Concluída / Não Concluída**
- [x] **Excluir Tarefa**
- [x] **Filtro (Todas, Concluídas, Pendentes)**
- [x] **Exportar lista de tarefas para `.csv`**
- [x] **Persistência de dados com SQLite**
- [x] **Interface gráfica simples com Tkinter**

## Estrutura do Projeto
```
gerenciador_tarefas/
│
├── main.py                      # Ponto de entrada da aplicação
│
├── controller/
│   └── tarefa_controller.py     # Controla a lógica entre UI e banco
│
├── model/
│   └── tarefa_model.py          # Classe Tarefa e lógica de banco SQLite
│
├── view/
│   └── tarefa_view.py           # Interface gráfica (Tkinter)
│
└── database/
    └── conexao.py               # Gerencia conexão com banco de dados


```


## Tecnologias Utilizadas

- Python 3.x
- Tkinter (GUI nativa)
- SQLite (banco de dados local)
- CSV (exportação)
- POO (classes e separação em camadas)
- PyInstaller (para gerar `.exe`)