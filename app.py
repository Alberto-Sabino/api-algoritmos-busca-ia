from http.client import HTTPException
import os
from algoritmos import comPeso, semPeso
from flask import Flask, request, json, abort, make_response
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
cp = comPeso.busca()
sp = semPeso.busca()

# ------------------------------------- ROTAS -------------------------------------

# --------------------------------- Busca sem peso --------------------------------

@app.post("/api/amplitude")
def buscaPorAmplitude():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho = sp.amplitude(grafo, nos, origem, destino)
    except:
        return erroInterno()

    return caminho


@app.post("/api/profundidade")
def buscaPorProfundidade():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        if request.args.get('limite', None) != None:
            caminho = sp.prof_limitada(grafo, nos, origem, destino, int(request.args.get('limite')))
        else:
            caminho = sp.profundidade(grafo, nos, origem, destino)
    except:
        return erroInterno()

    return caminho

@app.post("/api/aprofundamento-interativo")
def buscaPorAprofundamento():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        limite = request.get_json()['limite']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho = sp.aprof_iterativo(grafo, nos, origem, destino, limite)
    except:
        return erroInterno()
    
    return caminho


@app.post("/api/bidirecional")
def buscaBidirecional():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho = sp.bidirecional(grafo, nos, origem, destino)
    except:
        return erroInterno()

    return caminho


# -------------------------------- Busca com peso --------------------------------

@app.post("/api/custo-uniforme")
def buscaPorCustoUniforme():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho, custo = cp.custo_uniforme(grafo, nos, origem, destino)
        response = make_response(json.dumps({ 
                        "caminho": caminho,
                        "custo": custo
                    }), 200)
        response.content_type = "application/json"

        return response
    except:
        return erroInterno()


@app.post("/api/greedy")
def buscaPorGreedy():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho, custo = cp.greedy(grafo, nos, origem, destino)
        response = make_response(json.dumps({ 
                        "caminho": caminho,
                        "custo": custo
                    }), 200)
        response.content_type = "application/json"

        return response
    except:
        return erroInterno()

    return caminho


@app.post("/api/a-estrela")
def buscaPorAEstrela():
    try:
        grafo = request.get_json()['grafo']
        nos = request.get_json()['nos']
        origem = request.get_json()['origem']
        destino = request.get_json()['destino']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        caminho, custo = cp.a_estrela(grafo, nos, origem, destino)
        response = make_response(json.dumps({ 
                        "caminho": caminho,
                        "custo": custo
                    }), 200)
        response.content_type = "application/json"

        return response
    except:
        return erroInterno()

    return caminho


# ----------------------------- Tratamento de erros ------------------------------

@app.errorhandler(HTTPException)
def global_catch(e):
    response = e.get_response()
    response.data =  json.dumps({
        "codigo_erro": e.code,
        "nome": e.name,
        "descricao": e.description
    })
    response.content_type = "application/json"
    return response


def erroInterno():
    response = make_response()
    response.data = json.dumps({
        "codigo_erro": 500,
        "nome": "Erro interno no servidor",
        "descricao": "Ocorreu um erro ao buscar o melhor caminho."
    })
    response.content_type = "application/json"
    return response


# -------------------------------- Iniciando servidor --------------------------------

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', "False"))
    app.run(debug=debug, port=port, host='0.0.0.0' )