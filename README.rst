SimpleNote -> Jekyll
====================

This is an integration script between Jekyll blog format and SimpleNote_ notes tagged with ``blog``.

Install
-------

- Install pipsi_
- Run ``pipsi install simplenote_jekyll``

Setup
-----

Set the following environment variables:

:``SIMPLENOTE_USER``: Username (email) for your SimpleNote_ account
:``SIMPLENOTE_PASSWD``: Password for your SimpleNote_ account

Use
---

Change directory to the base of your Jekyll blog, then run ``sn-export``. Running ``git status`` should show you what posts are newly imported from SimpleNote_.

.. _SimpleNote: https://www.simplenote.com/
.. _pipsi: https://github.com/mitsuhiko/pipsi
