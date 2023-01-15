# [Code Style](https://docs.python-guide.org/writing/style/)

Python vs JavaScript:

[Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js)

## [General concepts](https://docs.python-guide.org/writing/style/#general-concepts)

### [Function arguments](https://docs.python-guide.org/writing/style/#function-arguments)

**Positional** (mandatory) arguments have no default values.  
Must be specified before keyword arguments.  
You can also name the arguments, in which case you can also switch the order if you wanted to.  
For the following routine signatures:  
`send(message, recipient)` or `point(x, y)`  
You could invoke them like:  
`send(recipient='World', message='Hello')` or `point(y=2, x=1)`

**Keyword** are not mandatory and have default values. Often used for optional parameters sent to the function.  
Beware of the using default arguments that are mutable [gotcha](./7_CommonGotchas.md#mutable-default-arguments).

Think more carefully about using either of the following two argument techniques:

**Arbitrary argument list** (`*args`)  
Optional positional arguments are always turned into a tuple before they are passed to the function.  
Effective Python - Item 22 calls these Variable (optional) Positional Arguments.  

**Arbitrary keyword argument dictionary** (`**kwargs`)  
In the function body, kwargs will be a dictionary of all the passed named arguments that have not been caught by other keyword arguments in the function signature.  
Effective Python - Item 23 discusses keyword arguments.

### Avoid the magical wand

### We are all responsible users

The main convention for private properties and implementation details is to prefix all “internals” with an underscore.

### Returning values

## [Idioms](https://docs.python-guide.org/writing/style/#idioms)

### Unpacking

Python has a very powerful tuple assignment feature that allows a tuple of variables on the left of an assignment to be assigned values from a tuple on the right of the assignment.

Code like the following, which was taken from [Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/#regular-expressions-in-python-and-javascript) is valid:

```python
...
start, end = match.start(), match.end()
```

* [Tuple Assignment](https://runestone.academy/ns/books/published/thinkcspy/Lists/TupleAssignment.html)

"Python for JavaScript Developers" has some other unpacking examples, such as:

* `dict` unpacking which is similar to JavaScript spread
* Union operator for dictionaries

### [Create an ignored variable](https://docs.python-guide.org/writing/style/#create-an-ignored-variable)

Use double underscore `__` for ignored/throwaway variables.

### Create a length-N list of the same thing

### Create a length-N list of lists

### Searching for an item in a collection

## [PEP8](https://docs.python-guide.org/writing/style/#pep-8)

* PEP 8 is the de facto code style guide for Python
* pep8.org is the easier to read PEP 8 style guide for Python

Linting tools:

* Pylint
* Flake8
* mypy
* pycodestyle (pep8)

[Setting up linting in VS Code](https://code.visualstudio.com/docs/python/linting)

### Auto-Formatting

Pylint is [configurable](https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html). Google has a [Python Style Guide](https://google.github.io/styleguide/pyguide.html), which also uses Pylint, and provides a [pylintrc](https://google.github.io/styleguide/pylintrc) file under the [2.1 Lint subsection](https://google.github.io/styleguide/pyguide.html#s2.1-lint).
The internal Google style guide mandates 2 spaces. Google's externaly-published style guide says 4, consistent with PEP 8.
Google's [pylintrc](https://google.github.io/styleguide/pylintrc) uses 2 spaces, for conformity with many open-sourced Google projects (like TensorFlow).

## [Conventions](https://docs.python-guide.org/writing/style/#conventions)

### [Check if a variable equals a constant](https://docs.python-guide.org/writing/style/#check-if-a-variable-equals-a-constant)

[Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

```python
# Just check the value
if attr:
    print('attr is truthy!')

# or check for the opposite
if not attr:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if attr is None:
    print('attr is None!')
```

### [Access a Dictionary Element](https://docs.python-guide.org/writing/style/#access-a-dictionary-element)

```python
d = {'hello': 'world'}

# Bad
if d.has_key('hello'):
    print(d['hello'])    # prints 'world'
else:
    print('default_value')
    
# Good
print(d.get('hello', 'default_value')) # prints 'world'
print(d.get('thingy', 'default_value')) # prints 'default_value'

# Or:
if 'hello' in d:
    print(d['hello'])
```

### [Short Ways to Manipulate Lists](https://docs.python-guide.org/writing/style/#short-ways-to-manipulate-lists)

### [Filtering a list](https://docs.python-guide.org/writing/style/#filtering-a-list)

Use a list comprehension or generator expression.

[List comprehensions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions) provides a powerful, concise way to work with lists.

[Generator expressions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions) follows almost the same syntax as list comprehensions but return a generator instead of a list.

```python
# comprehensions create a new list object
filtered_values = [value for value in sequence if value != x]

# generators don't create another list
filtered_values = (value for value in sequence if value != x)
```

### [Modifying the values in a list](https://docs.python-guide.org/writing/style/#modifying-the-values-in-a-list)

### [Read From a File](https://docs.python-guide.org/writing/style/#read-from-a-file)

### [Line Continuations](https://docs.python-guide.org/writing/style/#line-continuations)

* Not so good: **Backslash** (`\`) at the end of the line without any horizontal white space (` `) following it
* Better: Use **parentheses** around your elements. Left with an unclosed parenthesis on an end-of-line, the Python interpreter will join the next line until the parentheses are closed. The same behaviour holds for curly and square braces

Having to split a long logical line is usually a sign that you are trying to do too many things at the same time.

## [Zen of Python](https://docs.python-guide.org/writing/style/#zen-of-python)

Also known as [PEP 20](https://www.python.org/dev/peps/pep-0020), the guiding principles for Python’s design.

## [PEP 8](https://docs.python-guide.org/writing/style/#pep-8)

* [PEP 8](https://peps.python.org/pep-0008/) is the de facto code style guide for Python
* Effective Python (2nd Edition) - Item 2: Should be read with this

### [Auto-Formatting](https://docs.python-guide.org/writing/style/#auto-formatting)

## [Conventions](https://docs.python-guide.org/writing/style/#conventions)


## Personal

The following sub-sections are personal and not part of "The Hitchhiker's Guide to Python".

### Other Resources

[Built-in Functions](https://docs.python.org/3/library/functions.html)

### Swap For loops with Functional Paradigms

This Stackoverflow post [Why program functionally in Python?](https://stackoverflow.com/questions/1892324/why-program-functionally-in-python) is thought provoking. The accepted answer with examples discusses:

* "_lambda, even more so map (and filter), and most especially reduce, are hardly ever the right tool for the job in Python_"
* "_Perfectly proper functional approaches in Python often include [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions), [generator expressions](https://docs.python.org/3/tutorial/classes.html#generator-expressions)_" (follows almost the same syntax as list comprehensions but return a generator instead of a list), "_itertools, higher-order functions_"
* "_itertools, does include imap and ifilter: the difference is that, like all of itertools, these are stream-based (like map and filter builtins in Python 3, but differently from those builtins in Python 2)_"
* "_So, summarizing...: anything you can code with lambda, map, and filter, you can code (more often than not advantageously) with def (named functions) and listcomps -- and usually moving up one notch to generators, generator expressions, or itertools, is even better_"

Then the comments discuss other techniques, but without examples, so with less weight IMHO.

This [Functional Programming in Python: When and How to Use It](https://realpython.com/python-functional-programming/) is also well worth reading and playing with the examples after reading the above Stackoverflow post. In some cases it shows you how to use map(), filter() and reduce(), but as the Stackoverflow discussion points out, often simpler pythonic approaches are shorter, easier to understand and make more sense.

An example of [Applying a Function to an Iterable With map()](https://realpython.com/python-functional-programming/#applying-a-function-to-an-iterable-with-map)

```
>>> "+".join(map(str, [1, 2, 3, 4, 5]))
'1+2+3+4+5'
```

and how to do the same thing in a more pythonic way with list comprehension:

```
>>> "+".join([str(num) for num in [1, 2, 3, 4, 5]])
'1+2+3+4+5'
```

<br>

"Effective Python (2nd Edition)" has:

* Item 27 Use Comprehensions Instead of map and filter
* Item 36: Consider itertools for Working with Iterators and Generators



### Replace If Statements with Dictionary

[Using a dictionary](https://www.youtube.com/watch?v=z726s8J8HmI) instead of `if`s and `else`s creates a functional, declaritive and polymorphic coding style rather than imperative and procedural.

### Slicing Sequences

Good places to start:

* "Effective Python (2nd Edition) Item 11: Know How to Slice Sequences" Provides examples of slicing sequences
* "Effective Python (2nd Edition) Item 12: Avoid Striding and Slicing in a Single Expression"
* "Effective Python (2nd Edition) Item 13: Prefer Catch-All Unpacking Over Slicing" Which covers catch-all unpacking via starred expressions


There is also the [`slice`](https://docs.python.org/3/library/functions.html#slice) built-in function which works [like so](https://www.tutorialsteacher.com/python/slice-method):

```python
mystr = 'TutorialsTeacher'
nums = [1,2,3,4,5,6,7,8,9,10]

portion1 = slice(9)
portion2 = slice(2, 8, 2)   

print('slice: ', portion1)
print('String value: ', mystr[portion1])
print('List value: ', nums[portion1])

print('slice: ', portion2)
print('String value: ', mystr[portion2])
print('List value: ', nums[portion2])
```

Types that can be sliced:

* `list`
* arrays - Or custom class objects that implement sequence methods `__getitem__()`, `__setitem__()` and `__len__()`, ideally as well as other methods from the abstract base class `Sequence` of the built-in module [`collections.abc`](https://docs.python.org/3/library/collections.abc.html), as detailed in Effective Python (2nd Edition) Item 43.
  Details on slicing arrays [here](https://www.askpython.com/python/array/array-slicing-in-python)
* `str`
* `tuple`
* `range`
* `dict` - Details on slicing [here](https://stackoverflow.com/questions/29216889/slicing-a-dictionary)
* [`bytes`, `bytearray`](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) - Details on slicing [here](https://www.dotnetperls.com/bytes-python) (search "slice")

All of the built-in sequence types are detailed [here](https://docs.python.org/3/library/stdtypes.html).

#### Other Resources

* [Use Cases for Asterisks](https://betterprogramming.pub/understand-the-versatility-of-asterisks-in-python-know-8-use-cases-722bff20e84c)
* [Iterables](https://realpython.com/python-for-loop/#iterables)
