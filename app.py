from flask import Flask
from flask_jwt_extended import JWTManager
from api.trains import trains_bp
from api.bookings import bookings_bp
from api.auth import auth_bp  

def create_app():
    app = Flask(__name__)    
    app.config.from_object('config.Config')
    jwt = JWTManager(app)

    # Register the authentication blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(trains_bp)
    app.register_blueprint(bookings_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
