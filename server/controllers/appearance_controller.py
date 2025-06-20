from flask import Blueprint, request, jsonify
from server.models import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint("appearance_bp", __name__)

@appearance_bp.route("/", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    try:
        new = Appearance(
            guest_id=data["guest_id"],
            episode_id=data["episode_id"],
            rating=data["rating"]
        )
        db.session.add(new)
        db.session.commit()
        return {
            "id": new.id,
            "guest_id": new.guest_id,
            "episode_id": new.episode_id,
            "rating": new.rating
        }, 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
