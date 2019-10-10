from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

client = MongoClient()
db = client.Contractor
secrets = db.secrets

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template("home.html")

@app.route('/secrets')
def secrets_index():
    """Show all secrets"""
    return render_template("secrets_index.html", secrets = secrets.find())

@app.route('/secrets/new')
def secrets_new():
    """Create a new secrets"""
    return render_template("secrets_new.html")

@app.route('/secrets', methods=["POST"])
def secrets_submit():
    """Submit a new secret."""
    timestamp = request.form.get("timestamp")
    timestamp =  timestamp[4:6] + "-" + timestamp[6:] + "-" + timestamp[0:4]
    secret = {
        "type": request.form.get("secret-type"),
        "name": request.form.get("secret-holder"),
        "text": request.form.get("secret-text"),
        "timestamp": timestamp
    }
    print(request.form.to_dict())
    secrets.insert_one(secret)
    return redirect(url_for("secrets_index"))

@app.route('/secrets/<secret_id>')
def secrets_show(secret_id):
    secret = secrets.find_one({"_id" : ObjectId(secret_id)})
    return render_template("secrets_show.html", secret=secret)

@app.route('/secrets/:id/edit')
def secrets_edit(secret_id):
    """Show the edit form for a displayed secret."""
    secret = secrets.find_one({'_id': ObjectId(secret_id)})
    return render_template('secrets_edit.html', secret = secret)

@app.route('/secrets/:id', methods=["POST"])
def secrets_update(secret_id):
    """Submit an edited secret."""
    updated_secret = {
        "type": request.form.get("secret-type"),
        "name": request.form.get("secret-holder"),
        "text": request.form.get("secret-text")
    }
    secrets.update_one(
        {'_id': ObjectId(secret_id)},
        {'$set': updated_secret})
    return redirect(url_for('secret_show', secret_id=secret_id))

@app.route('/secrets/:id/delete', methods=["POST"])
def secrets_delete():
    pass

if __name__ == '__main__':
    app.run(debug=True)