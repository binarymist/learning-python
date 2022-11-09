# [Documentation](https://docs.python-guide.org/writing/documentation/)

## [Project Documentation](https://docs.python-guide.org/writing/documentation/#project-documentation)

## [Project Publication](https://docs.python-guide.org/writing/documentation/#project-publication)

### [Sphinx](https://docs.python-guide.org/writing/documentation/#sphinx)

[Sphinx](https://www.sphinx-doc.org/) is far and away the most popular Python documentation tool. Use it. It converts reStructuredText markup language into a range of output formats including HTML, LaTeX (for printable PDF versions), manual pages, and plain text.

There is also great, free hosting for your Sphinx docs: [Read The Docs](http://readthedocs.org/). Use it. You can configure it with commit hooks to your source repository so that rebuilding your documentation will happen automatically.

## [Code Documentation Advice](https://docs.python-guide.org/writing/documentation/#code-documentation-advice)

In Python, docstrings describe modules, classes, and functions:

```python
def square_and_rooter(x):
    """Return the square root of self times self."""
    ...
```

### [Docstrings and Magic](https://docs.python-guide.org/writing/documentation/#docstrings-and-magic)

Docstrings can be used to embed unit test logic. [Doctest](https://docs.python.org/3/library/doctest.html) will read all embedded docstrings that look like input from the Python commandline (prefixed with `>>>`) and run them, checking to see if the output of the command matches the text on the following line.

