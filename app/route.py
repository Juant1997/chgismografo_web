
from flask import Blueprint, render_template, request
from app import collection  # importa la colección

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    comment = request.form['comment']

    # Guardar en MongoDB
    collection.insert_one({
        "name": name,
        "age": age,
        "comment": comment
    })

    return f"<h2>Gracias, {name}!</h2><p>Edad: {age}</p><p>Comentario: {comment}</p>"
