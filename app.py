from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import encurtador

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://seu_usuario:senha@localhost:5432/flask_db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']

    # Implementação própria com hash MD5 (generate_short_url)
    short_url = encurtador.generate_short_url(long_url)
    
    # Utilização de um serviço de encurtamento de URL como o pyshorteners (generate_short_url_2)
    tiny_url = encurtador.generate_tiny_url(long_url)
    
    return render_template('shortened.html', short_url=short_url, tiny_url=tiny_url)

@app.route('/shorten')
def show_shortened():
    return render_template('shortened.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = encurtador.get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
