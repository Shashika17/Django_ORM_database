
# ____________[[1ST WAY TO RUN]]____________

## USING DOCKER IMAGE

   **Run command:-**
    docker compose up --build

   **Note:**
    Make sure you have installed Docker and Docker-Compose in your system. You can download it from the official website [here](https://www.docker.com/get-start)

   **Special Note:**
    after it start it will show [Starting development server at http://0.0.0.0:8000/] 0.0.0.0 is for global deployment it's originally deployed at [http://localhost:8000/] check this link to view page

      +-----------------------------------+
      |if there is login to admin:-       |
      |username : shashika                |
      |password : root                    |
      +-----------------------------------+
-------------------------------------------------------------------------------------------------------------------

# ____________[[2ND WAY TO RUN]]____________

## (1)  ACTIVATE ENVIORMENT

   **in cmd type:-**
    env_site/Scripts/activate

## (2)  INSTALL PACKAGES

   **in cmd type:-**
    pip install -r  requirements.txt

## (3) RUN THE PROJECT (TO START SERVER)

      in cmd navigate to assesment run command:-
      cd assesment

      and then to start server run command:-
      python manage.py runserver

      and then  open your browser and go to the link <http://localhost:8000/>

      +-----------------------------------+
      |if there is login to admin:-       |
      |username : shashika                |
      |password : root                    |
      +-----------------------------------+
    ---------------------------------------------------------------------------

## TO TEST

# Step1

      define dejango setting module type:-
      $env:DJANGO_SETTINGS_MODULE = "assesment.settings"
    --------------------------------------------------------------------------

# Step2

      run  test in django admin panel or by typing these commands in cmd :-
      pytest exams/tests.py
    --------------------------------------------------------------------------  
