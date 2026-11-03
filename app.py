from flask import Flask, render_template

app = Flask(__name__)

# List containing five of my favortie books
books = [
    "The Way of Kings",
    "A Game of Thrones",
    "The Eye of the World",
    "The Dark Tower IV: Wizard and Glass",
    "Mistborn"
]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/list")
def show_list():
    return render_template("list.html", items=books)

if __name__ == "__main__":
    app.run(debug=True)