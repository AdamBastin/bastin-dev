import os

from flask import cli 

from bastinweb import create_app

def create_app_with_config(*args):
    # Determine the configuration based on an environment variable
    # Default to 'development' if not set
    env = os.getenv('FLASK_ENV', 'development').lower()
    return create_app(f'bastinweb.config.{env.capitalize()}Config')


# @cli.command()
# def show_urls():
#     """Show all registered URLs."""
#     app = create_app_with_config()
#     with app.app_context():
#         for rule in app.url_map.iter_rules():
#             print(f"{rule.endpoint}: {rule}")

if __name__ == "__main__":
    app = create_app_with_config()
    app.run(host='0.0.0.0', port=5000, debug=True)