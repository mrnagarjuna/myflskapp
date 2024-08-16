from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials for demonstration
dummy_email = "user@example.com"
dummy_password = "password"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == dummy_email and password == dummy_password:
            return "Logged in successfully!"
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
