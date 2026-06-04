from datetime import datetime

def validate_task_title(title):
    # Check if title is empty
    if len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    
    return True


def validate_task_description(description):
    # Check if description is empty
    if len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False
    
    return True    


def validate_due_date(due_date):
    try:
        # Check if date follows YYYY-MM-DD format
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    
    except ValueError:
        print("Error: Invalid due date. Please use YYYY-MM-DD format.")
        return False