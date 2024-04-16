# Backend
Following scripts should be run in the **`root`** folder.

## Environment setup
Firstly, create a virtual environment to install python dependencies.

    python -m venv env

Line above will create a folder named`env` where the scripts to start the virtual environment can be found. To activate the virtual environment run the following:

    source env/bin/activate

## Installation
Now, dependencies can be installed via:

    pip install -r requirements.txt

## Migration
To set up the database and database tables, run the following scripts:

    python manage.py makemigrations
    python manage.py migrate
After the migrations are done, project will be ready to be built for the first time.

## Building
To build and run the server, run the following bash script:

    python manage.py runserver
By default, Django server will be run at the `http://127.0.0.1:8000/`

## Preparing example data
After navigating to `http://127.0.0.1:8000/` address, via the form at the bottom of the page data can be created to populate the database. For this example, car models will be created with brand, model and manufacture year. The structure of data is already presented above the form as JSON for the available data.

# Frontend
Please refer to the `README` file in `frontend` directory for the guide to build the UI of the project.
