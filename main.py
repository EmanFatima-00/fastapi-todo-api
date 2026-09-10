from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Ye humari khali to-do list hai
tasks = []
next_id = 1

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

@app.get("/")
def ghar():
    return {"message": "To-Do API chal rahi hai"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def sab_tasks_dikhao():
    return tasks

@app.post("/tasks", status_code=201)
def naya_task_add_karo(task: TaskCreate):
    global next_id
    naya_task = Task(id=next_id, title=task.title)
    tasks.append(naya_task)
    next_id += 1
    return naya_task

@app.put("/tasks/{task_id}")
def task_complete_karo(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    raise HTTPException(status_code=404, detail="Task nahi mila")

@app.delete("/tasks/{task_id}", status_code=204)
def task_delete_karo(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return