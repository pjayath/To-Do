# Development Summary

How this To-Do app was built, step-by-step.

## Project Overview

This is a web-based calendar and task management app built with:
- **Python + Flask** for the backend
- **SQLite** for data storage
- **HTML/CSS** for the frontend (no frameworks)
- Simple, clean, and easy to modify

Built in June 2026 by Claude Code (AI assistant) with user input on features.

## Build Timeline & Releases

### PR #1: Initial README
- Added a basic project README
- Set up GitHub repository structure
- **Status:** Merged to main

### PR #2: Core Flask App with Calendar
- Implemented Flask backend with SQLite database
- Created month-grid calendar view
- Added day-view for task management
- Features: add, complete (toggle), delete to-dos
- Added gradient styling (purple → pink background)
- **Improvements:** Fixed Windows-specific date formatting bug (strftime `%-d` not portable)
- **Status:** Merged to main

### PR #3: Time Field & Sorting
- Added time field to each to-do
- Tasks now sort in ascending date/time order
- Restyled checkbox from circle to square (purple fill when checked)
- Updated UI to show time next to each task
- **Improvements:** Portable date formatting, robust migration for existing databases
- **Status:** Merged to main

### PR #4: Documentation (Current)
- Comprehensive README with feature overview
- SETUP.md with installation & troubleshooting
- FEATURES.md with detailed usage walkthrough
- DEVELOPMENT.md (this file) with build history
- **Purpose:** Help other developers understand and extend the codebase

## Architecture

### Backend (app.py)

**Core Functions:**
- `get_db()` — Database connection management
- `init_db()` — Initialize SQLite schema on startup
- `month_view(year, month)` — Render calendar grid
- `day_view(day)` — Show tasks for a specific date
- `add()` — Create new to-do
- `toggle(todo_id)` — Mark complete/incomplete
- `delete(todo_id)` — Remove to-do
- `reschedule(todo_id)` — Move to different date

**Database Schema:**
```sql
CREATE TABLE todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  date TEXT NOT NULL,
  time TEXT NOT NULL DEFAULT '00:00'
)
```

### Frontend

**Templates:**
- `calendar.html` — Month grid with navigation
- `day.html` — Task list for a single day

**Styling:**
- `style.css` — Gradient background, calendar grid, responsive layout, square checkbox styling

**No JavaScript dependencies** — all interactions are form-based POST requests

### Data Flow

```
User clicks date
    ↓
Browser requests GET /day/<date>
    ↓
Flask queries todos WHERE date = ?
    ↓
Renders day.html with task list
    ↓
User adds task / toggles / moves / deletes
    ↓
Browser POSTs to /add, /toggle, /delete, /reschedule
    ↓
Flask updates database
    ↓
Browser redirects to GET /day/<date>
    ↓
Page refreshes with updated state
```

## Key Design Decisions

### 1. No Build Tools
- Used plain HTML/CSS/Python, no webpack/npm
- Easier for others to understand and modify
- Faster to develop and iterate
- Runs on any system with Python installed

### 2. SQLite Database
- Lightweight, file-based (no separate server)
- Easy to backup (just copy todo.db)
- Perfect for single-user or small teams
- Can migrate to PostgreSQL later if needed

### 3. Form-Based Navigation
- Every action is a POST form submit → redirect
- Simple, no async JavaScript complexity
- Works in any browser, even without JavaScript
- Easy to debug (just look at form data)

### 4. Responsive, Not Mobile-First
- Designed for desktop/laptop use
- Works on tablets but not optimized for mobile yet
- Can be improved with media queries if needed

### 5. One-Click Launcher
- Windows users double-click `start.bat`
- Automatically opens browser + starts server
- Reduces friction for non-technical users

## What Went Well

- **Clean separation of concerns** — app.py handles logic, templates handle UI
- **Minimal dependencies** — just Flask, no heavy frameworks
- **Easy to test locally** — no deployment complexity
- **Gradient styling** — looks modern and polished
- **Square checkbox** — better visual feedback than text
- **Ascending sort** — logical task ordering by time

## Lessons & Improvements

### Bug Fixed
- **Date formatting:** `%-d` in `strftime()` doesn't work on Windows Python
  - Solution: Use `day_date.day` instead of strftime formatting
  - Lesson: Always test on target platform

### Data Migration
- When adding the `time` column, needed to handle existing databases
- Solution: Check if column exists before adding it
- Lesson: Schema changes need migration logic

### Browser Persistence
- User data persists in `todo.db` even after closing the app
- Works across multiple sessions automatically
- Important for daily-use apps

## Future Enhancements

### Short Term
- [ ] Edit existing task (change title without delete + re-add)
- [ ] Keyboard shortcuts (e.g., Ctrl+Shift+N to add new task)
- [ ] Search/filter tasks
- [ ] Task priorities (high/medium/low)
- [ ] Task notes/descriptions

### Medium Term
- [ ] Recurring tasks (daily, weekly, monthly)
- [ ] Categories/tags for tasks
- [ ] Export to CSV or calendar file (iCal)
- [ ] Import from other apps
- [ ] Multi-user support with login

### Long Term
- [ ] Mobile app (React Native or Flutter)
- [ ] Sync across devices (cloud backend)
- [ ] Real-time collaboration
- [ ] AI-powered task suggestions
- [ ] Calendar integration (Google Calendar, Outlook)

## Code Quality

### Strengths
- Simple, readable code
- Clear function/variable names
- Minimal dependencies
- Good separation of templates and logic

### Areas for Improvement
- No unit tests yet (could add with pytest)
- No input validation/sanitization (SQL injection risk if user data isn't escaped — Flask does this by default)
- No error handling for database failures
- No logging

## Deployment Notes

### For Production Use
- Replace `debug=True` with `debug=False`
- Use a production WSGI server (e.g., Gunicorn, uWSGI) instead of Flask's dev server
- Add a database backup strategy
- Set up proper logging
- Add authentication if multi-user
- Use environment variables for config

### Example Production Setup
```bash
pip install gunicorn
gunicorn --workers 4 app:app
```

## How to Extend

### Adding a New Feature

1. **Plan the database schema** — Does the todos table need new columns?
2. **Add the route** — Create a new `@app.route()` in app.py
3. **Update the template** — Modify calendar.html or day.html
4. **Add styling** — Update static/style.css if needed
5. **Test locally** — Run app.py and verify in browser
6. **Create a PR** — Document the feature and changes

### Example: Add Task Priority

1. Add column: `ALTER TABLE todos ADD COLUMN priority TEXT DEFAULT 'normal'`
2. Add form field in day.html: `<select name="priority"><option>low</option>...</select>`
3. Add to insert query in app.py: `INSERT INTO todos (..., priority) VALUES (..., ?)`
4. Sort by priority in day_view: `ORDER BY date ASC, priority ASC, time ASC`
5. Style based on priority in CSS: `.priority-high { color: red; }`

## Version History

- **v1.0** (PR #2) — Core Flask app, calendar, task management
- **v1.1** (PR #3) — Time field, sorting, square checkbox styling
- **v1.2** (PR #4) — Documentation for users and developers

## Getting Help

- Check SETUP.md for installation issues
- Check FEATURES.md for how to use the app
- Check README.md for technical overview
- Read app.py comments for code-level details
- Test changes locally before committing

## Credits

Built by Claude Code (AI) with guidance from the user on feature requests and design preferences.

Questions or ideas? Feel free to fork, modify, and contribute back!
