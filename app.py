from flask import Flask, render_template, request, redirect
import short_url_generator
import pyshorteners
import encurtador

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = encurtador.generate_short_url_2(long_url)
    # Implementação própria com hash MD5 (generate_short_url)
    # Utilização de um serviço de encurtamento de URL como o pyshorteners (generate_short_url_2)
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = short_url_generator.get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
