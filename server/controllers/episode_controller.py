from flask import Blueprint, jsonify, request
from server.models import Episode
from server.app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint("episode_bp", __name__)

@episode_bp.route("/", methods=["GET"])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": e.id,
        "date": e.date,
        "number": e.number
    } for e in episodes]), 200

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    return {
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [{
            "id": a.id,
            "guest_id": a.guest_id,
            "guest_name": a.guest.name,
            "rating": a.rating
        } for a in episode.appearances]
    }, 200

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted successfully"}, 200
