from flask import Flask, render_template, request, jsonify
from password_utils import analyze_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    analysis = analyze_password(password)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
