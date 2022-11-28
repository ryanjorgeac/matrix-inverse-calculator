class Maybe:
    def map(self, function):
        raise NotImplementedError()

    def orElseThrow(self, exception):
        raise NotImplementedError()


class just(Maybe):
    def __init__(self, value):
        self.value = value

    def map(self, function):
        return just(function(self.value))

    def orElseThrow(self, exception):
        return self.value


class nothing(Maybe):
    def map(self, function):
        return self

    def orElseThrow(self, exception):
        raise exception