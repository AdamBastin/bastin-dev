import os

from bastinweb import create_app

if __name__ == "__main__":
    env = os.getenv('FLASK_ENV', 'development').lower()
    app = create_app(f'bastinweb.config.{env.capitalize()}Config')
    app.run(host='0.0.0.0', port=8000)