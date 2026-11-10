from flask import Flask

from routes.homepage import homepage_bp
from routes.cadastro import cadastro_bp
from routes.login import login_bp

from routes.selecionar_contagem import selecionar_contagem_bp

from routes.contagem import contagem_bp

from routes.relatorio_entrada import relatorio_entrada_bp

from routes.relatorio_datas import relatorio_datas_bp

from routes.trocas import trocas_bp


app = Flask(__name__)
app.secret_key = "secret_key"

# REGISTRAR BLUEPRINTS
app.register_blueprint(homepage_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)

app.register_blueprint(selecionar_contagem_bp)

app.register_blueprint(contagem_bp)

app.register_blueprint(relatorio_entrada_bp)

app.register_blueprint(relatorio_datas_bp)

app.register_blueprint(trocas_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)
