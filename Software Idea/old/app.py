from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define other routes as needed
@app.route('/process_option', methods=['POST'])
def process_option():
    data = request.get_json()
    option = data['option']
    
    # Perform operations based on the selected option (MDFY, ARU, RC)
    
    return jsonify({'message': 'Option processed successfully'})
@app.route('/mdfy')
def modify_car_list():
    # Logic for handling car list modification
    return render_template('mdfy.html')

# Define other routes as needed
@app.route('/logout')
def logout():
    # Logic for logging out
    return jsonify({'message': 'Logged out successfully'})
if __name__ == '__main__':
    app.run(debug=True)
