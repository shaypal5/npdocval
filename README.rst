npdocval
########

|PyPI-Status| |Downloads| |PyPI-Versions| |Build-Status| |Codecov| |Codefactor| |LICENCE|

Numpy docstring validation CLI (original code by `akaszynski <https://github.com/akaszynski`_)

.. code-block:: bash

   npdocval module my_package


.. contents::

.. section-numbering::


🔩 Installation
===============

Install ``npdocval`` with:

.. code-block:: bash

  pip install npdocval

🪠  Use
=====

From the terminal, in a Python environment when the desired module (often a package) is installed, run:

.. code-block:: bash

   npdocval module my_package


🎁 Contributing
===============

Package author (not the core code itself!) and current maintainer is `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed, especially since this package is very much in its infancy and many other pipeline stages can be added.

🪛 Installing for development
-----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:npdocval/npdocval.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd npdocval
  pip install -e ".[test]"


⚗️ Running the tests
--------------------

To run the tests, use:

.. code-block:: bash

  python -m pytest


Notice ``pytest`` runs are configured by the ``pytest.ini`` file. Read it to understand the exact ``pytest`` arguments used.


📓 Adding documentation
-----------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
.. _`these conventions`: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


💳 Credits
==========
The original code using `Numpydoc Validation <https://numpydoc.readthedocs.io/en/latest/validation.html>`_ to create a recrusive function generating a report for the entire module was written by `Alex Kaszynski <akascap@gmail.com>`_ (his Github user is `akaszynski <https://github.com/akaszynski`_). See `the original package's repository <https://github.com/pyvista/numpydoc-validation>`_.

The CLI wrapper was created by `Shay Palachy <http://www.shaypalachy.com/>`_  (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/npdocval.svg
  :target: https://pypi.org/project/npdocval

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/npdocval.svg
   :target: https://pypi.org/project/npdocval

.. |Build-Status| image:: https://github.com/npdocval/npdocval/actions/workflows/test.yml/badge.svg
  :target: https://github.com/npdocval/npdocval/actions/workflows/test.yml

.. |Codecov| image:: https://codecov.io/github/npdocval/npdocval/coverage.svg?branch=master
   :target: https://codecov.io/github/npdocval/npdocval?branch=master

.. |Codacy|  image:: https://api.codacy.com/project/badge/Grade/7d605e063f114ecdb5569266bd0226cd
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/shaypal5/npdocval?utm_source=github.com&utm_medium=referral&utm_content=shaypal5/npdocval&utm_campaign=Badge_Grade_Dashboard

.. |Requirements| image:: https://requires.io/github/shaypal5/npdocval/requirements.svg?branch=master
     :target: https://requires.io/github/shaypal5/npdocval/requirements/?branch=master
     :alt: Requirements Status

.. |Downloads| image:: https://pepy.tech/badge/npdocval
     :target: https://pepy.tech/project/npdocval
     :alt: PePy stats

.. |Codefactor| image:: https://www.codefactor.io/repository/github/npdocval/npdocval/badge?style=plastic
     :target: https://www.codefactor.io/repository/github/npdocval/npdocval
     :alt: Codefactor code quality
