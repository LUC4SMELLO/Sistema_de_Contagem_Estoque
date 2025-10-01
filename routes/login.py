from flask import Blueprint, request, flash, redirect, url_for, render_template, session

from backend.validadores.validar_login import validar_login


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome_completo = str(request.form.get("nome_completo")).rstrip()
        senha = str(request.form.get("senha")).rstrip()

        valido, mensagem = validar_login(nome_completo, senha)
        if not valido:
            flash(mensagem, "erro")
            return render_template("login.html")
        
        else:
            session["username"] = nome_completo
            return redirect(url_for("contagem_estoque.contagem_estoque"))
        

    
    return render_template("login.html")