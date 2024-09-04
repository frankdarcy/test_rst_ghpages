Test RST
========

Minimal RST docs to test building and deploying in github pages.
The project source is `here <https://github.com/frankdarcy/test_rst_ghpages>`_.

.. toctree::
    :maxdepth: 1
    :caption: Dir 1
    :glob:
    :hidden:

    ../dir1/**/doc/index

.. toctree::
    :maxdepth: 1
    :caption: Dir A
    :glob:
    :hidden:

    ../dirA/**/doc/index
