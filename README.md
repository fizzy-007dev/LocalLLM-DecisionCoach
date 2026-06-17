# AI Decision Coach

AI Decision Coach is a role-based decision assistant that helps users make practical choices by analyzing a problem from the perspective of a student, teacher, manager, developer, or designer.

The project uses a Flask backend, a responsive HTML/CSS/JavaScript frontend, and a local Ollama model. It does not require a paid API key.

## Features

- Role-based decision generation
- Supports student, teacher, manager, developer, and designer roles
- Accepts user problem, constraints, and decision priority
- Gives structured output with recommendation, reasons, pros, risks, alternatives, and action plan
- Uses local AI through Ollama
- No paid API key required
- Modern responsive user interface
- Copy-to-clipboard output button
- Switching hero taglines for a modern app feel

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| AI Model Runtime | Ollama |
| Default Model | gemma:2b |

## Folder Structure

```text
ai-decision-coach/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── LICENSE
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── docs/
    └── project-report.md
```

## How It Works

1. The user selects a role.
2. The user enters a decision problem.
3. The user adds constraints and priority.
4. Flask receives the input from the frontend.
5. Flask builds a role-specific prompt.
6. The prompt is sent to Ollama.
7. Ollama generates a structured decision.
8. The result is displayed on the webpage.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-decision-coach.git
cd ai-decision-coach
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from the official Ollama website.

### 5. Pull the AI model

```bash
ollama pull gemma:2b
```

### 6. Start Ollama

```bash
ollama serve
```

Keep this terminal running.

### 7. Create environment file

Copy `.env.example` and rename it to `.env`:

```bash
cp .env.example .env
```

For Windows PowerShell:

```powershell
copy .env.example .env
```

### 8. Run the Flask app

Open another terminal and run:

```bash
python app.py
```

Now open:

```text
http://127.0.0.1:5000
```

## Sample Input

Role: Developer

Problem:

```text
Should I use Flask or Node.js for my beginner full-stack project?
```

Constraints:

```text
I have 2 days, I know basic Python, and I want to finish fast without paid APIs.
```

Priority:

```text
Speed
```

## Sample Output Format

```text
1. Recommended Decision
2. Why This Fits the Role
3. Pros
4. Risks / Cons
5. Alternatives
6. Final Action Plan
```

## Future Improvements

- Add user login
- Save previous decisions
- Add database support
- Add PDF export
- Add dark mode
- Add more roles
- Add comparison mode for two choices
- Add RAG using local project documents

## GitHub Upload Steps

```bash
git init
git add .
git commit -m "Initial commit: AI Decision Coach"
git branch -M main
git remote add origin https://github.com/your-username/ai-decision-coach.git
git push -u origin main
```

## Team Collaboration Workflow

For a small team, collaborators can clone the main repository, create their own branch, push changes, and open a pull request.

Recommended workflow:

```bash
git clone https://github.com/your-username/ai-decision-coach.git
cd ai-decision-coach
git checkout -b feature/frontend-ui
```

After editing:

```bash
git add .
git commit -m "Improve frontend UI"
git push origin feature/frontend-ui
```

Then open a pull request on GitHub.

## License

This project is licensed under the MIT License.
