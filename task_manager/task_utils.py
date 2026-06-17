from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title")
        return

    if not validate_task_description(description):
        print("Invalid description")
        return

    if not validate_due_date(due_date):
        print("Invalid date")
        return

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


def mark_task_as_complete(tasks, task_index):
    if len(tasks) == 0:
        print("No tasks available")
        return

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")


def view_pending_tasks(tasks):
    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for task in pending:
        print(task["title"])


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100