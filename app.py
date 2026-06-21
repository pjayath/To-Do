import calendar
import sqlite3
from datetime import date, datetime
from pathlib import Path

from flask import Flask, g, redirect, render_template, request, url_for

DB_PATH = Path(__file__).parent / "todo.db"

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            date TEXT NOT NULL,
            time TEXT NOT NULL DEFAULT '00:00'
        )
        """
    )
    existing_cols = [row[1] for row in db.execute("PRAGMA table_info(todos)").fetchall()]
    if "time" not in existing_cols:
        db.execute("ALTER TABLE todos ADD COLUMN time TEXT NOT NULL DEFAULT '00:00'")
    db.commit()
    db.close()


@app.route("/")
def index():
    today = date.today()
    return redirect(url_for("month_view", year=today.year, month=today.month))


@app.route("/calendar/<int:year>/<int:month>")
def month_view(year, month):
    db = get_db()
    rows = db.execute(
        "SELECT date, COUNT(*) as total, SUM(done) as done_count FROM todos "
        "WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ? GROUP BY date",
        (f"{year:04d}", f"{month:02d}"),
    ).fetchall()
    counts = {row["date"]: {"total": row["total"], "done": row["done_count"]} for row in rows}

    cal = calendar.Calendar(firstweekday=6)
    weeks = cal.monthdatescalendar(year, month)

    prev_month = month - 1 or 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    return render_template(
        "calendar.html",
        weeks=weeks,
        year=year,
        month=month,
        month_name=calendar.month_name[month],
        today=date.today(),
        counts=counts,
        prev_year=prev_year,
        prev_month=prev_month,
        next_year=next_year,
        next_month=next_month,
    )


@app.route("/day/<day>")
def day_view(day):
    db = get_db()
    todos = db.execute(
        "SELECT * FROM todos WHERE date = ? ORDER BY date ASC, time ASC", (day,)
    ).fetchall()
    day_date = date.fromisoformat(day)
    return render_template("day.html", todos=todos, day=day, day_date=day_date)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    todo_date = request.form.get("date") or date.today().isoformat()
    todo_time = request.form.get("time") or datetime.now().strftime("%H:%M")
    if title:
        db = get_db()
        db.execute(
            "INSERT INTO todos (title, date, time) VALUES (?, ?, ?)",
            (title, todo_date, todo_time),
        )
        db.commit()
    return redirect(url_for("day_view", day=todo_date))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    db = get_db()
    db.execute("UPDATE todos SET done = NOT done WHERE id = ?", (todo_id,))
    db.commit()
    todo_date = request.form.get("date")
    return redirect(url_for("day_view", day=todo_date))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    db = get_db()
    db.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    db.commit()
    todo_date = request.form.get("date")
    return redirect(url_for("day_view", day=todo_date))


@app.route("/reschedule/<int:todo_id>", methods=["POST"])
def reschedule(todo_id):
    new_date = request.form.get("new_date")
    old_date = request.form.get("date")
    db = get_db()
    if new_date:
        db.execute("UPDATE todos SET date = ? WHERE id = ?", (new_date, todo_id))
        db.commit()
        return redirect(url_for("day_view", day=new_date))
    return redirect(url_for("day_view", day=old_date))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
