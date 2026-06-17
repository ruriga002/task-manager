def validate_task_title(title):
    if len(title.strip()) == 0:
        return False
    return True


def validate_task_description(description):
    if len(description.strip()) == 0:
        return False
    return True


def validate_due_date(due_date):
    try:
        parts = due_date.split("-")
        if len(parts) != 3:
            return False

        year, month, day = map(int, parts)

        if len(str(year)) != 4:
            return False

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        return True

    except ValueError:
        return False