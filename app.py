from flask import Flask

from routes.homepage import homepage_bp
from routes.cadastro import cadastro_bp
from routes.login import login_bp

from routes.contagem_estoque import contagem_estoque_bp
from routes.salvar_contagem import salvar_contagem_bp

from routes.salvar_contagem_temporaria import salvar_contagem_temporaria_bp
from routes.carregar_contagem_temporaria import carregar_contagem_temporaria_bp

from routes.selecionar_contagem import selecionar_contagem_bp

from routes.contagem_doces import contagem_doces_bp
from routes.salvar_contagem_doces import salvar_contagem_doces_bp

from routes.contagem_geladeira import contagem_geladeira_bp
from routes.salvar_contagem_geladeira import salvar_contagem_geladeiras_bp

app = Flask(__name__)
app.secret_key = "secret_key"

# REGISTRAR BLUEPRINTS
app.register_blueprint(homepage_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)

app.register_blueprint(contagem_estoque_bp)
app.register_blueprint(salvar_contagem_bp)

app.register_blueprint(salvar_contagem_temporaria_bp)
app.register_blueprint(carregar_contagem_temporaria_bp)

app.register_blueprint(selecionar_contagem_bp)

app.register_blueprint(contagem_doces_bp)
app.register_blueprint(salvar_contagem_doces_bp)

app.register_blueprint(contagem_geladeira_bp)
app.register_blueprint(salvar_contagem_geladeiras_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)