from flask import Flask, render_template, send_from_directory, make_response
import os

# Simplified setup
app = Flask(__name__)

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('.', 'manifest.json', mimetype='application/json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('.', 'sw.js', mimetype='application/javascript')

@app.route('/')
def home():
    # This will look for 'templates/portfolio.html'
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)