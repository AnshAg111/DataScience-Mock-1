import time 

def timer(func):
    def time_taken():
        start=time.time()
        func()
        end=time.time()
        print("execution time: ", end-start)
    return time_taken()

@timer
def my_function():
    print(4+6)
    time.sleep(2)

my_function()