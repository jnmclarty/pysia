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

See Also
--------

There are python 3 bindings for Sia, maintained by humans which might be or become more pythonic. See siapy_.

Install
-------

.. code-block:: console

    pip install pysia

Usage
-----

.. code-block:: python

   from pysia import Sia
   
   sia = Sia()
   
   consensus = sia.get_consensus()


Features
--------

* Exposes a method for each API endpoint of siad, matching Siad API docs 1-to-1
* User-friendly autocomplete (GET -> get*ters, POST -> setters)
* Pure python responses

License
-------

* Free software: MIT license

Documentation
-------------

Coming soon, here:

* Documentation: https://pysia.readthedocs.io.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _siapy: https://github.com/lolsteve/siapy
