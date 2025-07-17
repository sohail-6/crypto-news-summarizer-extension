# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    url = data.get('url', '')
    return jsonify({
        'summary': [
            "Sample summary line 1.",
            "Sample summary line 2.",
            "Sample summary line 3."
        ],
        'sentiment': 'neutral'
    })

if __name__ == '__main__':
    app.run(debug=True)
