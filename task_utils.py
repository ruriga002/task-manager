from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):

    # Validate title
    if not validate_task_title(title):
        return

    # Validate description
    if not validate_task_description(description):
        return

    # Validate due date
    if not validate_due_date(due_date):
        return

    # Create task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    # Add task to list
    tasks.append(task)
    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):

    # Check if index is valid
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):

    pending_tasks = []

    # Find unfinished tasks
    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)

    # Display pending tasks
    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(pending_tasks):
            print(
                f"{i + 1}. {task['title']} - "
                f"{task['description']} "
                f"(Due: {task['due_date']})"
            )


# Implement calculate_progress function
def calculate_progress(tasks=tasks):

    # Avoid division by zero
    if len(tasks) == 0:
        progress = 0
    else:
        completed_tasks = 0

        for task in tasks:
            if task["completed"]:
                completed_tasks += 1

        progress = (completed_tasks / len(tasks)) * 100

    return progress