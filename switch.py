class Switch():

    cases = []

    def add_case(self, test, execute):
        self.cases.append((test, execute))

    def switch(self):
        for case in self.cases:
            if case[0]():
                case[1]()
                break