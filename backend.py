from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Müzik dosyası için route
@app.route('/10numaran.mp3')
def serve_music():
    return send_from_directory('.', '10numaran.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
