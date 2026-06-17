# validation.py

def validate_task_title(title):
    """
    Validate that the task title is not empty.
    """
    if len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    return True


def validate_task_description(description):
    """
    Validate that the task description is not empty.
    """
    if len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False
    return True


def validate_due_date(due_date):
    """
    Validate that the due date is in YYYY-MM-DD format.
    """
    try:
        year, month, day = map(int, due_date.split("-"))

        if len(str(year)) != 4:
            print("Error: Year must have 4 digits.")
            return False

        if month < 1 or month > 12:
            print("Error: Month must be between 1 and 12.")
            return False

        if day < 1 or day > 31:
            print("Error: Day must be between 1 and 31.")
            return False

        return True

    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False