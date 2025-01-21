# # A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.
# # To create a virtual environment in Python, you can use the ven module that comes with Python. Here's an example of how to create a virtual environment and acfivate it:
    
# # # Create a virtual environment
# # python3 -m venv myenv               #PYTHON3 for macos and only python for windows

# # # Activate the virtual environment (Linux/macOS)
# # source myenv/bin/activate

# Activate the virtual environment (Windows)
# # myenv\Scripts\activate.bat

# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.
# To deactivate the virtual environment, you can use the deactivate command:

# # Deactivate the virtual environment
# deactivate



# The "requirements.txt" file
# In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:

# Output the list of installed packages and their versions to a file
# pip3 freeze > requirements.txt

# To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:
# # Install the packages listed in the requirements.txt file

# pip3 install -r requirements.txt          ##install all required packages from env to main computer

# Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.