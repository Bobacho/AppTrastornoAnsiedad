from flask import Blueprint, request, jsonify
from model.resultadoTest import tbResultadoTest
from utils.db import db

# Definición de blueprint
ResultadoTests = Blueprint('ResultadoTests', __name__)

@ResultadoTests.route('/ResultadoTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@ResultadoTests.route('/ResultadoTests/v1/listar', methods=['GET'])
def getResultadoTest():
    result = {}
    ResultadoTes = tbResultadoTest.query.all()
    result["data"] = ResultadoTes
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los resultados de los tests sin inconvenientes"
    return jsonify(result), 200

@ResultadoTests.route('/ResultadoTests/v1/insert', methods=['POST'])
def insertResultadoTest():
    result = {}
    body = request.get_json()
    idPaciente = body.get('idPaciente')
    puntajeResultadoTest = body.get('puntajeResultadoTest')
    infoResultado = body.get('infoResultado')
    fechaResultadoTest = body.get('fechaResultadoTest')
    revisadoResultadoTest = body.get('revisadoResultadoTest')

    if not idPaciente or not infoResultado or not fechaResultadoTest or puntajeResultadoTest is None:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    resultadotest = tbResultadoTest(idPaciente, puntajeResultadoTest, infoResultado, fechaResultadoTest, revisadoResultadoTest)
    db.session.add(resultadotest)
    db.session.commit()
    result["data"] = resultadotest
    result["status_code"] = 201
    result["msg"] = "Se agregó el resultado del test"
    return jsonify(result), 201

@ResultadoTests.route('/ResultadoTests/v1/update', methods=['POST'])
def updateResultadoTests():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    idPaciente = body.get('idPaciente')
    puntajeResultadoTest = body.get('puntajeResultadoTest')
    infoResultado = body.get('infoResultado')
    fechaResultadoTest = body.get('fechaResultadoTest')
    revisadoResultadoTest = body.get('revisadoResultadoTest')

    if not idResultadoTest or not idPaciente or not infoResultado or not fechaResultadoTest or puntajeResultadoTest is None:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    resultadosTest = tbResultadoTest.query.get(idResultadoTest)
    if not resultadosTest:
        result['status_code'] = 400
        result["msg"] = "El resultado del test no existe"
        return jsonify(result), 400

    resultadosTest.idPaciente = idPaciente
    resultadosTest.puntajeResultadoTest = puntajeResultadoTest
    resultadosTest.infoResultado = infoResultado
    resultadosTest.fechaResultadoTest = fechaResultadoTest
    resultadosTest.revisadoResultadoTest = revisadoResultadoTest
    db.session.commit()

    result["data"] = resultadosTest
    result["status_code"] = 202
    result["msg"] = "Se modificó el resultado del test"
    return jsonify(result), 202

@ResultadoTests.route('/ResultadoTests/v1/delete', methods=['DELETE'])
def deleteResultadoTests():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    if not idResultadoTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400

    resultadosTest = tbResultadoTest.query.get(idResultadoTest)
    if not resultadosTest:
        result["status_code"] = 400
        result["msg"] = "El resultado no existe"
        return jsonify(result), 400

    db.session.delete(resultadosTest)
    db.session.commit()

    result["data"] = resultadosTest
    result["status_code"] = 200
    result["msg"] = "Se eliminó el resultado"
    return jsonify(result), 200