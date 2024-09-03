from .baseTask import BaseTask


class HelloWorldTask(BaseTask):
    def setup(self): ...

    def run(self):
        print("hello world")
