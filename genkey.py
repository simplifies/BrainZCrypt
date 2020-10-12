def main():
    print(Fore.LIGHTCYAN_EX)
    print("Creating unique key...")
    key = Fernet.generate_key()
    keytowrite = key
    path = "key.key"
    fi = open(path, 'wb')
    fi.write(keytowrite)
    fi.close
    print("Key generated! hide the key where no one can find it!")
    print("loss of the key will result in lose of the files!")
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