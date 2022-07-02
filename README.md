
# Capstone Project Interface

Django Based interface for machine learning & various models to train & detection through web surface.


## Features

- Tracking in RealTime
- Blah Blah
    
## Run Locally

Clone the project :

```bash
  git clone https://github.com/MasumBhai/Capstone_Project_Interface.git
```

Go to the project directory :

```bash
  cd Capstone_Project_Interface
```

Creating virtual environment (for windows) :

```bash
  pip install virtualenv
  python<version> -m venv <virtual-environment-name>
  source env/bin/activate
```

Install dependencies :

```bash
  pip install -r requirements.txt
```
propagating changes to your models :
```bash
  py manage.py makemigrations
  py manage.py migrate --run-syncdb
```
SuperUser Creation: [see](https://stackoverflow.com/a/66924978/13939591) :
```bash
  py manage.py createsuperuser
```

Collect static files from each of the applications :
```bash
  py manage.py collectstatic
```

Migrate everything to be updated :
```bash
  py manage.py migrate
```
Test before any issue arises :
```bash
  py manage.py test
```
Run the server : 
```bash
  py manage.py tailwind start
  py manage.py runserver
```

## Deployment

To deploy this project run :

```bash
  py manage.py tailwind build
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Used By

This project is used by the following companies:

- Company 1
- Company 2

## Authors

- [Abdullah Al Masum](https://github.com/MasumBhai)

## Feedback

If you have any feedback, please reach out to me at [abdullahmasum6035@gmail.com](mailto:abdullahmasum6035@gmail.com?subject=Feedback%20For%20Your%20Github%20Repository)


