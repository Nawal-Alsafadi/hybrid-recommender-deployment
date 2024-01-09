
from api.routes.recommendation_system.hybrid_bp import hybrid_recommend_bp

from flask import Blueprint


def app_routes(app):
    app.register_blueprint(hybrid_recommend_bp, url_prefix='/api')
