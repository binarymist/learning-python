# [Code Style](https://docs.python-guide.org/writing/style/)

Python vs JavaScript:

[Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js)




## [General concepts](https://docs.python-guide.org/writing/style/#general-concepts)




Todo: Discover and doc functional paradigms https://github.com/binarymist/learning-python/blob/main/doc/TheHitchhikersGuideToPython/3_WritingGreatPythonCode/2_CodeStyle.md#swap-for-loops-with-functional-paradigms
  Currently working through https://realpython.com/python-functional-programming/#applying-a-function-to-an-iterable-with-map .........................................
Todo: Carry on with https://www.valentinog.com/blog/python-for-js/#regular-expressions-in-python-and-javascript



Todo: Work through General concepts page




### [Function arguments](https://docs.python-guide.org/writing/style/#function-arguments)




#### Other Resources

[Built-in Functions](https://docs.python.org/3/library/functions.html)

## Idioms

### Unpacking

Python has a very powerful tuple assignment feature that allows a tuple of variables on the left of an assignment to be assigned values from a tuple on the right of the assignment.

Code like the following, which was taken from [Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/#regular-expressions-in-python-and-javascript) is valid:

```python
...
start, end = match.start(), match.end()
```

* [Tuple Assignment](https://runestone.academy/ns/books/published/thinkcspy/Lists/TupleAssignment.html)



## [PEP 8](https://docs.python-guide.org/writing/style/#pep-8)

* [PEP 8](https://peps.python.org/pep-0008/) is the de facto code style guide for Python
* Effective Python (2nd Edition) - Item 2: Should be read with this

### [Auto-Formatting](https://docs.python-guide.org/writing/style/#auto-formatting)

## [Conventions](https://docs.python-guide.org/writing/style/#conventions)











## Personal

The following sub-sections are personal and not part of "The Hitchhiker's Guide to Python".

### Swap For loops with Functional Paradigms

This Stackoverflow post [Why program functionally in Python?](https://stackoverflow.com/questions/1892324/why-program-functionally-in-python) is thought provoking. The accepted answer with examples discusses:

* "_lambda, even more so map (and filter), and most especially reduce, are hardly ever the right tool for the job in Python_"
* "_Perfectly proper functional approaches in Python often include list comprehensions, generator expressions, itertools, higher-order functions_"
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


