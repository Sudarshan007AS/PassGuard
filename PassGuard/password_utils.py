import math
import re

common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123']

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32
    return len(password) * math.log2(charset) if charset else 0

def estimate_crack_time(entropy):
    # Rough estimation based on entropy (bits)
    # Assuming 10 billion guesses per second (offline attack)
    guesses_per_second = 10_000_000_000
    seconds = 2 ** entropy / guesses_per_second
    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    else:
        years = seconds / 31536000
        return f"{years:.1f} years"

def analyze_password(password):
    entropy = calculate_entropy(password)
    feedback = []
    explanations = []

    if not password:
        return {
            "strength": "Empty",
            "score": 0,
            "feedback": ["Please enter a password."],
            "explanations": [],
            "crack_time": "N/A",
            "mfa_recommendation": False,
            "improvement_steps": []
        }

    # Context-aware suggestions:
    if password.lower() in common_passwords:
        feedback.append("This password is too common and easily guessable.")
        explanations.append("Common passwords are the first ones attackers try.")
    if len(password) < 8:
        feedback.append("Use at least 8 characters.")
        explanations.append("Longer passwords are harder to crack.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Add uppercase letters.")
        explanations.append("Mixing uppercase letters increases complexity.")
    if not re.search(r'[0-9]', password):
        feedback.append("Include numbers.")
        explanations.append("Numbers add extra variety to your password.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Add symbols for extra strength.")
        explanations.append("Symbols make your password more resistant to guessing.")

    # Detect common substitution patterns that don't add real security
    substitutions = {
        '0': 'o',
        '1': 'i',
        '3': 'e',
        '4': 'a',
        '5': 's',
        '@': 'a',
        '$': 's',
        '7': 't'
    }
    weak_subst = any(char in substitutions for char in password.lower())
    if weak_subst:
        feedback.append("Avoid common character substitutions like '3' for 'e' or '$' for 's'; they are predictable.")
        explanations.append("Attackers know these tricks and try them automatically.")

    # Simple entropy thresholds
    if entropy < 28:
        strength = "Very Weak"
        score = 1
    elif entropy < 36:
        strength = "Weak"
        score = 2
    elif entropy < 60:
        strength = "Moderate"
        score = 3
    else:
        strength = "Strong"
        score = 4

    # MFA Readiness: recommend MFA if password strength is less than strong
    mfa_recommendation = score < 4

    # Crack time estimation
    crack_time = estimate_crack_time(entropy)

    # Interactive improvement steps (basic flow)
    improvement_steps = []
    if len(password) < 8:
        improvement_steps.append("Increase password length to 8 or more characters.")
    if not re.search(r'[A-Z]', password):
        improvement_steps.append("Add uppercase letters (A-Z).")
    if not re.search(r'[0-9]', password):
        improvement_steps.append("Include numbers (0-9).")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        improvement_steps.append("Add special symbols (!@#$%, etc.).")

    return {
        "entropy": round(entropy, 2),
        "strength": strength,
        "score": score,
        "feedback": feedback,
        "explanations": explanations,
        "crack_time": crack_time,
        "mfa_recommendation": mfa_recommendation,
        "improvement_steps": improvement_steps
    }
