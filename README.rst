=========
Bucketize
=========

What?
-----

A CLI tool to determine STDIN line rate at the interval of choice.

Installation
------------

Directly from github:

.. code-block::bash

    $ pip install git+https://github.com/smetj/bucketize.git


From Pypi:

    $ pip install bucketize


From a cloned repo:

.. code-block:: bash

    $ python setup.py install



Examples
--------

Send to Graphite the number of close() calls a process does per 10 seconds:


.. code-block:: bash

    $ strace -p 2760 -e close | bucketize --time_bucket_size 10 --output_template "one.two.three {amount} {time}"
    one.two.three 1 1476562447.65
    one.two.three 0 1476562457.65
    one.two.three 68 1476562467.65
    one.two.three 1 1476562477.65
    one.two.three 1 1476562487.65
    one.two.three 0 1476562497.65^C

    $ strace -p 2760 -e close | bucketize --time_bucket_size 10 --output_template "one.two.three {amount} {time}"| nc graphite-server 2003




