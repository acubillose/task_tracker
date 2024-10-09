```markdown
# Task Tracker CLI https://roadmap.sh/projects/task-tracker

Task Tracker CLI is a simple command-line interface application that allows you to manage your tasks efficiently. This project helps you track your tasks, mark their status, and store them in a JSON file.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as "in-progress" or "done"
- List all tasks
- Filter tasks by status: "todo", "in-progress", or "done"
- Store tasks persistently in a JSON file

## Requirements

- Python 3.x
- No external libraries are required.

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/task-tracker-cli.git
cd task-tracker-cli
```

### 2. Create a virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Run the CLI

You can run the CLI commands by executing the `task_tracker.py` file:

```bash
python task_tracker.py [command] [arguments]
```

## Commands

### Add a Task
```bash
python task_tracker.py add "Task description"
```
Adds a new task with a unique ID.

### List All Tasks
```bash
python task_tracker.py list
```
Lists all tasks.

### List Tasks by Status
```bash
python task_tracker.py list [status]
```
- `todo`: Lists all tasks that are pending.
- `in-progress`: Lists all tasks that are in progress.
- `done`: Lists all tasks that are marked as done.

### Mark a Task as "In Progress"
```bash
python task_tracker.py mark-in-progress [task_id]
```
Marks a task as "in-progress" based on the task's ID.

### Mark a Task as "Done"
```bash
python task_tracker.py mark-done [task_id]
```
Marks a task as "done" based on the task's ID.

### Update a Task
```bash
python task_tracker.py update [task_id] "New description"
```
Updates the task's description by providing the task ID and the new description.

### Delete a Task
```bash
python task_tracker.py delete [task_id]
```
Deletes a task by providing the task ID.

## Task Properties

Each task contains the following properties:

- **id**: Unique identifier for the task.
- **description**: A brief description of the task.
- **status**: The current status of the task (`todo`, `in-progress`, or `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## File Storage

Tasks are stored in a JSON file named `tasks.json` located in the same directory as the CLI application. If this file does not exist, it will be created automatically when you add your first task.

## Example Usage

### Adding a Task
```bash
python task_tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Listing All Tasks
```bash
python task_tracker.py list
# Output: 
# 1. Buy groceries - todo
```

### Marking a Task as Done
```bash
python task_tracker.py mark-done 1
# Output: Task 1 marked as done.
```

### Deleting a Task
```bash
python task_tracker.py delete 1
# Output: Task 1 deleted.
```

## Contributing

Feel free to contribute by forking this repository, making changes, and submitting a pull request.
