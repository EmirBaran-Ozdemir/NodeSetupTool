import os
import sys, subprocess 
import argparse
import requests
import coloredlogs, logging

# ? Parse argument to get repo name
# ? Install/Update repo
# ? Find all package.json files
# ? Install node_modules
# ? List all node commands

argParser = argparse.ArgumentParser()
argParser.add_argument("-u", "--url", help="Link to github repo (https://exampleperson/examplerepo.git)")
argParser.add_argument("-c", "--clear", help="Clears this setup tool after installation", action="store_true")
argParser.add_argument("-v", "--verbose", help="Show search details", action="store_true")
args = argParser.parse_args()


log_format = '%(asctime)s %(name)s %(message)s'
date_format = '%H:%M:%S'

coloredlogs.install(level='DEBUG',datefmt=date_format,fmt=log_format)

def InstallPackages(repo_dir, nestedCount):
    logger = logging.getLogger('InstallPackages')

    nestedChar = "-"
    baseChar = "|"
    found = False
    for item in os.listdir(repo_dir):
        path = os.path.join(repo_dir, item)
        
        if os.path.isdir(path):
            if item == ".git" or item == "node_modules":
                continue
            if args.verbose:
                logger.info(f"{baseChar + nestedCount * nestedChar} Controlling {path}")
            found = InstallPackages(path, nestedCount + 1)

        if os.path.isfile(path):
            if item  == "package.json":
                found = True
                package_dir = os.path.dirname(path)
                logger.warning(baseChar + (nestedCount * nestedChar) + package_dir)
                logger.warning(f"Running npm install at {package_dir}")
                original_dir = os.getcwd()  
                os.chdir(package_dir)  
                os.system("npm install")  
                os.chdir(original_dir)  

    return found

def GetRepo(repo_url, repo_dir):
    logger = logging.getLogger('GetRepo')
    if os.path.exists(repo_dir):
        logger.warning("Repository already exists. Updating...")
        command = "git pull origin"
        os.chdir(repo_dir)
        os.system(command)
        os.chdir("..")
    else:
        logger.warning("Repository does not exist. Cloning...")
        command = "git clone "
        os.system(command + repo_url)
    if os.path.exists(repo_dir):
        logger.warning(f"{command} has successful")
        return True
    else:
        logger.error(f"{command} has failed")
        return False

def CheckRepo(url):
    logger = logging.getLogger('CheckRepo')
    logger.warning(f"Checking repository:{url}")
    response = requests.get(url.split(".git")[0])
    if response.ok:
        logger.warning("Connection established.")
        return True
    else:
        logger.error(f"Response code : {response.status_code}. Repo may not be exists. ")
        return False


def main():
    logger = logging.getLogger('Main')
    nestedCount = 0

    repo_url = args.url
    repo_dir = args.url.split(".git")[0].split("/")[-1]

    # Check if repo exists
    if not CheckRepo(repo_url):
        exit()

    # Update/Install Repository
    os.chdir("..")
    if not GetRepo(repo_url, repo_dir):
        exit()

    # Update/Install package.json dependencies
    logger.warning(f"Searching packages at {os.getcwd()}")
    if InstallPackages(repo_dir, nestedCount):
        logger.warning("Packages installed successfully")
    else:
        logger.critical("No packages found")

    # Delete setup tool after installation
    if args.clear:
        setupFolder = os.getcwd() + "/NodeSetupTool"
        subprocess.Popen(f"python -c \"import shutil, time; time.sleep(1); shutil.rmtree('{setupFolder}');\"")
        sys.exit(0)

if __name__ == "__main__":
    main()
