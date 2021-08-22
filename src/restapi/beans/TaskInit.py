

class TaskInit:

    def __init__(self, task_id):
        self.task_id = task_id

    @property
    def task_id_attr(self):
        return self.task_id

    @task_id_attr.setter
    def task_id_attr(self, task_id):
        self.task_id = task_id