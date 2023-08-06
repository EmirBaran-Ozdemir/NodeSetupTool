# GitHub Repo Setup and Node.js Package Installation Tool

Tired of the repetitive process of setting up Node.js projects? Look no further! Introducing a powerful tool designed to simplify your Node.js project setup.

This Python script provides a convenient way to automate the process of setting up a GitHub repository, updating it if it already exists, installing Node.js packages listed in `package.json` files, and optionally clearing the setup tool after installation. It is particularly useful for managing multiple Node.js projects within a repository.

## Features

- Clones or updates a GitHub repository based on the provided repository URL.
- Searches for all `package.json` files within the repository directory and installs the corresponding Node.js packages using `npm install`.
- Provides optional verbose mode for detailed search information.
- Supports clearing the setup tool directory after installation.

## Prerequisites

- Python 3.x
- `git` and `npm` should be installed and added to the system's PATH.

## Usage

Run the script from the command line with the following arguments:

- `-u` or `--url`: The GitHub repository URL (e.g., `https://github.com/username/repo.git`).
- `-c` or `--clear`: (Optional) Clear the setup tool directory after installation.
- `-v` or `--verbose`: (Optional) Show detailed search information.

Example:

```shell
pip install -r requirements.txt
python setup.py -u https://github.com/username/repo.git -c -v
```

## Workflow

1. The script starts by parsing command-line arguments using the `argparse` library.

2. It sets up logging using the `coloredlogs` library to provide clear output messages.

3. The `InstallPackages` function is defined to recursively search for `package.json` files within the repository directory and install the corresponding Node.js packages using `npm install`.

4. The `GetRepo` function handles cloning or updating the GitHub repository based on the provided URL.

5. The `CheckRepo` function verifies if the repository URL is valid and accessible.

6. In the `main` function:
   - The repository URL and directory are extracted from the command-line arguments.
   - The existence of the repository is checked using `CheckRepo`. If the repository does not exist, the script exits.
   - The repository is cloned or updated using `GetRepo`.
   - The `InstallPackages` function is called to install Node.js packages.
   - If the `-c` flag is provided, the setup tool directory is cleared after installation.

7. The script is executed if run as the main module.

## Notes

- Make sure you have the necessary permissions to clone the repository and install packages.
- If you encounter issues, ensure that `git` and `npm` are correctly installed and accessible from the command line.
- This script assumes that the repository's main directory contains the Node.js projects (directories containing `package.json` files).
- Be cautious when using the `-c` flag, as it will delete the setup tool directory, potentially resulting in data loss.

## License

This script is provided under the [MIT License](LICENSE). Use it at your own risk.

**Disclaimer:** This tool is not officially maintained or endorsed by GitHub, npm, or any other associated services. Use it responsibly and ensure you understand the implications of the actions it performs.
