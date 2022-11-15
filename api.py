from flask import Flask, render_template, make_response, request

import db
import requests

app = Flask(__name__)


@app.route("/documents", methods=["GET"])
def documents():
    documents = db.get_documents()
    return {'data': documents}, 200

@app.route("/documents/<int:document_id>", methods=["GET"])
def documents_id(document_id):
    documents = db.get_documents()
    return {'data': documents[document_id -1]}

@app.route("/documents/<int:document_id>/tags", methods=["GET"])
def documents_id_tags(document_id):
    tags = db.get_tags(document_id)
    return {'tags': tags}, 200

@app.route("/")
def index():
    return render_template("index.html")


# Only keep debug=True for prod env
if __name__ == '__main__':
    app.run(debug=True, port=7003)
