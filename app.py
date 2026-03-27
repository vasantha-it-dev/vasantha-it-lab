from flask import Flask, render_template, send_from_directory, make_response
import os

# This tells Flask to look specifically in the current folder for your files
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

@app.route('/manifest.json')
def serve_manifest():
    response = make_response(send_from_directory('.', 'manifest.json'))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/sw.js')
def serve_sw():
    response = make_response(send_from_directory('.', 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/')
def home():
    # Make sure your file is named portfolio.html inside the templates folder
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)