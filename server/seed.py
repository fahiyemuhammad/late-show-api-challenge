from server.app import db, create_app
from server.models import User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Drop all and recreate tables
    db.drop_all()
    db.create_all()

    # --- Users ---
    user1 = User(username="fahiye")
    user1.set_password("password123")

    # --- Guests ---
    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Comedian")

    # --- Episodes ---
    episode1 = Episode(date="2025-06-20", number=1)
    episode2 = Episode(date="2025-06-21", number=2)

    # --- Appearances ---
    appearance1 = Appearance(guest=guest1, episode=episode1, rating=4)
    appearance2 = Appearance(guest=guest2, episode=episode1, rating=5)
    appearance3 = Appearance(guest=guest1, episode=episode2, rating=3)

    # Add all to the session
    db.session.add_all([
        user1,
        guest1, guest2,
        episode1, episode2,
        appearance1, appearance2, appearance3
    ])

    # Commit to DB
    db.session.commit()

    print("✅ Done seeding!")