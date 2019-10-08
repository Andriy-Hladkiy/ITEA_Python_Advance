class SingletoneExample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            return cls._instance
        raise Exception('Instance already exists')

    def __init__(self):
        self._x = 10
        self._y = 200


a = SingletoneExample()
b = SingletoneExample()

a._x = 100

print(a._x)
print(b._x)
