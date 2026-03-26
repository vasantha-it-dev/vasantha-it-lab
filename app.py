from flask import Flask, render_template, request

app = Flask(__name__)

# 1. The Home Route (The Builder Page)
@app.route('/')
def index():
    # This renders your form where you enter name, bio, and pick a theme
    return render_template('builder.html')

# 2. The View Route (The Theme Logic)
@app.route('/view', methods=['POST'])
def view():
    # Collect data from the form inputs
    # .get() helps prevent errors if a field is empty
    name = request.form.get('name', 'Vasantha IT Architect')
    bio = request.form.get('bio', 'IT Student at S.V.N College')
    skills_raw = request.form.get('skills', '')
    
    # Convert the comma-separated string into a clean list
    skills_list = [s.strip() for s in skills_raw.split(',') if s.strip()]
    
    user_data = {
        'name': name,
        'bio': bio,
        'skills': skills_list
    }
    
    # Get the value from the radio buttons in builder.html
    selected_theme = request.form.get('theme')

    # THEME SWITCHER LOGIC:
    # This checks which theme you picked and opens the matching file
    if selected_theme == 'cyber':
        return render_template('cyber_theme.html', user=user_data)
    elif selected_theme == 'minimal':
        return render_template('minimal_theme.html', user=user_data)
    else:
        # This is your default 'Cinematic' template (portfolio.html)
        return render_template('portfolio.html', user=user_data)

if __name__ == '__main__':
    # '0.0.0.0' allows your friends on the same Wi-Fi to see your app
    app.run(debug=True, host='0.0.0.0', port=5000)
