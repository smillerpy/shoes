=============
Super Zapatos
=============

To use this project follow these steps:

#. $ git clone git@github.com:smillerpy/shoes.git
#. $ pip install django
#. $ mkvirtualenv super
#. $ pip install -r requirements/local.txt
#. $ chmod 766 manage.py 
#. $ ./manage.py migrate
#. $ ./manage.py runserver


Usage examples:

Get the list of stores:
curl -u my_user:my_password http://localhost:8000/services/stores/ 

Create a new store 
curl -H "Content-Type: application/json" -X POST -d '{"name":"aaaa","address":"xyz"}' -u my_user:my_password http://localhost:8000/services/stores/ 

Or you can go to this urls in a navegator an explre them with a cool interface. Remmember to register
Happy evaluating!

