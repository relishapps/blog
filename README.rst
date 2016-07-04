=====
Blog
=====

Blog is a simple Django app to have a blog on your site.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'blog',
    ]

2. Include the blog URLconf in your project urls.py like this::

    url(r'^', include('blog.urls')),

3. Run `python manage.py migrate` to create the blog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a blog (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to view the blog.