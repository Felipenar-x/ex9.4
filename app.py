from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Flask", "concluida": False},
    {"id": 2, "titulo": "Fazer deploy na Azure", "concluida": True}
]

@app.route("/")
def home():
    return jsonify({"mensagem": "API RESTful Flask funcionando na Azure!"})

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.json
    nova_tarefa["id"] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            dados = request.json
            tarefa.update(dados)
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida com sucesso"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404  