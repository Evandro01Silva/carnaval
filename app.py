from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

LANGUAGES = ['pt', 'en', 'es', 'it', 'fr', 'de', 'ru']
DEFAULT_LANG = 'pt'

def load_translations(lang):
    if lang not in LANGUAGES:
        lang = DEFAULT_LANG
    with open(f'translations/{lang}.json', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    lang = request.args.get('lang', DEFAULT_LANG)
    texts = load_translations(lang)
    return render_template('index.html', texts=texts, lang=lang)

@app.route('/historia')
def historia():
    lang = request.args.get('lang', DEFAULT_LANG)
    texts = load_translations(lang)
    return render_template('historia.html', texts=texts, lang=lang)

@app.route('/personagens')
def personagens():
    lang = request.args.get('lang', DEFAULT_LANG)
    texts = load_translations(lang)
    return render_template('personagens.html', texts=texts, lang=lang)

@app.route("/galeria")
def galeria():
    lang = request.args.get("lang", "pt")
    texts = load_translations(lang)
    return render_template("galeria.html", texts=texts, lang=lang)

@app.route('/como_chegar')
def como_chegar():
    lang = request.args.get('lang', DEFAULT_LANG)
    texts = load_translations(lang)
    return render_template('como_chegar.html', texts=texts, lang=lang)

@app.route('/sobre')
def sobre():
    lang = request.args.get('lang', DEFAULT_LANG)
    texts = load_translations(lang)
    return render_template('sobre.html', texts=texts, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
