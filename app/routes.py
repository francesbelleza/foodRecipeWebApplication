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
#       [] /recipe/<integer>/delete
#           [] This page will delete the specific recipe
#           [] HTML


from app import myapp_obj
from flask import render_template, flash, redirect, url_for, request
from flask import redirect
from app.forms import LoginForm, NewRecipe
from app.models import User, Recipe
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
    all_recipes = Recipe.query.all()

    return render_template("recipes.html", title='List of Recipes', recipes=all_recipes)


@myapp_obj.route("/recipe/<int:recipe_id>")
def specific_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    return render_template("specific_recipe.html", recipe=recipe)


@myapp_obj.route("/recipe/new", methods = ['GET', 'POST'])
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
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if request.method == 'POST':
        db.session.delete(recipe)
        db.session.commit()
        flash(f'Recipe "{recipe.title}" successfully deleted', 'success')
        return redirect(url_for('recipes'))

    return render_template("delete_recipe.html", recipe=recipe)