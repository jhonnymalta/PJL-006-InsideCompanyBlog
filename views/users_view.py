from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from data.db_session import create_session
from models.User import User




users_routes = Blueprint('users_routes',__name__)





#register
@users_routes.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        password_value = request.form['password']
        hashing = User.hashing_password(password_value)

        user: User = User(
            user_name = request.form['user_name'],
            password_hash = hashing,
            profile_image = request.form['profile_image'],
            email = request.form['email']
        )
      
        
        with create_session() as session:        
            session.add(user)
            session.commit() 
            flash('Thanks for registration!')
            return redirect(url_for('users_routes.login'))
    return render_template('register.html')



#login
@users_routes.route("/login",methods=['POST','GET'])
def login():
    

    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        with create_session() as session:
            user = session.query(User).filter(User.user_name == user_name).first()
            if user is None:
                flash("Username or Password don't mach!")
                return redirect(url_for('users_routes.login'))
                
            elif user.check_password(password) and user is not None:
                login_user(user)
                
                flash('Log in success!')
                next = request.args.get('next')
                return redirect(next or url_for('core.index')) 
            else:
                #return redirect(url_for('users_route.login'))    
                return render_template('login.html')        
                
                
           
    return render_template('login.html')

#logout
@users_routes.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))
