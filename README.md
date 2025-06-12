# *PassGuard* - Password Strength Analyzer

**PassGuard** is a privacy-focused web app that instantly evaluates password strength using entropy calculations, real-time feedback, and interactive visuals. It’s designed to help users create more secure passwords and understand how strong their passwords really are.

## Project Objectives

- Analyze password strength using entropy and character variety  
- Estimate real-world time to crack passwords using brute-force methods  
- Provide real-time visual feedback and security tips  
- Display password composition breakdown (uppercase, lowercase, numbers, symbols)  
- Offer MFA readiness checks and improvement suggestions  

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **Security Logic**: Regex, entropy calculation, crack time estimation  
- **Password Scoring**: Based on character sets, patterns, substitutions, and length  

## Key Features

- **Live Password Strength Meter**  
  Real-time evaluation and color-coded strength meter based on entropy and best practices

- **Entropy & Crack Time Estimation**  
  Estimates how long a password might take to crack via brute-force attacks

- **MFA Readiness Check**  
  Alerts users whether their password is strong enough to pair with multi-factor authentication

- **Smart Suggestions & Feedback**  
  Suggests what to improve — length, symbol usage, common patterns — as users type

- **Password Composition Visualizer**  
  Shows percentage breakdown of lowercase, uppercase, numbers, and symbols used

- **Security Tips Included**  
  Practical advice on how to create stronger, more resilient passwords

## How It Works

1. User enters a password  
2. Frontend sends the password to the Flask backend via AJAX (`/analyze`)  
3. The backend:
   - Calculates entropy  
   - Estimates crack time  
   - Analyzes composition, patterns, and common weaknesses  
4. Results are returned and dynamically visualized on the frontend  

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sudarshan007AS/password-strength-analyzer.git
cd password-strength-analyzer
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
password-strength-analyzer/
│
├── app.py                  # Flask app entry point
├── password_utils.py       # Entropy and analysis logic
├── requirements.txt        # Project dependencies
├── templates/
│   └── index.html          # Main frontend interface
└── static/
    └── style.css           # Styling for the frontend
```

## Future Improvements

- Add dark mode toggle  
- Export password strength reports as PDF  
- Integration with password managers  
- Mobile responsiveness enhancements  
- Support for more advanced entropy models (zxcvbn, etc.)

## 👤 Author

**Sudarshan A S**  
[LinkedIn](https://www.linkedin.com/in/sudarshanas) • [GitHub](https://github.com/Sudarshan007AS)

---
