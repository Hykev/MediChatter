import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = 'AGREAGR LLAVE AQUI'

@app.route('/chat.py', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje = data.get('mensaje', '')

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': mensaje
            }
        ],
    )

    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(debug=True)
