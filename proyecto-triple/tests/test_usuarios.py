from app import create_app, db
from app.usuarios.models import User

app = create_app()

def test_user_creation():
    with app.app_context():
        user = User(email='test@example.com', password='password', name='Test User')
        db.session.add(user)
        db.session.commit()
        
        assert user.id is not None
        assert user.email == 'test@example.com'
        assert user.name == 'Test User'

def test_user_login():
    with app.app_context():
        user = User(email='test@example.com', password='password', name='Test User')
        db.session.add(user)
        db.session.commit()
        
        logged_in_user = User.query.filter_by(email='test@example.com').first()
        assert logged_in_user is not None
        assert logged_in_user.check_password('password') is True

def test_user_deletion():
    with app.app_context():
        user = User(email='delete@example.com', password='password', name='Delete User')
        db.session.add(user)
        db.session.commit()
        
        db.session.delete(user)
        db.session.commit()
        
        deleted_user = User.query.filter_by(email='delete@example.com').first()
        assert deleted_user is None

def test_user_update():
    with app.app_context():
        user = User(email='update@example.com', password='password', name='Update User')
        db.session.add(user)
        db.session.commit()
        
        user.name = 'Updated User'
        db.session.commit()
        
        updated_user = User.query.filter_by(email='update@example.com').first()
        assert updated_user.name == 'Updated User'