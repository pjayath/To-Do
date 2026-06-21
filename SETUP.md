# Setup Guide

Detailed setup instructions for running the To-Do app on your computer.

## Windows (Recommended)

### Option 1: One-Click Launcher (Easiest)

1. Navigate to `C:\Pramodh\AI\To-Do` in File Explorer
2. Double-click `start.bat`
3. A terminal window will open and your browser should automatically open to `http://127.0.0.1:5000`
4. If the browser doesn't open, manually type `http://127.0.0.1:5000` in your address bar
5. To stop the app, close the terminal window or press `Ctrl+C` inside it

**The `start.bat` file:**
```batch
@echo off
cd /d "%~dp0"
start "" http://127.0.0.1:5000
venv\Scripts\python app.py
```

This batch file automatically:
- Changes to the app directory
- Opens your browser to the app URL
- Runs the Python app server

### Option 2: Manual Terminal

1. Open PowerShell or Command Prompt
2. Navigate to the app folder:
   ```bash
   cd C:\Pramodh\AI\To-Do
   ```
3. Run the app:
   ```bash
   venv\Scripts\python app.py
   ```
4. You should see:
   ```
   * Running on http://127.0.0.1:5000
   ```
5. Open your browser to `http://127.0.0.1:5000`
6. To stop, press `Ctrl+C` in the terminal

## Mac / Linux

1. Open Terminal
2. Navigate to the app folder:
   ```bash
   cd /path/to/To-Do
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser to `http://127.0.0.1:5000`
6. To stop, press `Ctrl+C` in the terminal

## First Time Setup (If Virtual Environment Doesn't Exist)

If `venv` folder is missing, create it:

### Windows
```bash
cd C:\Pramodh\AI\To-Do
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Mac / Linux
```bash
cd /path/to/To-Do
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Keeping the App Running Daily

### Windows: Add to Startup (Optional)

To have the app start automatically when you log in:

1. Create a shortcut to `start.bat`:
   - Right-click `start.bat` → **Send to** → **Desktop (create shortcut)**
   
2. Move shortcut to Startup folder:
   - Press `Win+R`, type `shell:startup`, press Enter
   - Drag the shortcut into this folder

3. Next time you log in, the app will start automatically

### Windows: Minimize to Taskbar

After running `start.bat`, the terminal window appears. You can:
- Click the **minimize button** to hide it (it stays running in the taskbar)
- Click it in the taskbar to bring it back
- Close it when you're done using the app

## Troubleshooting

### "Port 5000 already in use"
Another app is using port 5000. Either:
- Close the other app first, then restart this app
- Change the port in `app.py`:
  ```python
  if __name__ == "__main__":
      app.run(debug=True, port=5050)  # Change 5000 to 5050
  ```
  Then access the app at `http://127.0.0.1:5050`

### "venv not found" or "python command not found"
- Make sure Python 3.7+ is installed: `python --version`
- If not installed, download from https://www.python.org/
- Create the virtual environment (see "First Time Setup" section above)

### "Database is corrupted"
- Stop the app
- Delete the `todo.db` file in the app folder
- Restart the app — it will create a fresh database

### "Changes aren't showing"
- Stop the app (Ctrl+C)
- Restart it
- Hard-refresh your browser (Ctrl+Shift+R or Ctrl+F5)

### "Browser doesn't open automatically"
- `start.bat` should open it, but if it doesn't:
  - Manually type `http://127.0.0.1:5000` in your browser address bar
  - Make sure the terminal shows "Running on http://127.0.0.1:5000"

## Next Steps

- Read [FEATURES.md](FEATURES.md) to learn how to use each feature
- Check [README.md](README.md) for technical details
- To customize or extend the app, see the Project Structure section in README.md
