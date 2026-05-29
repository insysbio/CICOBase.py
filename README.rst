LikelihoodProfiler.py
=====================

.. image:: https://github.com/insysbio/LikelihoodProfiler.py/actions/workflows/ci.yml/badge.svg
   :height: 20
   :target: https://github.com/insysbio/LikelihoodProfiler.py/actions/workflows/ci.yml
   :alt: CI

.. image:: https://img.shields.io/badge/python-3.10%2B-blue
   :height: 20
   :alt: Python 3.10+

.. image:: https://zenodo.org/badge/DOI/10.1371/journal.pcbi.1008495.svg
   :height: 20
   :target: https://doi.org/10.1371/journal.pcbi.1008495
   :alt: DOI:10.1371/journal.pcbi.1008495

``LikelihoodProfiler.py`` is a Python port of the CICO/LikelihoodProfiler
algorithms for practical identifiability analysis and confidence interval
evaluation.

The original Julia code line was published as ``LikelihoodProfiler.jl`` until
January 2025; its low-level computational core now lives in
`CICOBase.jl <https://github.com/insysbio/CICOBase.jl>`_.  This Python package
keeps the historical 0.3.0-era API and is useful for compatibility, experiments,
and validating Python translations of the original routines.  For new Julia
workflows, prefer CICOBase.jl and the current Julia ecosystem.

Status
------

This repository was previously tied to a frozen 2019 development environment.
The project metadata has been moved to ``pyproject.toml`` and the dependencies
are now limited to the packages imported by the library:

* ``numpy``
* ``nlopt``
* ``matplotlib``

Development, documentation, and build tools are exposed through optional extras
instead of being mixed into runtime installation.

Installation
------------

From a checkout:

.. code-block:: powershell

   python -m venv .venv
   .\.venv\Scripts\python -m pip install -U pip setuptools wheel
   .\.venv\Scripts\python -m pip install -e .

On macOS or Linux:

.. code-block:: bash

   python -m venv .venv
   . .venv/bin/activate
   python -m pip install -U pip setuptools wheel
   python -m pip install -e .

For development:

.. code-block:: bash

   python -m pip install -r requirements-dev.txt

Quick Start
-----------

Python uses zero-based parameter indexes.  The example below computes the
confidence interval for the first parameter component, ``x[0]``.

.. code-block:: python

   from likelihoodprofiler import get_interval

   def loss(x):
       return 5.0 + (x[0] - 3.0) ** 2 + (x[0] - x[1] - 1.0) ** 2 + 0 * x[2] ** 2

   result = get_interval(
       [3.0, 2.0, 2.1],
       0,
       loss,
       "LIN_EXTRAPOL",
       loss_crit=9,
   )

   result.plot()

Validation
----------

Run the unit test suite:

.. code-block:: bash

   python -m pytest

Build the documentation:

.. code-block:: bash

   sphinx-build -d .doctrees -b html docs site

Build source and wheel distributions:

.. code-block:: bash

   python -m build
   python -m twine check dist/*

The same checks are wired into GitHub Actions for supported Python versions.

Compatibility Notes
-------------------

* Supported Python versions are 3.10 and newer.
* ``nlopt`` is a compiled dependency.  Modern releases publish wheels for common
  Python/platform combinations; if a wheel is unavailable for a platform, a
  local compiler toolchain may be required.
* The package source and tests intentionally remain close to the historical
  port.  Infrastructure updates should avoid changing numerical behavior unless
  the change is covered by tests and compared against the Julia upstream.

Documentation
-------------

Hosted documentation for this repository is available at
https://insysbio.github.io/LikelihoodProfiler.py/.

The upstream Julia package is documented at
https://insysbio.github.io/CICOBase.jl/latest/.

Citation
--------

Borisov I, Metelkin E (2020) Confidence intervals by constrained optimization:
An algorithm and software package for practical identifiability analysis in
systems biology. PLoS Computational Biology 16(12): e1008495.

Reference: https://doi.org/10.1371/journal.pcbi.1008495

License
-------

MIT. See ``LICENSE``.
