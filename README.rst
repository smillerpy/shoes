=============
Super Zapatos
=============

-------
Install
-------

To use this project follow these steps:

#. $ git clone git@github.com:smillerpy/shoes.git
#. $ pip install django
#. $ mkvirtualenv super
#. $ pip install -r requirements/local.txt
#. $ chmod 766 manage.py 
#. $ ./manage.py migrate

------------
Start server
------------

#. $ ./manage.py runserver


Usage examples:

Get the list of stores:
curl -u my_user:my_password http://localhost:8000/services/stores/ 

Create a new store 
curl -H "Content-Type: application/json" -X POST -d '{"name":"aaaa","address":"xyz"}' -u my_user:my_password http://localhost:8000/services/stores/ 

Or you can go to this urls in a navegator an explre them with a cool interface. Remmember to register

---------
RUN TESTS 
---------

#. $ ./manage.py test

The tests are for store only.
You may need to follow the following steps to install phantomjs. (You may get and error asking for it if that is the case)

#. $ sudo apt-get install software-properties-common
#. $ sudo apt-get update
#. $ sudo apt-get install -y python-software-properties python g++ make
#. $ sudo add-apt-repository -y ppa:chris-lea/node.js
#. $ sudo apt-get update
#. $ sudo apt-get install nodejs
#. $ sudo apt-get install fontconfig
#. $ sudo npm -g install phantomjs

Happy evaluating!


