import sys
import os
import subprocess

python_path = sys.executable
air_directory = ""
current_dir = os.getcwd()
if current_dir.find('air'):
    air_directory = f"{current_dir}"
else:
    air_directory = os.path.join(current_dir, "air")
extension = ".py"
exclude = "air13.py"

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def print_fail(message):
    print(f"{colors.RED}{message}{colors.ENDC}")

def print_success(message):
    print(f"{colors.GREEN}{message}{colors.ENDC}")

def test():
    success = 0
    total = 0

    files = os.listdir(air_directory)
    for file in files:
        if file.endswith(extension) and not file in exclude:
            path = os.path.join(air_directory, file)

            # test si le fichier existe bien
            try:
                with open(path, mode="r") as f:
                    print_success(f"Le fichier {file} a bien été trouvé dans le répertoire")
                    # c'est un success, on incrémente
                    success += 1
                    f.close()
            except FileNotFoundError:
                print_fail("Le fichier n'a pas été trouvé")
            finally:
                total += 1

            # exécution de la fonction test du fichier
            result = subprocess.run([python_path, path] + ['--test'], capture_output=True, text=True)
            exit_code = result.returncode
            if exit_code == 0:
                print_success(f"{file} : success")
                success += 1
            else:
                print_fail(f"{file} : fail")
                print_fail(exit_code)
                print_fail(f"{result.stdout}")
                print_fail(f"{result.stderr}")
            total += 1
    print(f"Total success: ({success}/{total})")
test()
