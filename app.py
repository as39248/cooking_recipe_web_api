from flask import Flask, render_template, request, redirect, url_for
import search_recipe


app = Flask(__name__)


@app.get('/')
def home():
    return render_template('example.html')


@app.route('/search', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        input_value = request.form.get("search")
        return search_recipe.search_recipes(input_value)

    return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
