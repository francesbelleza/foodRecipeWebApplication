# Need to create 4 pages:
#       [x] /recipes
#           [x] This page with an unordered list Links to an external
#              site it will show all of the names of the recipes you have.
#           [x] HTML
#       [x] /recipe/new
#           [x] In this page you will have a form that will allow you
#              to add a new recipe.
#           [x] HTML
#       [x] /recipe/<integer>
#           [x] This page will return one recipe with its details
#           [x] HTML
#       [x] /recipe/<integer>/delete
#           [x] This page will delete the specific recipe
#           [x] HTML

from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.security import generate_password_hash

from app import myapp_obj, login_manager
from flask import render_template, flash, redirect, url_for, request
from flask import redirect
from app.forms import LoginForm, NewRecipe
from app.models import User, Recipe
from app import db


@myapp_obj.route("/")
def home():
    recipes = Recipe.query.all()
    return render_template("home.html", recipes=recipes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@myapp_obj.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()

    if form.validate_on_submit():
        if form.username.data == "correct_username" and form.password.data == "correct_password":
            flash('Login successful.', 'success')
            return redirect(url_for('recipes'))

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash(f"Welcome back, {user.username}.", "success")
                return redirect(url_for('home'))
        else:
                flash("Wrong username or password", "error")


        if not user:
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=form.remember_me.data)
            flash(f"Account created", "success")
            return redirect(url_for("home"))
    return render_template("login.html", title='Sign In', form=form)

@myapp_obj.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", 'success')
    return redirect(url_for("login"))

@myapp_obj.route("/recipes", methods = ['GET'])
@login_required
def recipes():
    all_recipes = Recipe.query.all()

    return render_template("recipes.html", title='List of Recipes', recipes=all_recipes)


@myapp_obj.route("/recipe/<int:recipe_id>")
@login_required
def specific_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    return render_template("specific_recipe.html", recipe=recipe)


@myapp_obj.route("/recipe/new", methods = ['GET', 'POST'])
@login_required
def new_recipe():
    form = NewRecipe()

    if form.validate_on_submit():
        recipe = Recipe(
            title = form.title.data,
            description = form.description.data,
            ingredients = form.ingredients.data,
            instructions = form.instructions.data
        )
        db.session.add(recipe)
        db.session.commit()

        flash(f'Recipe "{form.title.data}" succesfully saved!', 'success')
        return redirect(url_for('recipes'))

    return render_template("new_recipe.html", title='Add a New Recipe', form=form)


@myapp_obj.route("/recipe/<int:recipe_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if request.method == 'POST':
        db.session.delete(recipe)
        db.session.commit()
        flash(f'Recipe "{recipe.title}" successfully deleted', 'success')
        return redirect(url_for('recipes'))

    return render_template("delete_recipe.html", recipe=recipe)