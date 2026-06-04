from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "decision-coach"

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
OLLAMA_MODEL = "gemma:2b"


def call_ollama(messages):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"].strip()


def build_system_prompt():
    return """
You are an AI Decision Coach.

Your job is to help users make practical decisions tailored to their selected role.

The supported roles can include:
- Student
- Teacher
- Manager
- Developer
- Designer
- Entrepreneur
- Researcher
- Other

Always think carefully and adapt your reasoning to the user's role, priorities, and constraints.

For the main decision analysis, respond in this exact structured format:

1. Recommended Decision
- Give the best suggested decision clearly.

2. Why? (Based on Role)
- Explain why this decision fits the user's selected role.
- Mention relevant role-based thinking.

3. Risks (Pros and Cons)
Pros:
- ...
- ...

Cons:
- ...
- ...

4. Alternatives
- Alternative 1: ...
- Alternative 2: ...
- Alternative 3: ...

5. Action Plan
- Step 1: ...
- Step 2: ...
- Step 3: ...

Rules:
- Be practical, clear, and supportive.
- Do not be vague.
- Keep formatting neat and readable.
- For follow-up scenario questions, recalculate based on the previous context and the new scenario.
- If the user changes assumptions, compare the new answer with the old one.
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form.get("role", "").strip()
        custom_role = request.form.get("custom_role", "").strip()
        problem = request.form.get("problem", "").strip()
        constraints = request.form.get("constraints", "").strip()
        priority = request.form.get("priority", "").strip()

        if role == "Other" and custom_role:
            final_role = custom_role
        else:
            final_role = role

        if not final_role or not problem:
            return render_template(
                "index.html",
                error="Please select a role and enter the problem statement."
            )

        user_prompt = f"""
User Role: {final_role}
Problem Statement: {problem}
Constraints: {constraints if constraints else "None provided"}
Priority: {priority if priority else "Balanced"}

Please analyze this decision and provide a structured recommendation tailored to the user's role.
"""

        messages = [
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_prompt}
        ]

        try:
            result = call_ollama(messages)
        except Exception as e:
            result = (
                "Unable to reach Ollama right now.\n\n"
                f"Technical error: {str(e)}\n\n"
                "Please make sure Ollama is running and gemma:2b is available."
            )

        session["decision_context"] = {
            "role": final_role,
            "problem": problem,
            "constraints": constraints,
            "priority": priority
        }

        session["chat_messages"] = messages + [{"role": "assistant", "content": result}]
        session["initial_result"] = result
        session["followups"] = []

        return redirect(url_for("result_page"))

    return render_template("index.html", error=None)


@app.route("/result", methods=["GET"])
def result_page():
    initial_result = session.get("initial_result")
    context = session.get("decision_context")
    followups = session.get("followups", [])

    if not initial_result or not context:
        return redirect(url_for("index"))

    return render_template(
        "exit.html",
        context=context,
        initial_result=initial_result,
        followups=followups
    )


@app.route("/followup", methods=["POST"])
def followup():
    question = request.form.get("question", "").strip()

    if not question:
        return redirect(url_for("result_page"))

    context = session.get("decision_context")
    chat_messages = session.get("chat_messages", [])
    followups = session.get("followups", [])

    if not context or not chat_messages:
        return redirect(url_for("index"))

    followup_prompt = f"""
This is a follow-up scenario question from the user.

Original Role: {context['role']}
Original Problem: {context['problem']}
Original Constraints: {context['constraints'] if context['constraints'] else "None provided"}
Original Priority: {context['priority'] if context['priority'] else "Balanced"}

User's new scenario / follow-up question:
{question}

Please recalculate the advice based on the original context plus this new question.
Keep the answer structured and easy to read.
"""

    chat_messages.append({"role": "user", "content": followup_prompt})

    try:
        answer = call_ollama(chat_messages)
    except Exception as e:
        answer = (
            "Unable to process the follow-up question right now.\n\n"
            f"Technical error: {str(e)}"
        )

    chat_messages.append({"role": "assistant", "content": answer})
    followups.append({"question": question, "answer": answer})

    session["chat_messages"] = chat_messages
    session["followups"] = followups

    return redirect(url_for("result_page"))


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)