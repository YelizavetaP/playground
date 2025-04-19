from config import APP_NAME, VERSION, DEBUG_MODE

from folder2 import hello_from_folder2_to_f1

def hello_from_folder1():
    print(f"Hello from folder1's module1!")
    print(f"App: {APP_NAME} v{VERSION}")
    print(f"Debug mode: {'enabled' if DEBUG_MODE else 'disabled'}") 
    print('-'*50)
    hello_from_folder2_to_f1()


