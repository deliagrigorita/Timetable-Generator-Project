# Timetable-Generator-Project

## Project structure
```
.
├── Timetable_Generator_Project/
│ ├── Timetable-Generator-Project/   # project configurations
│ │ ├── init.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ └── Timetable/                     # sub-module of the application
                                     # (ex.: Timetable for front-end views, Generator for algorithms)
│ ├── migrations/                    # module-specific migrations (auto-generated)
│ │ └── ...
│ ├── static/                        # static html / css / js elements
│ │ └── ...
│ ├── templates/                     # module-specific templates (front-end views)
│ │ └── ...
│ ├── views/                         # module-specific views (back-end controllers)
│ │ └── ...
│ ├── init.py                        # module-specific pre-initialization
│ ├── urls.py                        # module-specific urls definitions
│ ├── models.py                      # module-specific models (ORM classes)
│ └── tests.py                       # modeule-specific test code
├── venv/                            # automatically created in terminal
│ └── ...
├── manage.py                        # run script
├── .gitignore                       # files / folders which will not be pushed into VCS
├── requirements.txt                 # contains external modules
└── README.md
```

## Developer work-instruction

### 1. Clone the Repository

To work on this Django project locally, you'll need to clone the repository. Open your terminal and run:
```
git clone https://github.com/deliagrigorita/Timetable-Generator-Project.git
git fetch
git pull
```

### 2. Create a venv (only once)
```
cd Timetable-Generator-Project
python -m venv venv
venv\Scripts\activate
```

### 3. Install requirements (after new dependencies are introduced)
```
pip install -r requirements.txt
```

### 4. Local database sync
#### 4.1 Make sure XAMPP's MySQL server is up and running
(must already have a database called 'timetable_generator_project' created from phpmyadmin page)
#### 4.2 Set database to local one {#set-database}
```
Timetable_Generator_Project/settings.py
comment   'default':{..., 'NAME': 'raul05madalin$Timetable-Generator-Project', ...}
uncomment 'default':{..., 'NAME': 'timetable_generator_project', ...}
```
#### 4.3 Migrate models into the database
```
python manage.py makemigrations <package> #(ex. : Timetable)
python manage.py migrate
```

### 5. Run server locally
#### 5.1 In terminal:
```
python manage.py runserver
```
#### 5.2 In PyCharm:
##### New configuration:
```
Python: 3.10
script: /path/to/project/Timetable-Generator-Project/manage.py
script parameters: runserver
```
#### 5.3 Open localhost
```
http://127.0.0.1:8000/
```

### 6. Push changes to prod
When pushing into ```main``` make sure that:
#### 6.1 Database is set back to prod one (see [4.2](#set-database) and revert)
#### 6.2 Any new requirements are placed into requirements.txt
(if not sure if you are missiong anything, run the following command)
```
pip3 freeze > requirements.txt
```




