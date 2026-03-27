from flask import Flask, render_template, send_from_directory, make_response
import os

# This 'root_path' tells Render exactly where your master1 folder is
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static',
            root_path=os.path.dirname(os.path.abspath(__file__)))

@app.route('/manifest.json')
def serve_manifest():
    response = make_response(send_from_directory(app.root_path, 'manifest.json'))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/sw.js')
def serve_sw():
    response = make_response(send_from_directory(app.root_path, 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/')
def home():
    # This looks for portfolio.html inside your templates folder
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)