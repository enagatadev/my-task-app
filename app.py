import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tasks": [], "next_id": 1}


def save_tasks(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


data = load_tasks()
tasks = data["tasks"]
next_id = data["next_id"]


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("title", "").strip()
    deadline = request.form.get("deadline", "").strip()
    priority = request.form.get("priority", "中")
    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "deadline": deadline,
            "priority": priority,
        })
        next_id += 1
        save_tasks({"tasks": tasks, "next_id": next_id})
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    global tasks
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    save_tasks({"tasks": tasks, "next_id": next_id})
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
