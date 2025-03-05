# src/homework/c_decisions/decisions.py

def get_options_ratio(option, total):
    """Returns the ratio of option to total."""
    if total == 0:  # Prevent division by zero
        return 0
    return option / total

def get_faculty_rating(ratio):
    """Returns the faculty rating based on the ratio."""
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"
