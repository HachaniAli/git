class family:

    def __init__(self, prenom, age, gendre, location):
        self.prenom = prenom
        self.age = age
        self.gendre = gendre
        self.location = location

    def sleep(self):
        print(f"{self.prenom} is Sleeping")