import model.tarefa_model as model 

def adicionar_tarefa(descricao):
    model.criar(descricao)

def lista_tarefas():
    return model.listar()

def marcar_concluida(id):
    model.atualizar_concluida(id)

def excluir_tarefa(id):
    model.excluir(id)