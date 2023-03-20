class Browser:
    def __init__(self):
        self.history = []
        self.future = []

    def go(self, url):
        self.history.append(url)
        self.future.clear()

    def back(self):
        if len(self.history) > 1:
            self.future.append(self.history.pop())
            return self.history[-1]
        else:
            return self.history[0]

    def forward(self):
        if self.future:
            self.history.append(self.future.pop())
            return self.history[-1]
        else:
            return self.history[-1]

    def printAll(self):
        for url in self.history:
            print(url)

