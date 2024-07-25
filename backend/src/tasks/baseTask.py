import abc


class BaseTask(abc.ABC):

    @abc.abstractmethod
    def setup(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError()
