from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

NOTES_FILE = "notes.txt"

# Load notes from the file


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Save notes to the file


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for note in notes:
            file.write(note + "\n")


notes = load_notes()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("index.html", notes=notes)


@app.route("/save", methods=["POST"])
def save():
    save_notes(notes)
    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for("home"))


@app.route("/edit/<int:index>", methods=["POST"])
def edit_note(index):
    new_text = request.form.get("edited_note")
    if 0 <= index < len(notes):
        notes[index] = new_text
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
