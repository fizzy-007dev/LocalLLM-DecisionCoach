# AI Decision Coach - Project Report

## 1. Project Title

AI Decision Coach

## 2. Problem Statement

People often struggle to make decisions because they do not evaluate the problem from the right perspective. A student may care about time and learning, while a manager may care about budget, risk, and team productivity. Generic AI answers may not always match the user's real role or situation.

This project solves that problem by giving role-specific decision guidance.

## 3. Objective

The objective of AI Decision Coach is to help users make better decisions by analyzing their problem based on selected roles, constraints, and priorities.

## 4. Proposed Solution

The system takes the user's role, decision problem, constraints, and priority as input. It then builds a structured prompt and sends it to a local AI model through Ollama. The AI returns a practical decision with reasons, pros, risks, alternatives, and an action plan.

## 5. System Architecture

```text
User Interface
     ↓
HTML/CSS/JavaScript Frontend
     ↓
Flask Backend
     ↓
Prompt Builder
     ↓
Ollama Local AI Model
     ↓
Structured Decision Output
```

## 6. Modules

### Frontend Module

The frontend contains the form where the user enters their problem and selects role, priority, and constraints.

### Backend Module

The Flask backend receives frontend input, validates it, builds the prompt, and communicates with Ollama.

### AI Module

The AI module uses Ollama with the `gemma:2b` model to generate role-based decision suggestions.

## 7. Key Features

- Role-based decision support
- Local AI model integration
- No paid API dependency
- Structured decision output
- Modern responsive interface
- Copy decision output
- Beginner-friendly setup

## 8. Innovation

The project is different from a normal chatbot because it does not simply answer randomly. It changes its reasoning style based on the selected role. This makes the output more relevant and practical.

## 9. Feasibility

The project is feasible because it uses lightweight technologies such as Flask, HTML, CSS, JavaScript, and Ollama. The `gemma:2b` model can run on many laptops compared to larger models.

## 10. Expected Impact

The project can help students, developers, teachers, managers, and designers make better decisions faster. It can also be extended into a full productivity tool with login, database, decision history, and PDF exports.

## 11. Future Scope

- Add authentication
- Store decisions in a database
- Add dashboard
- Add PDF report export
- Add RAG support using uploaded files
- Add team decision mode
- Add voice input
- Deploy frontend separately
