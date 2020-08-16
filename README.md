# DjangoHyperNewsPortal
This project is a "Hyper News Portal" developed using Django framework. 

Run the following command in the project directory to see the main page of the project:

```python manage.py runserver```

The main page will be available at the ```localhost:8000``` address:

![hyper_main](https://user-images.githubusercontent.com/37106831/90333587-d26ffb80-dfcf-11ea-8cad-03926b41df5f.jpg)

The news are read from ```news.json``` file and listed and grouped by their dates in descending order:

You can search any phrase/keyword in the titles of the news. You can also click on the links to see the news details. 

In addition, you can add news using ```Create news``` link:

![hyper_create](https://user-images.githubusercontent.com/37106831/90333771-1e6f7000-dfd1-11ea-8eea-d02b27c237b7.jpg)

Created news are added to the ```news.json```file too.
