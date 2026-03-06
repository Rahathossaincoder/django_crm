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
step 8: After writing models we do:
        python manage.py makemigrations
        and it gives us a:
        "
            ..............................................................
            . from django.db import migrations, models                   .
            .                                                            .
            .                                                            .
            . class Migration(migrations.Migration):                     .
            .                                                            .
            .     initial = True                                         .
            .                                                            .
            .     dependencies = [                                       .
            .     ]                                                      .
            .                                                            .
            .     operations = [                                         . 
            .         migrations.CreateModel(                            .
            .             name='Record',                                 .
            .             fields=[                                       .
            .                 ('id', models.BigAutoField(                .
            .                     auto_created=True,                     .
            .                     primary_key=True,                      .
            .                     serialize=False,                       .
            .                     verbose_name='ID'                      .
            .                 )),                                        .
            .                 ('created_at', models.DateTimeField(       .
            .                     auto_now_add=True                      .
            .                 )),                                        .
            .                 ('first_name', models.CharField(           .
            .                     max_length=50                          .
            .                 )),                                        .
            .                 ('last_name', models.CharField(            .
            .                     max_length=50                          .
            .                 )),                                        .
            .                 ('email', models.CharField(                .
            .                     max_length=150                         .
            .                 )),                                        .
            .                 ('phone', models.CharField(                .
            .                     max_length=15                          .
            .                 )),                                        .
            .                 ('address', models.CharField(              .
            .                     max_length=100                         .
            .                 )),                                        .
            .                 ('city', models.CharField(                 .
            .                     max_length=50                          .
            .                 )),                                        .
            .                 ('state', models.CharField(                .
            .                     max_length=50                          .
            .                 )),                                        .
            .                 ('zipcode', models.CharField(              .
            .                     max_length=20                          .
            .                 )),                                        .
            .             ],                                             .
            .         ),                                                 .
            .     ]                                                      .
            ..............................................................
        "
        and then python manage.py migrate, will migrate it to mysql database
step 9: To add this on models.py:
        on admin.py:
        
        from .models import model_name
        admin.site.register(model_name)


