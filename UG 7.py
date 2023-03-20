class Browser:
    def __init__(self):
        self.history = []
        self.current_url = None
        self.future = []

    def go(self, url):
        self.history.append(url)
        self.current_url = url
        self.future = []

    def back(self):
        if len(self.history) > 1:
            self.future.append(self.history.pop())
            self.current_url = self.history[-1]

    def forward(self):
        if self.future:
            self.history.append(self.future.pop())
            self.current_url = self.history[-1]

    def printAll(self):
        for url in self.history:
            print(url)
