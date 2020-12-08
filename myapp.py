from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/change', methods = ['POST'])
def change():
    return redirect(request.form['url'])

if __name__ == '__main__':
    app.run(debug=False)
