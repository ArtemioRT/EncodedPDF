from flask import Flask, request, send_file
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/decode_pdf', methods=['POST'])
def decode_pdf():
    # Obtener el encoded_label y num_guia desde los parámetros de la solicitud
    encoded_label = request.json.get('encoded_label')
    num_guia = request.json.get('num_guia')

    # Validar que ambos parámetros estén presentes
    if not encoded_label or not num_guia:
        return {"error": "encoded_label y num_guia son requeridos"}, 400

    # Decodificar el contenido base64
    try:
        pdf_data = base64.b64decode(encoded_label)
    except Exception as e:
        return {"error": f"Error al decodificar base64: {str(e)}"}, 400

    # Guardar el archivo PDF en un objeto en memoria
    pdf_file = BytesIO(pdf_data)

    # Usar el num_guia como el nombre del archivo PDF
    file_name = f"archivo_{num_guia}.pdf"

    # Devolver el archivo como respuesta
    return send_file(pdf_file, as_attachment=True, download_name=file_name, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=True)
