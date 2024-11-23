# Password Strength Checker 🔐

A Python-based **Password Strength Checker** that evaluates the strength of passwords based on their **length**, **complexity**, and **uniqueness**. It provides actionable feedback to help users create strong and secure passwords.

---

## Features 🌟

1. **Password Strength Analysis**:
   - Evaluates password length and complexity.
   - Checks for the presence of:
     - Uppercase and lowercase letters.
     - Numbers.
     - Special characters.
   - Penalizes weak patterns like repetitive characters or common passwords.

2. **Feedback System**:
   - Offers clear, actionable advice to strengthen passwords.

3. **Easy to Use**:
   - Simple CLI-based tool that analyzes passwords in real time.

---

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/MokshagnaAnurag/PASSWORD-STRENGTH-CHECKER.git
   cd password-strength-checker
   ```

2. Install Python 3.7+ if not already installed.

3. No additional libraries are required.

---

## Usage 🚀

### Run the Password Strength Checker
1. Open a terminal and navigate to the project folder.
2. Run the program:
   ```bash
   python password_strength_checker.py
   ```

3. Enter a password when prompted, and the program will:
   - Evaluate its strength as **Weak**, **Medium**, or **Strong**.
   - Provide suggestions to improve its strength if needed.

---

## Example Output

### Example 1: Weak Password
#### Input:
```
Enter a password to check: 12345
```

#### Output:
```
Password Strength: Weak

Suggestions to improve your password:
 - Password should be at least 8 characters long.
 - Add at least one uppercase letter.
 - Add at least one lowercase letter.
 - Include at least one special character (e.g., !, @, #).
```

---

### Example 2: Strong Password
#### Input:
```
Enter a password to check: SecurePass123!
```

#### Output:
```
Password Strength: Strong

Great job! Your password is strong.
```

---

## Roadmap 🛣️

- [ ] Add a dictionary of common passwords to flag weak ones.
- [ ] Integrate checks for keyboard patterns (e.g., "asdf1234").
- [ ] Implement a GUI using **Tkinter** or a web-based tool for better usability.
- [ ] Provide a password generator feature for secure password creation.

---

## Contributing 🤝

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer ⚠️

This tool is for educational purposes only. It does not guarantee absolute security but aims to help users understand and create stronger passwords.
