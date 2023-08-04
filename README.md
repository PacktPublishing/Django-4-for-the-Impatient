


# Django 4 for the Impatient

<a href="https://www.packtpub.com/product/django-4-for-the-impatient/9781803245836?utm_source=github&utm_medium=repository&utm_campaign=9781803245836"><img src="https://static.packt-cdn.com/products/9781803245836/cover/smaller" alt="Django 4 for the Impatient" height="256px" align="right"></a>

This is the code repository for [Django 4 for the Impatient](https://www.packtpub.com/product/django-4-for-the-impatient/9781803245836?utm_source=github&utm_medium=repository&utm_campaign=9781803245836), published by Packt.

**Learn the core concepts of Python web development with Django over a weekend**

## What is this book about?
First Paragraph from the Long Description

This book covers the following exciting features: <First 5 What you'll learn points>
* Understand and implement Django Apps’ basic structure, including URLs, views, templates, and models
* Add bootstrap to improve the aesthetics of the site
* Create your own custom pages and have different URLs to route to them
* Navigate between pages by adding a header bar to all pages
* Work with databases and models

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1803245832) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviereviews.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

```

**Following is what you need for this book:**
This book is for Python developers at any level of experience with Python programming who want to build full-stack Python web applications using Django. The book is for absolute Django beginners..

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-12      | Python 3.8+                     | Windows, Mac OS X, and Linux (Any) |
| 1-12      | pip             | Windows, Mac OS X, and Linux (Any) |
| 1-12       | Visual Studio Code            | Windows, Mac OS X, and Linux (Any) |
| 1-12       | Git            | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/s1vSa).


### Related products <Other books you may enjoy>
* Python Microservices Development – 2nd edition [[Packt]](https://www.packtpub.com/product/python-microservices-development-second-edition/9781801076302?utm_source=github&utm_medium=repository&utm_campaign=9781801076302) [[Amazon]](https://www.amazon.com/dp/1801076308)

* Python Web Development with Sanic [[Packt]](https://www.packtpub.com/product/python-web-development-with-sanic/9781801814416?utm_source=github&utm_medium=repository&utm_campaign=9781801814416) [[Amazon]](https://www.amazon.com/dp/1801814414)

## Errata 
 * Page 64 (Code Snippet 3,line 2):  **python3 manage.py migrat** _should be_ **python3 manage.py migrate**
 * Page 64 (Code Snippet 4,line 2):**python manage.py migr3te** _should be_ **python manage.py migrate**
 * Page 2 (line 4):**There are other popular frameworks, such as Flash in Python and Express in JavaScript** _should be_ **There are other popular frameworks, such as Flask in Python and Express in JavaScript**
 * Page 33 (Code Snippet 1): The lines of code **`<h1>Welcome to the Home Page, {{ name }}</h1>`** and **`<h2>This is the full home page</h2>`** between the **`<div class="container">`** and **`</div>`** tags _should be removed_ in order to obtain the output shown in Figure 4.10.

 
## Get to Know the Authors
**Greg Lim**
is a technologist and the author of several books on programming. He has taught programming in tertiary institutions for many years and places a strong emphasis on learning by doing.

**Daniel Correa**
is a researcher, a software developer, and author of programming books. He has a Ph.D. in Computer Science. He is a professor at Universidad EAFIT in Colombia. He is interested in software architectures, frameworks (such as Laravel, Nest, Django, Express, Vue, React, Angular, and many more), web development, and clean code.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781803245836">https://packt.link/free-ebook/9781803245836 </a> </p>
