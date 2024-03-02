import uvicorn
import json

from PERT import PERT
from fastapi import FastAPI
from Encoders import TaskEncoder


app = FastAPI()
pert = PERT.getInstance(csv_write=True, csv_read=True)


@app.get("/add_task/{task_name}")
async def add_task(task_name: str, predecessor: str, optimistic: str, nominal: str, pessimistic: str):
    pert.add_data(task_name, predecessor, optimistic, nominal, pessimistic)
    task = pert.print_data(task_name)

    return json.dumps(task, cls=TaskEncoder)


@app.get("/del_task/{task_name}")
async def del_task(task_name: str):
    pert.del_data(task_name)

    return json.dumps(pert.show_data(), cls=TaskEncoder)


@app.get("/get_task/{task_name}")
async def get_task(task_name: str):
    task = pert.print_data(task_name)
    
    return json.dumps(task, cls=TaskEncoder)


@app.get("/show_tasks")
async def show_tasks():
    return json.dumps(pert.show_data(), cls=TaskEncoder)


@app.get("/summarize")
async def summarize():
    return json.dumps(pert.summarize())


if __name__ == "__main__":
    uvicorn.run("API:app", port=5000, log_level="info", reload=True)