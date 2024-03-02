import json 
from PERT.task import Task


class TaskEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Task):
            o = o.__dict__
            o["predecessor"] = list(o["predecessor"])
            o["_followers"] = list(o["_followers"])
            return o
        
        return super().default(o)