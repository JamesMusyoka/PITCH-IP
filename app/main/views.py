# from flask_login import login_required, current_user
# from .forms import PostForm
# from .. import db, photos
# from flask import render_template
# from . import main
# from ..models import User

# @main.route('/index', methods=['GET', 'POST'])
# def home():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Pitch(body=form.post.data, author=current_user,
#                      category=form.category.data)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post is now live!')
    
#         return redirect(url_for('main.index'))

#     # posts = Pitch.retrieve_posts(id).all()

#     return render_template("index.html", title='Home Page', form=form, posts=posts)

@main.route('/')
# @login_required
def index():

#     title = 'WELCOME TO JAMOPITCH'
#     return render_template('index.html')
# # 'test':TestConfig
# # posts = [
# #     {
# #         'author': {'username': 'Phanise'}
# #         'body': 'Beautiful day in Holland!'
# #         },
# #         {
# #             'author': {'username': 'James' },
# #             'body': 'The Original Series was cool'
# #             }
# #             ]

    return render_template('index.html')
# @main.route('/post', methods=['GET', 'POST'])
# @login_required
# def post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = form.post.data
#         category = form.category.data
#         user = current_user
#         new_pitch = Pitch(body=post, category=category, user=user)

#         # save pitch
#         db.session.add(new_pitch)
#         db.session.commit()
#         return redirect(url_for('main.explore', uname=user.username))

#     return render_template('post.html', form=form)

# # @main.route('/index.html', methods=['GET', 'POST'])
# # # @login_required
# # def pitch():
# #     form = PostForm()
# #     if form.validate_on_submit():
# #     #    post = form.post.data
# #     #    category = form.category.data
# #     #    user = current_user


# #        new_pitch = Pitch(body = post,category = category,user = user)

# #        # save pitch
# #        db.session.add(new_pitch)
# #        db.session.commit()

# #     life = Pitch.query.filter_by(category='index.html')
# #      # users_post = Pitch.query.filter_by(user_id=id).all()
# #     return render_template('user_index.html', title = 'title',form=form)

#     @main.route('/user/<uname>')
#     def profile(uname):
#         user = User.query.filter_by(username=uname).first()

#         if user is None:
#             abort(404)

#     return render_template("profile/profile.html", user=user)

#     @main.route('/user/<uname>/update', methods=['GET', 'POST'])
#     @login_required
#     def update_profile(username):
#         user = User.query.filter_by(username=uname).first()
#         if user is None:
#             abort(404)

#             form = UpdateProfile()
#         if form.validate_on_submit():
#             user.bio = form.bio.data

#             db.session.add(user)
#             db.session.commit()

#         return redirect(url_for('.profile', uname=user.username))

#     return render_template('profile/update.html', form=form)

#     @main.route('/user/<uname>/update/pic', methods=['POST'])
#     @login_required
#     def update_pic(uname):
#         user = User.query.filter_by(username=uname).first()
#         if 'photo' in request.files:
#             filename = photos.save(request.files['photo'])
#             path = f'photos/{filename}'
#             user.profile_pic_path = path
#             db.session.commit()
#         return redirect(url_for('main.profile', uname=uname))

#     @main.route('/technology' ,methods = ['GET','POST'])
#     def technology():
#         technology = Pitch.query.filter_by(category = 'Technology').all()
#         form = CommentForm()
#         if form.validate_on_submit():
#             details = form.details.data
#             user = current_user
            
#             new_comment = Comments(details = details,pitch_id=id,user =user)
#             db.session.add(new_comment)
#             db.session.commit()
        
#         return render_template('technology.html', technology = technology,form=form)

#     @main.route('/interview' ,methods = ['GET','POST'])
#     def business():
#         business = Pitch.query.filter_by(category = 'business').all()
#         form = CommentForm()
#         if form.validate_on_submit():
#             details = form.details.data
#             user = current_user

#             new_comment = Comments(details = details,pitch_id=id,user =user)
#             db.session.add(new_comment)
#             db.session.commit()

#         return render_template('business.html', business = business,form=form)

#     @main.route('/pickuplines' ,methods = ['GET','POST'])
#     def pickuplines():
        
#         form = CommentForm()
#         if form.validate_on_submit():
#             details = form.details.data
#             user = current_user
            
#             new_comment = Comments(details = details,pitch_id=id,user =user)
#             db.session.add(new_comment)
#             db.session.commit()
            
#         pickuplines = Pitch.query.filter_by(category = 'Pickuplines').all()
            
#         if pickuplines is None:
#             abort(404)

#         return render_template('pickuplines.html', pickuplines = pickuplines,form=form)

