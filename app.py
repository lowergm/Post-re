from flask import Flask, render_template, url_for, request, redirect

from database.database import db, Postagem

app = Flask(__name__)

@app.before_request
def _db_connect():
    db.connect()

@app.after_request
def _db_close(response):
    db.close()
    return response

@app.route("/")
def postagens():
    postagem = Postagem.select()
    return render_template("index.html", postagem=postagem)

@app.route("/criar", methods=["POST", "GET"])
def makePost():
    return render_template("post.html")

@app.route("/add", methods=["POST", "GET"])
def add_post():
    titulo = request.form["titulo"]
    texto = request.form["textoPost"]
    topico = request.form["topico"]
    Postagem.create(titulo=f"{titulo}", texto=f"{texto}", topico=f"{topico}")
    return redirect(url_for("postagens"))
#
#@app.route("/list_topic", methods=["GET", "POST"])
#def list_topic():
#    if request.method == "POST":
#        topicoPesquisa = request.form["pesquisarTopico"]
#        topicos = Postagem.select().where(Postagem.topico==f"{topicoPesquisa}")
#        return render_template("topico.html", topicos=topicos)
#    return redirect(url_for("postagens"))
#

if __name__ == "__main__":
    db.connect()
    db.create_tables([Postagem], safe=True)
    app.run(debug=True)
