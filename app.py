from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --- 1. THE PLAY STORE & PWA BRIDGE ---
# This allows the Android App to find its identity and "engine"
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

# --- 2. THE MAIN PAGES ---
@app.route('/')
def home():
    # Your main "Home" or "Portfolio" page
    return render_template('portfolio.html')

@app.route('/builder')
def builder():
    # The page where users can build their own portfolio
    return render_template('builder.html')

# --- 3. THE THEMES ---
# These are needed if your buttons link to specific theme previews
@app.route('/theme/cyber')
def cyber_theme():
    return render_template('cyber_theme.html')

@app.route('/theme/minimal')
def minimal_theme():
    return render_template('minimal_theme.html')

# --- 4. IMAGE HELPER ---
# This ensures that your 'profile.jpeg' or other images load correctly
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # '0.0.0.0' helps Render listen to the outside world
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)