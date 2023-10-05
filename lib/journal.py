class Journal():
    def __init__(self, name, string_checker):
        self.name = name
        self.string_checker = string_checker
        self.notebook = []

    def add(self, entry):
        punctuation = self.string_checker.has_punctuation(entry)
        if punctuation == False:
            raise Exception('Please add punctuation!')
            
            