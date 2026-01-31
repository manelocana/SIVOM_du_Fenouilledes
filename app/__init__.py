

from flask import Flask

from app.routes.home_routes import home_bp
from app.routes.sivm_routes import sivm_bp
from app.routes.aci_routes import aci_bp
from app.routes.blog_routes import blog_bp
from app.routes.contact_routes import contact_bp




def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(sivm_bp)
    app.register_blueprint(aci_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)

    
    
    
    return app