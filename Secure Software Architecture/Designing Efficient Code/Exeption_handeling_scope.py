def process_data(a, b):
    try:
         print( a / b)
    except ZeroDivisionError:
        print("Error: division by zero is not allowed")
        return None
    except TypeError:
        print("Error: both inputs must support division (e.g., numbers)")
        return None
    finally:
        print("Function execution finished")
    
a = int(input("Number 1: "))
b = int(input("Number 2: "))

process_data(a, b)