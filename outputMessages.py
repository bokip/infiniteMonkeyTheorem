def error(message):
    print(f"\033[91m[ ERROR ]\033[0m {message}")
    quit()
def info(message):
    print(f"\033[94m[ INFO ]\033[0m {message}")
def warning(message):
    print(f"\033[33m[ WARN ]\033[0m {message}") #done
def ok(message):
    print(f"\033[92m[  OK  ]\033[0m {message}") #done
def help():
    print("""      _    _      _         __  __                  
     | |  | |    | |       |  \/  |                 
     | |__| | ___| |_ __   | \  / | ___ _ __  _   _ 
     |  __  |/ _ \ | '_ \  | |\/| |/ _ \ '_ \| | | |
     | |  | |  __/ | |_) | | |  | |  __/ | | | |_| |
     |_|  |_|\___|_| .__/  |_|  |_|\___|_| |_|\__,_|
                   | |                              
                   |_|                              
    -t <text> - used to find <text> by generating infinitely random string
    -a <width> <height> <numberOfArts> - generates <numberOfArts> arts with <width> width and <height> height
    """)
