# Fixed: instance methods receive the object as their first parameter.
class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
