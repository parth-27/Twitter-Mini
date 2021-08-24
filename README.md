# Twitter Mini
## Setup

1. Git Clone the project with: ```git clone https://github.com/parth-27/Twitter-Mini.git```.

2. Move to the base directory: ```cd Twitter-Mini/server```

3. Create a new python enveronment with: ```python -m venv env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.
