from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/process_option', methods=['POST'])
def process_option():
    data = request.get_json()
    option = data['option']
    print(f'{option} pressed in Python')
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
