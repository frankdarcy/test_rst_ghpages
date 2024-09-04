A C
===

Overview
--------

Test docs

.. uml::
    :scale: 100%

    interface I1
    interface I2
    component X

    X ..> [libA] : uses
    X ..> [libB] : uses
    X -left- I1
    X -right- I2
