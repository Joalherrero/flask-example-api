from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test():
    return 'Hola Test'

@app.route('/primer_html')
def primer_html():
   return '''

    <html>
        <body>
        <h1>Flask</h1>
        </body>
    </html>

   '''

@app.route('/')
def hello_world():
    return 'Hola Flask 1.1.1 , desde el contendor!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
