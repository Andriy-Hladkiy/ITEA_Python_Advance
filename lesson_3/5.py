
def decorator(num_of_repeats=1):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print('Started wrapping')
            for i in range(num_of_repeats):
                result = func(*args, **kwargs)

            print('wrapped')
            return (result, 'Wrapped')

        return wrapper
    return actual_decorator


@decorator(10)
def say_hello(name):
    return f'Hello, {name}'


print(say_hello('Alex'))
