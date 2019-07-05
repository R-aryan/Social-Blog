## in users/views.property

from flask import render_template,redirect,url_for,redirect,flash,abort,Blueprint,request
from flask_login import login_user,current_user,logout_user,login_required
from companyblog import db
from companyblog.models import User,Blogpost
from companyblog.users.forms import RegistrationForm,UpdateUserForm,LoginForm
from companyblog.users.picture_handler import add_profile_picture

users= Blueprint('users',__name__)




#### views Required
# Register
@users.route('/register',methods=['GET','POST'])
def register():

    form= RegistrationForm()

    if form.validate_on_submit():
        email= form.email.data
        name=  form.name.data
        username= form.username.data
        password= form.password.data

        user= User(name,email,username,password)
        db.session.add(user)
        db.session.commit()
        flash('Thanks For Registration....!!')

        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)


#login
@users.route('/login',methods=['GET','POST'])
def login():

    form= LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Successfull....!!')

            next=request.args.get('next')

            if next==None or not next[0]=='/':
                next=url_for('core.index')

            return redirect(next)

    return render_template('login.html',form=form)



#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

#Update
@users.route('/account',methods=['GET','POST'])
@login_required

def account():
    form= UpdateUserForm()

    if form.validate_on_submit():
        if form.picture.data:
            username= current_user.username
            pic= add_profile_picture(form.picture.data,username)
            current_user.profile_image=pic

        current_user.username= form.username.data
        current_user.email= form.email.data
        db.session.commit()
        flash('Account Updated Succesfully......!!')

        return redirect(url_for('users.account'))

    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email

    profile_image= url_for('static',filename='profile_pics/'+current_user.profile_image)

    return render_template('account.html',profile_image=profile_image,form=form)



#users lists of blog posts
@users.route('/<username>')
def user_posts(username):
    page= request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()
    blog_posts = Blogpost.query.filter_by(author=user).order_by(Blogpost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user)
