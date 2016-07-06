=====
djangorelishblog
=====

djangorelishblog is a simple Django app to have a blog on your site.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add **django.contrib.humanize**, **djangorelishblog** and **markdownx** to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.humanize',
    'djangorelishblog',
    'markdownx',
]```

2. Include the **djangorelishblog** and **mardownx** URLconf in your project urls.py:

```python
url(r'^blog/', include('djangorelishblog.urls')),
url(r'^markdownx/', include('markdownx.urls')),
```

3. Run `python manage.py collectstatic` to setup **markdownx**.

4. Run `python manage.py migrate` to create the blog models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a blog (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/blog/ to view the blog.