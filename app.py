from Flask import Flask, render_template, send_from_directory, make_response
import os

app = Flask(__name__)

# Serve the PWA manifest directly from the root
@app.route('/manifest.json')
def serve_manifest():
    response = make_response(send_from_directory('.', 'manifest.json'))
    response.headers['Content-Type'] = 'application/json'
    return response

# Serve the Service Worker directly from the root
@app.route('/sw.js')
def serve_sw():
    response = make_response(send_from_directory('.', 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response

# Serve main app routes
@app.route('/')
def home():
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)