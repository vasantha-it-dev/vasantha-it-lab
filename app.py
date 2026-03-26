from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --- THE PLAY STORE BRIDGE ---
# These routes allow PWABuilder to find your app's "ID Card" and "Engine"
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

# --- YOUR APP ROUTES ---
@app.route('/')
def home():
    # This points to your main portfolio page
    return render_template('portfolio.html')

@app.route('/builder')
def builder():
    return render_template('builder.html')

# Add any other routes (cyber_theme, etc.) here as needed

if __name__ == '__main__':
    app.run(debug=True)
