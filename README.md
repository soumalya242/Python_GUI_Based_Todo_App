# 📝 To-Do List App

A simple desktop To-Do List application built with **Python** and **Tkinter**, with task data saved locally in a JSON file so your tasks persist between sessions.

## Features

- ➕ Add new tasks (via button click or pressing **Enter**)
- ✅ Mark tasks as complete
- 🗑️ Delete individual tasks
- 🧹 Clear all tasks
- 💾 Automatic saving/loading using a local `task.json` file


## Tech Stack

- **Language:** Python 3
- **GUI Library:** Tkinter (built into Python)
- **Data Storage:** JSON (`task.json`)

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Running the App
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```
2. Run the app:
   ```bash
   python Todo-app.py
   ```

### Building a Standalone .exe (Windows)
This app can be packaged into a standalone executable using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name TodoApp Todo-app.py
```
The executable will be created in the `dist/` folder.

## How It Works

- Tasks are stored as a list of dictionaries, e.g. `{"task": "Buy milk", "done": False}`
- On every add/complete/delete/clear action, the task list is saved to `task.json`
- On startup, the app loads existing tasks from `task.json` (if the file exists) and displays them

