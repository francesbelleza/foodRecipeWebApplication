# Need to create 4 pages:
#       [] /recipes
#           [] This page with an unordered list Links to an external
#              site.will show all of the names of the recipes you have.
#           [] HTML
#       [x] /recipe/new
#           [x] In this page you will have a form that will allow you
#              to add a new recipe.
#           [] HTML
#       [] /recipe/<integer>
#           [] This page will return one recipe with its details
#           [] HTML
#       [] /recipe/<integer>/delete
#           [] This page will delete the specific recipe
#           [] HTML


from app import myapp_obj
from flask import render_template, flash, redirect, url_for
from flask import redirect
from app.forms import LoginForm
from app.models import User
from app import db

@myapp_obj.route("/")
def home():
    return render_template("home.html")

@myapp_obj.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.user.data == "correct_username" and form.password.data == "correct_password":
            flash('Login successful.', 'success')
            return redirect(url_for('recipes'))
        else:
            flash('Wrong user name and/or password', 'error')

    return render_template("login.html", title='Sign In', form=form)


@myapp_obj.route("/recipes", methods = ['GET'])
def recipes():
    return render_template("recipes.html", title='List of Recipes')


@myapp_obj.route("/recipe/new", methods = ['GET', 'POST'])
def new_recipe():
    form = new_recipe()

    if form.validate_on_submit():
        flash(f'Recipe "{form.title.data}" succesfully saved!', 'success')
        return redirect(url_for('recipes'))

    return render_template("new_recipe.html", title='Add a New Recipe', form=new_recipe)
