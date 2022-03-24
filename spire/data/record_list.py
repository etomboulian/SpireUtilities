
from collections import UserList

class RecordList(UserList):
    def __init__(self):
        super().__init__()

    def first(self):
        return self.data[0]

    def one(self):
        if len(self.data) > 1:
            raise Exception("One() called but more than one record was returned")
        elif len(self.data) == 0:
            raise Exception("One() called but there were no records returned")
        else:
            return self.data[0]
    