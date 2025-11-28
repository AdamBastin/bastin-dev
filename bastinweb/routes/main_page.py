from flask import Blueprint, redirect, render_template

main_page_bp = Blueprint('main_page', __name__, url_prefix='/', template_folder='templates')

@main_page_bp.route('/')
def main_page():
    return redirect('/portfolio/')
    return render_template('maintemplate.html')