# [Code Style](https://docs.python-guide.org/writing/style/)

Python vs JavaScript:

[Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js)




## [General concepts](https://docs.python-guide.org/writing/style/#general-concepts)

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













The following sub-sections are personal and not part of "The Hitchhiker's Guide to Python".

### Swap For loops with Functional Paradigms

Todo: 

https://stackoverflow.com/questions/1892324/why-program-functionally-in-python

### Replace If Statements with Dictionary

[Using a dictionary](https://www.youtube.com/watch?v=z726s8J8HmI) instead of `if`s and `else`s creates a functional, declaritive and polymorphic coding style rather than imperative and procedural.

### Slicing Sequences



Todo: Carry on here ....... Work through all the slicing parts in Effective Pyton. Chapter 2 has several items ........................





"Effective Python (2nd Edition) Item 11: Know How to Slice Sequences" Provides examples of slicing sequences.

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
* arrays - Or custom class objects that implement sequence methods `__getitem__()` and `__len__()`. Details on slicing arrays [here](https://www.askpython.com/python/array/array-slicing-in-python)
* `str`
* `tuple`
* `range`
* `dict` - Details on slicing [here](https://stackoverflow.com/questions/29216889/slicing-a-dictionary)
* [`bytes`, `bytearray`](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) - Details on slicing [here](https://www.dotnetperls.com/bytes-python) (search "slice")

All of the built-in sequence types are detailed [here](https://docs.python.org/3/library/stdtypes.html).

#### Other Resources




