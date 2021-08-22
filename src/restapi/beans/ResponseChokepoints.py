from json import JSONEncoder


class ResponseChokepoints:

    def __init__(self, status=None, finished=None, result=None):
        self.__status = status
        self.__finished = finished
        self.__result = result

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, finished):
        self.__finished = finished

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result

class ResponseChokepointsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__