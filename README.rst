Py3Mailer
========
**Simple python bulk mailer script.**
 Based and inspired from python-mailer & Jonathan Bydendyk
Send bulk html emails from the commandline or in your python3 script by specifying a database of recipients in csv form, a html template with var placeholders and a subject line.

Requirements
------------

* python >= 3.x

Usage
-----
Setup
~~~~~
Edit the config file before running the script::

    $ nano config.py

Commandline
~~~~~~~~~~~
The simplest method of sending out a bulk email.

Run a test to predefined test_recipients::

    $ ./py3mailer -t /path/to/html/file.html /path/to/csv/file.csv 'Email Subject'

Send the actual email to all recipients::

    $ ./py3mailer -s /path/to/html/file.html /path/to/csv/file.csv 'Email Subject'

Module Import
~~~~~~~~~~~~~
Alernatively import the Py3Mailer class into your own code::

    from py3mailer import Py3Mailer

    py3mailer = Py3Mailer('/path/to/html/file.html' '/path/to/csv/file.csv' 'Email Subject')

    # send a test email
    py3mailer.send_test()

    # send bulk mail
    py3mailer.send()

Examples
--------
HTML
~~~~
Example of using placeholders in your html email:

   <!DOCTYPE html>
 <html lang="en">
  <head>
  </head>
  <body> <br>
    Test HTML Email to
    <!--mail--><br>
    <p>Hi
      <!--name-->, This is a test email from Py3mailer</p>
    <p>column3=<!--colum3--></p>
    <p>column4=<!--colum4--></p>
  </body>
 </html>


Every column of the csv file may be used as a placeholder. Placeolders are for example ${name} or ${title}.
The special columns "reciver" and "sender" are created automatically and contain the complete reciver and sender names,
including the email address.

CSV
~~~
Example of how the csv file should look::

 name,email,column3,column4
 Someones Name,someone@example.com,column3,column4
 ,someone.else@example.com,column3,
 ,some.nameless.person@example.com,,

The csv file should have a header with column names.
- One column should be 'name' with the complete name of the reciver.
- One column must be 'email' with the email address.
- No column should be called 'receiver' or 'sender', as these are internally used.
