=====
PySia
=====


.. image:: https://img.shields.io/pypi/v/pysia.svg
        :target: https://pypi.python.org/pypi/pysia

.. image:: https://img.shields.io/travis/jnmclarty/pysia.svg
        :target: https://travis-ci.org/jnmclarty/pysia

.. image:: https://readthedocs.org/projects/pysia/badge/?version=latest
        :target: https://pysia.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jnmclarty/pysia/shield.svg
     :target: https://pyup.io/repos/github/jnmclarty/pysia/
     :alt: Updates


Sia API bindings for Python 2 & 3.

This library is built using code-generation, to exactly match the endpoints, docs and responses maintained by Sia.  This library will not attempt to improve on, or resist, any API changes made upstream to siad.

This version targets siad >= 1.2.2.

Install
-------

.. code-block:: console

    pip install pysia

Usage
-----

.. code-block:: python

   >>> from pysia import Sia
   >>> sc = Sia() # Optionally, pass host & port.  Defaults to localhost & 9980
   
   >>> consensus = sc.get_consensus()
   >>> consensus['height']
   108058
       
   backup_made = sc.get_wallet_backup(destination=r'd:\siadwallet.dat')
   print(backup_made)
   # True
   
   backup_made = sc.get_wallet_backup(destination=r'error causing input?@#$!`')
   print(backup_made)
   >>> {'message': 'error when calling /wallet/backup: destination must be an absolute path'}

   print(sc.get_gateway())
   >>> {'peers': [{'netaddress': '92.253.172.90:9981', 'version': '0.5.2', 'inbound': False, 'local': False},...]}

   >>> print(sc.set_gateway_connect('212.77.177.47:9981'))
   True

   >>> print(sc.set_gateway_disconnect('212.77.177.47:9981'))
   True
    
   >>> print(sc.set_gateway_disconnect('212.77.177.47:9981'))
   {'message': 'not connected to that node'}


Features
--------

* Exposes a method for each API endpoint of siad, matching Siad API docs 1-to-1
* User-friendly autocomplete (GET -> getters, POST -> setters)
* Pure python responses
* User-friendly key-words called out for url-parameters GET-methods

Donations
---------

Sia:

2fd5ada234b5dba82584160213d8c9698d080bc4311277667a1ef38e5265fe7058aeeb627822

License
-------

* Free software: MIT license

Documentation
-------------

Coming soon, here:

* Documentation: https://pysia.readthedocs.io.

See Also
--------

There are python 3 bindings for Sia, maintained by humans which might be or become more pythonic. See siapy_.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _siapy: https://github.com/lolsteve/siapy
