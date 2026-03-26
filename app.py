from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# This serves ANY file in your main folder (sw.js, manifest.json, etc.)
@app.route('/<path:filename>')
def serve_root_files(filename):
    return send_from_directory('.', filename)

@app.route('/')
def home():
    return render_template('portfolio.html')

@app.route('/builder')
def builder():
    return render_template('builder.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)