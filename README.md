# To-Do App

A simple, elegant calendar-based to-do list built with Flask and SQLite.

## Features

- **Monthly calendar view** — Navigate between months to see your tasks at a glance
- **Date-based planning** — Add to-dos to specific dates (past, present, future)
- **Time tracking** — Assign a time to each to-do and they sort in ascending order
- **Task completion** — Mark to-dos complete with a square checkbox (filled when done)
- **Reschedule** — Move a to-do to a different date using the inline date picker
- **Quick stats** — Calendar shows a badge per day (e.g., `2/3` = 2 of 3 tasks done)
- **Gradient UI** — Clean, modern design with a purple-to-pink gradient background

## Quick Start

### Prerequisites
- Python 3.7+
- Windows, Mac, or Linux

### Installation & Running

1. **Clone or open the repository**
   ```bash
   cd C:\Pramodh\AI\To-Do
   ```

2. **Run the one-click launcher** (Windows only)
   - Double-click `start.bat` in the folder
   - Browser will open automatically to `http://127.0.0.1:5000`

3. **Or start manually**
   ```bash
   venv\Scripts\python app.py
   ```
   Then open your browser to `http://127.0.0.1:5000`

### Using the App

- **View calendar** — See the current month with task counts per day
- **Navigate months** — Click `←` and `→` to move between months
- **Add a to-do** — Click a date → type task name → set time (optional) → click **Add**
- **Mark complete** — Click the square checkbox next to a task
- **Reschedule** — Change the date field and click **Move** to move it to another day
- **Delete** — Click **✕** to remove a task
- **Go to today** — Click the "Go to today" link to jump back to the current date

## Project Structure

```
C:\Pramodh\AI\To-Do/
├── app.py                 # Flask app, routes, database logic
├── requirements.txt       # Python dependencies (Flask)
├── start.bat             # One-click launcher (Windows)
├── README.md             # This file
├── templates/
│   ├── calendar.html     # Month grid view
│   └── day.html          # Day view with task list
├── static/
│   └── style.css         # Styling (gradient, calendar grid, checkbox)
├── venv/                 # Python virtual environment
└── todo.db              # SQLite database (created on first run)
```

## Technical Details

### Stack
- **Backend:** Flask (Python web framework)
- **Database:** SQLite (lightweight, file-based)
- **Frontend:** HTML, CSS, vanilla JavaScript (no build tools)

### Database Schema
```sql
CREATE TABLE todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER (0/1),
  date TEXT (YYYY-MM-DD),
  time TEXT (HH:MM)
)
```

### Key Routes
- `GET /` — Redirects to current month calendar
- `GET /calendar/<year>/<month>` — Month grid view
- `GET /day/<date>` — Day view with task list for that date
- `POST /add` — Create a new to-do
- `POST /toggle/<id>` — Mark complete/incomplete
- `POST /delete/<id>` — Remove a to-do
- `POST /reschedule/<id>` — Move a to-do to a different date

## Development

### Install dependencies manually
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Run in debug mode
```bash
venv\Scripts\python app.py
```

### Making changes
- Edit `app.py` for routes/logic
- Edit `templates/*.html` for UI structure
- Edit `static/style.css` for styling
- The app auto-reloads on file changes (debug mode)

## Future Ideas

- User authentication (login/multiple users)
- Recurring tasks
- Task categories/tags
- Export to CSV/iCal
- Mobile-responsive design improvements
- Dark mode

## Troubleshooting

**Port 5000 already in use?**
- Another app is using port 5000
- Close other apps or modify `app.run(port=5000)` in `app.py` to a different port (e.g., 5050)

**Database corruption?**
- Delete `todo.db` and restart the app — it will create a fresh database

**Changes not showing?**
- Stop the app (Ctrl+C) and restart
- Hard-refresh your browser (Ctrl+Shift+R)

## Contributing

Feel free to fork, modify, and submit improvements!

## License

Open source — feel free to use, modify, and share.
