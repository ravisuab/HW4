# Under root folder
# To create virtual environment
python -m venv env-python
# To activate virtual environment
env-python/Scripts/activate
# To install libraries
pip install -r requirements.txt

# Under flask folder
# To initialize db and create table
python init_db.py
# To run the application
flask run