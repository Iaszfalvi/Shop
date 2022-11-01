class Letters(object):

    def __init__(self):
        self.myList = []

    def put(self, value):
        self.myList.append(value)

    def getValues(self):
        return self.myList