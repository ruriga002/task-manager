# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Add task
def add_task(title, description, due_date):

    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Mark task complete (FIXED INDEXING)
def mark_task_as_complete(index):

    if not isinstance(index, int):
        print("Invalid input. Please enter a number.")
        return

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")


# View pending tasks
def view_pending_tasks():

    pending_tasks = [task for task in tasks if not task["completed"]]

    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(pending_tasks):
            print(
                f"{i}. {task['title']} - "
                f"{task['description']} "
                f"(Due: {task['due_date']})"
            )


# Calculate progress
def calculate_progress():

    if len(tasks) == 0:
        return 0

    completed_tasks = sum(1 for task in tasks if task["completed"])
    return (completed_tasks / len(tasks)) * 100