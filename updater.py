from git import Repo
import time, requests, sys, shutil, os
import os.path

def main():
    print("Would you like to update the converter part of this program? It downloades the latest version from github page")
    print("1.Yes")
    print("2.No")
    updateanswer = input("")

    if updateanswer == "1":
        connection_test = str()

        if os.path.exists("./repo"):
            shutil.rmtree("./repo")  
            print("deleted file")      

        response = requests.get('https://github.com/CobaltXII/KrunkerToWavefront.git')
        print("Checking server status")

        if response.status_code == 200:
            print('Found server')                
            time.sleep(2)
            Repo.clone_from("https://github.com/CobaltXII/KrunkerToWavefront.git", "./repo")
            print("Cloned git")
            call()
                
        elif response.status_code == 404:
            print('Not Found.')
            time.sleep(2)
            clear()
    
    elif updateanswer == "2":
        call()

    else:
        print("ERROR With selecting answer, did you type 1 or 2?")
        time.sleep(4)
        clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

def call():
    print("Finished")
    time.sleep(1)
    import main
    main.main()

if __name__ == "__main__":
    main()
    