def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Started wrapping')
        result = func(*args, **kwargs)
        print('Wrapped')
        return (result, 'Wrapped')

    return wrapper


@my_decorator
def say_hello(name):
    return f'Hello, {name}'


print(say_hello('Alex'))
