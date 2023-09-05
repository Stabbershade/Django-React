# Django-React

## Description
Practise on Django-React Typescript for educational and experimental purposes. This is part of an environment to test concepts and ideas on my school project.

**Installation Steps for Local Virtual environment**
1) Ensure [Python](https://www.python.org/downloads/) has been installed on your local system before proceeding.

2) Ensure [pip3](https://cloudzy.com/blog/pip-upgrade/) has been installed on your local systsm before proceeding any further. 

3) Ensure [npm](https://kinsta.com/blog/how-to-install-node-js/) has been installed on your local systsm before proceeding any further. 

4) Create a new directory on your system so that it is easier to locate the files when developing the application.

5) Open a cmd/terminal on your local system and type the following command to create an isolated development environment on your system. Doing this step would create a directory named ".venv".
    ```bash
    python -m venv .venv
    ```

6) Next step would be to execute this command,
   For Windows:
     ```bash
     .venv\Scripts\activate.bat
      ```
    For Mac/Linux:
    ```bash
    source .venv/bin/activate
    ```
7) Before proceeding look for the (.venv) sign on your command line before proceeding.

8) Once the steps have been completed, type the following commands to install the needed dependencies on your system from the "requirements.txt". Once the installation is complete you can proceed to run the application
    ```bash
   pip install -r requirements.txt
    ```

9) Navigate into the `frontend` folder and run the command. This ensure frontend dependencies are installed.
  ```bash
  npm install
  ```

10) Ensure for updated `bundle.js` in the current directory by running the command:
  ```bash
  npm run dev
  ```

**Running The Application**
1) Type the following commands to run the server as needed:
  ```bash
  python manage.py runserver
  ```