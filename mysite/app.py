class person:
    def __init__(self, name):
        self.yourname = name

    def func(self):
        print("Hey ! My name is " + self.yourname)

pe = person("Alex")
pe.func()