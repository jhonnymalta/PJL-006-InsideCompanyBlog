from flask import Flask
from data.db_session import create_tables

from views.core_view import core
from views.handlers_view import error_pages
from views.users_view import users_routes

from models.User import User

from flask_login import LoginManager
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users_routes)





login_manager.init_app(app)
login_manager.login_view = 'users_routes.login'


@login_manager.user_loader
def load_user(user_id):
    from data.db_session import create_session
    with create_session() as session:
        user: User = session.query(User).filter(User.id == user_id).first()
    return  user
if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)