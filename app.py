from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This renders your "Portfolio Creator" page
    return render_template('portfolio.html')

@app.route('/view', methods=['POST'])
def view_portfolio():
    # This pulls the data from your form
    name = request.form.get('name')
    skills = request.form.get('skills')
    bio = request.form.get('bio')
    
    # This sends the data to your portfolio theme
    return render_template('builder.html', name=name, skills=skills, bio=bio)

if __name__ == '__main__':
    app.run(debug=True)