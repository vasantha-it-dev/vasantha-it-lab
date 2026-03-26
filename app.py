from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# This tells the internet: "When you ask for /sw.js, look in the main folder"
@app.route('/sw.js')
def serve_sw():
    return send_from_directory('.', 'sw.js')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/')
def home():
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
