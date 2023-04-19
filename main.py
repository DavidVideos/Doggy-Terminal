import os
import subprocess
import shutil
import socket
import psutil
import requests
import bcrypt
import urllib.request
import zipfile
import webbrowser as wb

if not os.path.exists("help_messages"):
        print("help_messages foler was not found")
        print("Downloading help_text.zip from Github...")
        # Download and extract help_text.zip from Github
        url = "https://raw.githubusercontent.com/DavidVideos/Doggy-Terminal/main/storage_folder/help_text.zip"
        with urllib.request.urlopen(url) as response, open("help_text.zip", "wb") as out_file:
            shutil.copyfileobj(response, out_file)
            print("help_text.zip is downloaded")
            print("Extracting help_text.zip...")
        with zipfile.ZipFile("help_text.zip", "r") as zip_ref:
            zip_ref.extractall("help_messages")
        print("help_text.zip is extracted")
        print("Deleting help_text.zip...")
        os.remove("help_text.zip")
        print("help_text.zip is deleted")

if not os.path.exists("linkget_downloads"):
    os.mkdir("linkget_downloads")

f = open('./help_messages/help.txt', 'r')
help = f.read()

current_dir = os.path.dirname(os.path.abspath(__file__))

help_messages_path = "help_messages"
linkget_downloads = "linkget_downloads"

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Doggy Terminal [Version: IN DEVELOPMENT]")

while True:
    # Az aktuális mappa és meghajtó megjelenítése
    print(f"{os.getcwd()} $ ", end="")
    
    # A felhasználó által beírt parancs beolvasása
    command = input()
    
    # A parancsok feldolgozása
    if command.startswith("cd "):
        # A cd parancs feldolgozása
        directory = command.split(" ")[1]
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print(f"{directory}: no such directory")
    elif command.startswith("open "):
        # Az open parancs feldolgozása
        file_path = command.split(" ")[1]
        try:
            os.startfile(file_path)
        except FileNotFoundError:
            print(f"{file_path}: no such file")
    elif command == "exit":
        # A terminál bezárása
        break

    elif command == "local":
        print("Your Local IPS Is: " + host_ip)
        print("Your Desktop Name Is: " + host_name)

    elif command == "public":
        def get_public_ip():
            url = 'https://api.ipify.org'
            response = requests.get(url)
            return response.text
        
        public_ip = get_public_ip()
        print(f"Your public IP address is {public_ip}")

    elif command == "ls":
        # A jelenlegi mappa fájljainak listázása
        files = os.listdir()
        for file in files:
            print(file)

    elif command == "help":
        print(help)
        f.close()

    elif command.startswith("ping "):
        # A ping parancs feldolgozása
        params = command.split(" ")[1:]
        try:
            # Ha van megadva ciklus, akkor annyiszor pingelünk
            if "-n" in params:
                count = int(params[params.index("-n") + 1])
                host = params[params.index("-n") + 2]
                for i in range(count):
                    subprocess.call(["ping", "-n", "1", host])
            # Ha nincs megadva ciklus, akkor végtelenül pingelünk
            else:
                host = params[0]
                while True:
                    subprocess.call(["ping", "-n", "1", host])
        except:
            print("An error occurred while pinging")

    elif command == "ipconfig":
        os.system("ipconfig")

    elif command.startswith("ssh "):
        # Az SSH parancs feldolgozása
        ssh_command = command.split(" ")[1:]
        try:
            subprocess.call(["ssh"] + ssh_command)
        except:
            print("An error occurred while connecting to the SSH server")


    elif command.startswith("cp "):
    # A cp parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            shutil.copy(source, destination)
        except FileNotFoundError:
            print(f"{source} vagy {destination}: No such file or directory")

    elif command.startswith("copy "):
    # A cp parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            shutil.copy(source, destination)
        except FileNotFoundError:
            print(f"{source} or {destination}: No such file or directory")

    elif command.startswith("mv "):
        # Az mv parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            shutil.move(source, destination)
            print(f"{source} is moved to {destination}")
        except FileNotFoundError:
            print(f"{source}: No such file")

    elif command.startswith("move "):
        # Az mv parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            shutil.moved(source, destination)
            print(f"{source} is moved to {destination}")
        except FileNotFoundError:
            print(f"{source}: No such file")
    
    elif command.startswith("rn "):
        # Az mv parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            os.rename(source, destination)
            print(f"{source} is renamed to {destination}")
        except FileNotFoundError:
            print(f"{source}: No such file")
    
    elif command.startswith("rename "):
        # Az mv parancs feldolgozása
        source = command.split(" ")[1]
        destination = command.split(" ")[2]
        try:
            os.rename(source, destination)
            print(f"{source} is renamed to {destination}")
        except FileNotFoundError:
            print(f"{source}: No such file")

    elif command.startswith("rm "):
        # Az rm parancs feldolgozása
        file_path = command.split(" ")[1]
        try:
            os.remove(file_path)
            print(f"{file_path} is removed")
        except FileNotFoundError:
            print(f"{file_path}: No such file")

    elif command.startswith("remove "):
        # Az rm parancs feldolgozása
        file_path = command.split(" ")[1]
        try:
            os.remove(file_path)
            print(f"{file_path} is removed")
        except FileNotFoundError:
            print(f"{file_path}: No such file")

    elif command.startswith("mkdir "):
    # A mkdir parancs feldolgozása
        directory = command.split(" ")[1]
        try:
            os.mkdir(directory)
            print(f"{directory} is created")
        except FileExistsError:
            print(f"{directory}: Already exists")
        
        except FileNotFoundError:
            print("Error when executing this command")
            print("usage mkdir: mkdir <folder_name>")
    
    elif command == "tasklist":
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            else:
                print(f"Name: {pinfo['name']}, Username: {pinfo['username']}, pid: {pinfo['pid']}")

    elif command.startswith("taskkill "):
        name = command.split(" ")[1]
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            else:
                if pinfo['name'] == name:
                    pid = pinfo['pid']
                    def kill_process(pid):
                        try:
                            process = psutil.Process(pid)
                            process.kill()
                            print(f"Process with PID {pid} killed successfully")
                        except psutil.NoSuchProcess:
                            print(f"No such process with name {name}")
                    kill_process(pid)
                    break
        else:
            print(f"No such process named {name}")
    
    elif command.startswith("linkget "):
        try:
            link = command.split(" ")[1]
            file_name = link.split("/")[-1] # A fájl neve a link utolsó része lesz
            file_path = os.path.join(linkget_downloads, file_name) # A fájl elérési útvonala
            print("Downloading", file_name, "from", link)
            urllib.request.urlretrieve(link, file_path)
        except ValueError:
            print("Error when executing this command")
            print("usage linkget: linkget <link_to_file>")
        print(file_name, "is downloaded succesfull")


    else:
        # Ismeretlen parancs esetén hibaüzenet kiírása
        print("This cannot be recognized as an internal or external command or an operable program")
        print("Type 'help' to see all the available commands")
