import timeit

number_of_calls = int(input('Enter number of calls:\n'))


def my_decorator(number_of_calls):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            call = 1
            dict_of_call = dict({})
            for i in range(number_of_calls):
                result = func(*args, **kwargs)
                run_time = timeit.Timer().timeit()
                dict_of_call.update({call: run_time})
                call += 1
            return [result, func.__name__], dict_of_call

        return wrapper

    return actual_decorator


@my_decorator(number_of_calls)
def say_hello():
    return 'Hello'


print(say_hello())
