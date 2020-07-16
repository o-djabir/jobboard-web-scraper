# jobboard-web-scraper

This application lets you scrape french jobboards, and helps automate applying to job offers.

For this application to run, you need to have Python and Django installed, as well as django-bootstrap4. 



Once you've installed all the necessities, downloaded and extracted the repository, you should start by creating a superuser. 

``sh
python manage.py createsuperuser
``


You can now run the project. On your terminal/command prompt/...etc, navigate to the root of your folder, where the manage.py file is located and run the project with:

``sh
python manage.py runserver
``

The applicaton will be up and running at http://127.0.0.1:8000/webScraper/

You now need to scrape the jobboards and save the job postings. In your terminal/command prompt/...etc, at the same location, simply run:

``sh
python manage.py scrape
``

Once it's completed, reload your page, and the postings should appear. You can delete them directly from the user interface, or mass delete them from the admin view, and scrape later once additional offers have been posted.
