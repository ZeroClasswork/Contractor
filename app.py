from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template("home.html")

@app.route('/secrets')
def secrets_index():
    """Show all secrets"""
    return render_template("secrets_index.html")

@app.route('/secrets/new')
def secrets_new():
    """Create a new playlist"""
    return render_template("secrets_new.html")

@app.route('/secrets', methods=["POST"])
def secrets_submit():
    pass

@app.route('/secrets/:id')
def secrets_show():
    pass

@app.route('/secrets/:id/edit')
def secrets_edit():
    pass

@app.route('/secrets/:id', methods=["POST"])
def secrets_update():
    pass

@app.route('/secrets/:id/delete', methods=["POST"])
def secrets_delete():
    pass

if __name__ == '__main__':
    app.run(debug=True)