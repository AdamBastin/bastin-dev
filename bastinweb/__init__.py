from flask import Flask

from bastinweb.routes.portfolio import portfolio_bp
from bastinweb.routes.main_page import main_page_bp

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(main_page_bp)

    return app

def create_app():
    app = Flask(__name__)

    app.config.from_object('bastinweb.config.ProductionConfig')
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(main_page_bp)

    return app