from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This shows your "Portfolio Creator" input form
    return render_template('portfolio.html')

@app.route('/view', methods=['POST'])
def view_portfolio():
    # 1. Capture the data from the form
    name = request.form.get('name')
    # We split skills by comma so the template can loop through them
    skills_input = request.form.get('skills', '')
    skills_list = [s.strip() for s in skills_input.split(',') if s.strip()]
    bio = request.form.get('bio')
    theme = request.form.get('theme')

    # 2. Create a user object for the template
    user_data = {
        'name': name,
        'skills': skills_list,
        'bio': bio
    }

    # 3. Route to the correct theme based on the user's choice
    if theme == 'cyber':
        return render_template('cyber_theme.html', user=user_data)
    elif theme == 'minimal':
        return render_template('minimal_theme.html', user=user_data)
    else:
        # Default 'cinematic' style
        return render_template('builder.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)