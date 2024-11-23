import re

def password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 8:
        score += 2
    elif 6 <= len(password) < 8:
        score += 1
        feedback.append("Password should be at least 8 characters long.")
    else:
        feedback.append("Password is too short. Consider making it longer.")


    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")


    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")


    if any(char in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~" for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #).")


    if re.search(r'(.)\1\1', password):  
        score -= 1
        feedback.append("Avoid repeating characters three or more times.")
    if password.lower() in ["password", "123456", "qwerty", "abc123"]:
        score = 0
        feedback.append("Your password is too common. Choose something unique.")


    if score >= 6:
        strength = "Strong"
    elif 4 <= score < 6:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback



if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    user_password = input("Enter a password to check: ").strip()
    
    strength, suggestions = password_strength(user_password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print(f" - {suggestion}")
    else:
        print("Great job! Your password is strong.")
