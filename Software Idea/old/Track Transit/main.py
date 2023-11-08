from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('modify_car.html', message="Welcome to Modify Car")

@app.route('/modify_car', methods=['POST'])
def modify_car():
    car_number = request.form['car_number']
    btn_pressed = request.form['btnpr']

    if btn_pressed == 'add_car':
        # Add car logic here
        message = f'Added car with number {car_number}'
    elif btn_pressed == 'delete_car':
        # Delete car logic here
        message = f'Deleted car with number {car_number}'
    else:
        message = 'Unknown action'

    return render_template('modify_car.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
