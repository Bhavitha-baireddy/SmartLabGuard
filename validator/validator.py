import ast


def validate_submission(code):
    result = {
        "syntax": False,
        "tests": False,
        "quality": False,
        "message": ""
    }

    # Syntax check
    try:
        ast.parse(code)
        result["syntax"] = True
    except SyntaxError:
        result["message"] = "Python syntax error found."
        return result

    # Empty submission check
    if not code.strip():
        result["message"] = "Submission is empty."
        return result

    # Basic quality check
    if len(code) > 10000:
        result["message"] = "Submission is too large."
        return result

    result["quality"] = True

    # Function check
    if "def " in code:
        result["tests"] = True
    else:
        result["message"] = "No Python function found."
        return result

    result["message"] = "Submission passed all validation checks."

    return result