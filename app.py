# Before running, make sure to run in the terminal:
# pip install bcrypt
# pip install flask

from flask import Flask, request, redirect, url_for, render_template, session
from database import get_db, init_db
import bcrypt
import re
import logging

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

init_db()

# ---------- PASSWORD VALIDATION ----------
def is_valid_password(password):
    return (
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[^A-Za-z0-9]", password)
    )

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            session["user"] = username
            logging.info(f"User {username} logged in successfully")
            return redirect(url_for("dashboard"))
        else:
            error = "Incorrect username or password"

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            error = "Fields cannot be empty"
        elif not is_valid_password(password):
            error = "Password must include uppercase, lowercase, number, and special character"
        else:
            conn = get_db()
            try:
                hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_pw)
                )
                conn.commit()
                logging.info(f"New user {username} registered")

                return redirect(url_for("login"))
            except:
                conn.rollback()
                error = "Username already exists or error occurred"
            finally:
                conn.close()

    return render_template("register.html", error=error)

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entries = conn.execute(
        "SELECT * FROM entries WHERE user=?",
        (session["user"],)
    ).fetchall()
    conn.close()
    return render_template("dashboard.html", entries=entries, username=session["user"])

    # TEMPORARY (remove later)
    # return render_template("dashboard.html", username=session["user"])


# ---------- CREATE ----------
@app.route("/create", methods=["GET", "POST"])
def create():
    if "user" not in session:
        return redirect(url_for("login"))

    error = ""
    if request.method == "POST":
        runner = request.form["runner"].strip()
        school = request.form["school"].strip()
        grade = request.form["grade"].strip()
        time = request.form["time"].strip()

        if not runner or not school or not grade or not time:
            error = "All fields are required"
        else:
            conn = get_db()
            try:
                conn.execute(
                    "INSERT INTO entries (runner, school, grade, time, user) VALUES (?, ?, ?, ?, ?)",
                    (runner, school, grade, time, session["user"])
                )
                conn.commit()
                logging.info(f"Entry created: runner={runner}, school={school}, grade={grade}, time={time}, user={session['user']}")
                conn.close()
                return redirect(url_for("dashboard"))
            except:
                conn.rollback()
                error = "Error creating entry"
                logging.error(f"Error creating entry: {error}")
            finally:
                conn.close()

    return render_template("create.html", error=error)


# ---------- UPDATE ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entry = conn.execute(
        "SELECT * FROM entries WHERE id=? AND user=?",
        (id, session["user"])
    ).fetchone()

    if not entry:
        conn.close()
        return "Not allowed"

    if request.method == "POST":
        runner = request.form["runner"].strip()
        school = request.form["school"].strip()
        grade = request.form["grade"].strip()
        time = request.form["time"].strip()

        if not runner or not school or not grade or not time:
            error = "All fields are required"
            conn.close()
            return render_template("edit.html", entry=entry, error=error)

        try:
            conn.execute(
                "UPDATE entries SET runner=?, school=?, grade=?, time=? WHERE id=? AND user=?",
                (runner, school, grade, time, id, session["user"])
            )
            conn.commit()
            logging.info(f"Entry {id} updated by user {session['user']}")
        except:
            conn.rollback()
            logging.error(f"Error updating entry {id}")
        finally:
            conn.close()

        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("edit.html", entry=entry)

# ---------- DELETE ----------
@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    try:
        conn.execute(
            "DELETE FROM entries WHERE id=? AND user=?",
            (id, session["user"])
        )
        conn.commit()
        logging.info(f"Entry {id} deleted by user {session['user']}")
    except:
        conn.rollback()
        logging.error(f"Error deleting entry {id}")
    finally:
        conn.close()

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)