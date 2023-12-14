from flask import Flask, render_template, request, redirect
from models.team_model import Team

app = Flask(__name__)


@app.route("/")
@app.route("/times")
def listar_times():
    times = Team.find_all()
    dict_times = [time.to_dict() for time in times]
    return render_template("times.html", times=dict_times)


@app.route("/times/adicionar", methods=["GET", "POST"])
def adicionar_time():
    if request.method == "POST":
        nome = request.form["nome"]
        novo_time = Team(name=nome)
        novo_time.save()
        return redirect("/times")

    return render_template("adicionar_time.html")


@app.route("/times/editar/<team_name>", methods=["GET", "POST"])
def editar_time(team_name):
    time = Team.find_by_name(team_name)

    if not time:
        return redirect("/times")

    if request.method == "POST":
        novo_nome = request.form["nome"]
        time.name = novo_nome
        time.update()
        return redirect("/times")

    return render_template("editar_time.html", time=time.to_dict())


@app.route("/times/excluir/<team_name>", methods=["GET", "POST"])
def excluir_time(team_name):
    time = Team.find_by_name(team_name)

    if not time:
        return redirect("/times")

    if request.method == "GET":
        return render_template("excluir_time.html", time=time.to_dict())

    time.delete()
    return redirect("/times")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
