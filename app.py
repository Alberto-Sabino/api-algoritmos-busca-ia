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
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho = sp.amplitude(grafo, origem, destino)
        retorno = []

        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            return retorno
        else:
            return caminho
    except:
        return erroInterno()


@app.post("/api/profundidade")
def buscaPorProfundidade():
    try:
        grafo = request.get_json()['grafo']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        if request.args.get('limite', None) != None:
            caminho = sp.prof_limitada(grafo, origem, destino, int(request.args.get('limite')))
        else:
            caminho = sp.profundidade(grafo, origem, destino)

        retorno = []

        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            return retorno
        else:
            return caminho
    except:
        return erroInterno()


@app.post("/api/aprofundamento-interativo")
def buscaPorAprofundamento():
    try:
        grafo = request.get_json()['grafo']
        limite = request.get_json()['limite']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho = sp.aprof_iterativo(grafo, origem, destino, limite)
        retorno = []

        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            return retorno
        else:
            return caminho
    except:
        return erroInterno()


@app.post("/api/bidirecional")
def buscaBidirecional():
    try:
        grafo = request.get_json()['grafo']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho = sp.bidirecional(grafo, origem, destino)
        retorno = []

        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            return retorno
        else:
            return caminho
    except:
        return erroInterno()

# -------------------------------- Busca com peso --------------------------------

@app.post("/api/custo-uniforme")
def buscaPorCustoUniforme():
    try:
        grafo = request.get_json()['grafo']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho, custo = cp.custo_uniforme(grafo, origem, destino)

        retorno = []
        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            response = make_response(json.dumps({
                            "caminho": retorno,
                            "custo": custo
                        }), 200)
            response.content_type = "application/json"

            return response
        else:
            return caminho
    except:
        return erroInterno()


@app.post("/api/greedy")
def buscaPorGreedy():
    try:
        grafo = request.get_json()['grafo']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho, custo = cp.greedy(grafo, origem, destino)

        retorno = []
        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            response = make_response(json.dumps({
                            "caminho": retorno,
                            "custo": custo
                        }), 200)
            response.content_type = "application/json"

            return response
        else:
            return caminho
    except:
        return erroInterno()


@app.post("/api/a-estrela")
def buscaPorAEstrela():
    try:
        grafo = request.get_json()['grafo']
    except:
        abort(400, 'As informações passadas no body da request estão incompletas.')

    try:
        origem, destino = identificarViagem(grafo)
        caminho, custo = cp.a_estrela(grafo, origem, destino)
        retorno = []
        if caminho != 'caminho não encontrado':
            for ponto in caminho:
                retorno.append(grafo[ponto[0]][ponto[1]])

            response = make_response(json.dumps({
                            "caminho": retorno,
                            "custo": custo
                        }), 200)
            response.content_type = "application/json"

            return response
        else:
            return caminho
    except:
        return erroInterno()


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

def identificarViagem(grafo):
    x = 0
    y = 0
    origem = []
    destino = []

    for linha in grafo:
        x+=1
        for objeto in linha:
            y+=1
            if 'origem' in objeto:
                origem = [x-1, y-1]
            elif 'destino' in objeto:
                destino = [x-1, y-1]
        y = 0
    return origem, destino

# -------------------------------- Iniciando servidor --------------------------------

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', "False"))
    app.run(debug=debug, port=port, host='0.0.0.0' )
