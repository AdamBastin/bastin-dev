from flask import Blueprint, render_template

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio', template_folder='templates')


@portfolio_bp.route('/')
def portfolio():
    return render_template('main_template.html', main_content='portfolio_page.html')


@portfolio_bp.route('/TeamsChatExporter')
def teams_chat_exporter():
    return render_template('main_template.html', main_content='portfolios/teams_chat_exporter.html')