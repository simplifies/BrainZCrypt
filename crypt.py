def main():
    colorama.init()
    print(Fore.GREEN)
    print("BrainZCrypt Started successfully")
    print(Fore.RESET)
    banner = """\u001b[38;5;240m
                              ____                      
                      __,-~~/~    `---.                 
                    _/_,---(      ,    )                
                __ /        <    /   )  \___            
               ====------------------===;;;==           
                   \/  ~"~"~"~"~"~\~"~)~",1/            
                   (_ (   \  (     >    \)              
                    \_( _ <         >_>'                
\u001b[38;5;202m                       ~ `-i' ::>|--"                   
                           I;|.|.|                      
                          <|i::|i|>                     
\u001b[38;5;220m                           |[::|.|                      
                            ||: |                       \u001b[0m
\u001b[41m───────────────────────────BRAINZCRYPT───────────────────────────\u001b[0m
"""
    print(banner)
    print(Fore.LIGHTRED_EX)
    print("Enter file to crypt: ")
    print(Fore.YELLOW)
    filename = input(str(">>> "))
    with open('key.key', 'r') as file:
        encoded = file.readline()
        f = Fernet(encoded)
    with open(filename, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
        file.close()
    print("File encrypted successfully!")
try:
    import random
    import os
    from cryptography.fernet import Fernet
    import colorama
    from colorama import Fore, Back
    main()
except Exception as e:
    print("Unable to start BrainZCrypt due to:")
    print(e)