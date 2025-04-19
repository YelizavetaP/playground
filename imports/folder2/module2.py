from config import MAX_RETRIES, DATABASE

def hello_from_folder2():
    print(f"Hello from folder2's module2!")
    print(f"Max retries: {MAX_RETRIES}")
    print(f"Database connection: {DATABASE['host']}:{DATABASE['port']}") 


def hello_from_folder2_to_f1():
    print(f"----Hello from folder2's module2 to f1 m1!")
    print(f"Max retries: {MAX_RETRIES + 10} ")

