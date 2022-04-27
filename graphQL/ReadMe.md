# We have create project for Image upload using Graphql API, Graphene library with Celery progress bar.
   - Inside We have create Django application name "hero".
# We have used the list of libary for GraphQL using Image upload mentioned below:-
​
  -Graphene 
    pip install graphene
  
  -Graphene-Django
    pip install graphene_django
​
  -Celery progress bar
    pip install celery_progress
​
  -Tastypie
    pip install tastypie
​
# Also we have create Test case for file upload.
  -> Command for Run Test Case file:
    ./manage.py test
​
# Start Celery Command for progress bar.
  -> Command for Celery progress bar.
   celery -A demoGraphQl worker -l info
​
# Start Django Project Command:
  -> Command for Run project:
   python manage.py runserver