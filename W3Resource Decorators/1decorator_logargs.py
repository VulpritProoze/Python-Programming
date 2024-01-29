'''
1. Write a Python program to create a decorator that logs the
arguments and return value of a function
'''

#   My attempt
def log_args(func):
    def log_args_wrapper(*args, **kwargs):
        args_passed_in_func = [repr(a) for a in args]
        kwargs_passed_in_func = [f"{k}={v!r}" for k, v in kwargs.items()]
        formatted_arguments = ", ".join(args_passed_in_func + kwargs_passed_in_func)
        
        return_value = repr(func(*args, **kwargs))
        print("Arguments:", formatted_arguments)
        print("Return value:", return_value)
    return log_args_wrapper

@log_args 
def bar_func(a, b, c):
    print(f"a + b + c = {a+b+c}")
    
bar_func(12, 24, 48)