from setuptools import setup

setup(
    name = "django-timezones",
    version = __import__("timezones").__version__,
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    description = "A Django reusable app to deal with timezone localization for users",
    long_description = open("README").read(),
    url = "http://code.google.com/p/django-timezones/",
    license = "BSD",
    packages = [
        "timezones",
        "timezones.templatetags",
    ],
    install_requires = [
        "pytz==2009a",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Framework :: Django",
    ]
)