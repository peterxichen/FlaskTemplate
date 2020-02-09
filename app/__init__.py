from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        input_string = request.form["input_string"]
        return output(input_string)
    return render_template('home.html')

@app.route9('/output')
def output(input_string=None):
    data = {'input_string': input_string}
    return render_template('output.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)