step 1:
    start python virtual enviournment:
        python3 -m venv venv
        activate: source venv/bin/activate
step 2:
    install django: pip install django
    install mysql; pip install mysql
    install mysql connector: pip install mysql-connector-python  
step 3:
    start project: django-admin startproject dcrm
    start app: python manage.py startapp website
step 4:
    add app on django,
    fix database from sqlite to mysql
    then :
        ......................................................
        . import mysql.connector                            .
        .                                                   .
        . dataBase = mysql.connector.connect(               .
        .     host='localhost',                             .
        .     user='root',                                  .
        .     passwd='password123'                          .
        . )                                                 .
        .                                                   .
        . # prepare a cursor object                         .
        . cursorObject = dataBase.cursor()                  .
        .                                                   .
        . # Create a database                               .
        . cursorObject.execute("CREATE DATABASE elderco")   .
        .                                                   .
        . print("All Done!")                                .
        ......................................................
    and run this file from the place where there is manage.py file
    and then 'python manage.py migrate' to configure databse according to django
step 5: create super user:
            python manage.py createsuperuser

step 6: connect the django app with django project using urls
step 7: Django Login and Logout