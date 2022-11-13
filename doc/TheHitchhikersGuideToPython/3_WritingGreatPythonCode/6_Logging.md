# [Logging](https://docs.python-guide.org/writing/logging/#logging)

From hardest to read documentation to easiest:

* [PEP 282](https://peps.python.org/pep-0282/)
* [`logging` Python doc](https://docs.python.org/3/library/logging.html)
* [Logging tutorial]

[loguru](https://github.com/Delgan/loguru) is an alternative approach for logging, nearly as simple as using a simple print statement.

## [Logging in a Library](https://docs.python-guide.org/writing/logging/#logging-in-a-library)

Notes for [configuring logging for a library](https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library) are in the [logging tutorial].
Because the user, not the library, should dictate what happens when a logging event occurs,
It is strongly advised that you do not add any handlers other than NullHandler to your library’s loggers.

## [Logging in an Application](https://docs.python-guide.org/writing/logging/#logging-in-an-application)

The twelve factor app, contains a section on [logging best practice](https://12factor.net/logs).
It emphatically advocates for treating log events as an event stream, and for sending that event stream to standard output to be handled by the application environment.

The docs cover three ways to configure a logger:

* Using an INI-formatted file
* Using a dictionary or a JSON-formatted file
* Using code
