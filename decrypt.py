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
    print("Do you want to decrypt a folder or a file?\n1: File\n2: Folder")
    print(Fore.YELLOW)
    choic = input(str(">>> "))
    if choic == "1":
        print(Fore.LIGHTRED_EX)
        print("Enter full path of file to decrypt: ")
        print(Fore.YELLOW)
        filename = input(str(">>> "))
        with open('key.key', 'r') as file:
            encoded = file.readline()
            f = Fernet(encoded)
        with open(filename, "rb") as file:
                file_data = file.read()
                decrypted_data = f.decrypt(file_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
            file.close()
        print("File decrypted successfully!")
        input("Press enter to continue")
    if choic == "2":
        print(Fore.LIGHTRED_EX)
        print("Enter full path of folder to decrypt: ")
        print(Fore.YELLOW)
        dirname = input(str(">>> "))
        list = os.listdir(dirname)
        for file1 in list:
            file1 = dirname + "/" + file1
            with open('key.key', 'r') as file:
                encoded = file.readline()
                f = Fernet(encoded)
            with open(file1, "rb") as file:
                    file_data = file.read() 
                    decrypted_data = f.decrypt(file_data)
            with open(file1, "wb") as file:
                file.write(decrypted_data)
                file.close()
            print("Derypted file " + file1)
        print("\nFolder decrypted successfully!")
        input("Press enter to continue")

    uname = os.uname()
    if uname.sysname == "Linux":
        os.system("clear")
        main()
    if uname.sysname == "Windows":
        os.system("cls")
        main()
        
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
