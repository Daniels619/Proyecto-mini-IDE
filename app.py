from flask import Flask, request, jsonify, render_template
from parser import analizar_sintactico
from lexer import analizar_lexico_con_diccionario  # Cambiado aquí
from turing import ejecutar_maquina_turing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar-lexico', methods=['POST'])
def lexico():
    data = request.get_json()
    code = data.get('code', '')
    resultado = analizar_lexico_con_diccionario(code)  # Usar el nuevo análisis léxico
    return jsonify({'resultado': resultado})  # Ya es lista de dicts, jsonify funciona bien

@app.route('/analizar-sintactico', methods=['POST'])
def sintactico():
    data = request.get_json()
    code = data.get('code', '')
    resultado_obj = analizar_sintactico(code)

    return jsonify({
        'resultado': resultado_obj.get('resultado', ''),
        'errores': resultado_obj.get('errores', [])
    })

@app.route('/turing', methods=['POST'])
def turing():
    data = request.get_json()
    code = data.get('code', '')
    resultado = ejecutar_maquina_turing(code)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
