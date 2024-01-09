# minimal_django_pyfakefs_unittest_mock
Minimal Django project to produce a bug caused by the combination of pyfakefs and unittest.mock 

Based on https://docs.djangoproject.com/en/5.0/intro/tutorial01/

Steps to reproduce:
pip install -r requirements.txt
cd mysite
python manage.py runserver
pytest -m with_fakefs

Expected:
2 test cases pass

Observed:
first test case passes, second test case fails

In contrast, run pytest -m without_fakefs. this runs an identical test, without using the fake filesystem fixture. both cases pass, as expected.

