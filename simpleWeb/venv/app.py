from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)  # Debug print statement
    name = request.form['name']
    email = request.form['email']
    return render_template('result.html', name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)























