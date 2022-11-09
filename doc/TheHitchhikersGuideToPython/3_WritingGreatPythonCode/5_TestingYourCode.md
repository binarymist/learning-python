# [Testing Your Code](https://docs.python-guide.org/writing/tests/#testing-your-code)

## [The Basics](https://docs.python-guide.org/writing/tests/#the-basics)

### [unittest](https://docs.python-guide.org/writing/tests/#unittest)

unittest is the batteries-included test module in the Python standard library. Similar to NUnit.

### [Doctest](https://docs.python-guide.org/writing/tests/#doctest)

Also discussed [here](../3_WritingGreatPythonCode/4_Documentation.md#docstrings-and-magic.md)

## [Tools](https://docs.python-guide.org/writing/tests/#tools)

### [py.test](https://docs.python-guide.org/writing/tests/#py-test)

[py.test](https://docs.pytest.org/en/latest/) is a no-boilerplate alternative to Python’s standard unittest module. py.test is easier to setup, easier to write tests, no inheritance required, runs tests in parallel.

Mocking provided by [pytest-mock](https://pypi.org/project/pytest-mock/).

### [Hypothesis](https://docs.python-guide.org/writing/tests/#hypothesis)

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a property-based test library.

Hypothesis is practical as well as very powerful and will often find bugs that escaped all other forms of testing. It integrates well with py.test, and has a strong focus on usability in both simple and advanced scenarios.

### [tox](https://docs.python-guide.org/writing/tests/#tox)

[tox](https://tox.wiki/en/latest/) is a tool for automating test environment management and testing against multiple interpreter configurations.

