# [Structuring Your Project](https://docs.python-guide.org/writing/structure/)

## [Object-oriented programming](https://docs.python-guide.org/writing/structure/#object-oriented-programming)

In JavaScript everything exect the following [_primitive_](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)s are objects: `null`, `undefined`, `string`, `number`, `bigint`, `boolean` and `symbol`

_In Python, everything is an object_. _Functions, classes, strings, and even types are objects in Python: like any object, they have a type, they can be passed as function arguments, and they may have methods and properties._

There are no built-in primitives.

_The way Python handles modules and namespaces gives the developer a natural way to ensure the encapsulation and separation of abstraction layers, both being the most common reasons to use object-orientation. Therefore, Python programmers have more latitude as to not use object-orientation, when it is not required by the business model._

## [Decorators](https://docs.python-guide.org/writing/structure/#decorators)

Effective Python (2nd Edition) - Item 26: Should be read with this. It specifies that `functools.wraps` should be used when creating decorator functions. This also assumes you understand [`*args` and `**kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html)

## [Context Managers](https://docs.python-guide.org/writing/structure/#context-managers)

Are used with `with` statements such as:

```python
with open('file.txt') as f:
    contents = f.read()
```

* The first example context manager uses a class.  
  [book.pythontips.com - context_managers](https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-class) also covers this
* The second example context manager uses a generator, decorated with `contextmanager` from Python's `contextlib`.  
  Both of the following resource also cover this:
  * Effective Python (2nd Edition) - Item 66
  * [book.pythontips.com - context_managers](https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-generator)

## [Dynamic typing](https://docs.python-guide.org/writing/structure/#dynamic-typing)

_Variables_ in Python _are not a segment of the computer’s memory where some value is written, they are ‘tags’ or ‘names’ pointing to objects._

```python
a = 1
# a now points to an integer object
a = 2
# a now points to a different integer object
```

Unlike in JavaScript where if you declare and/or define a variable anywhere without using `var`, `let` or `const` it will become global, in Python there is no prefix required and where ever you ~~declare~~ define a variable will be it's scope.

In Python the concept of declaring a variable (for built-in types) before using it doesn't exist, you just define or assign it (ex: `a = 1`). Arrays need to be defined because they are not built-in types, as can be seen in the link below "lists vs arrays".

A variable which is defined inside a function is local to that function

## [Mutable and immutable types](https://docs.python-guide.org/writing/structure/#mutable-and-immutable-types)

_Typical mutables are lists and dictionaries_.

_Immutable types provide no method for changing their content._

_Mutable types are not “stable”, and therefore cannot be used as dictionary keys._

_Using properly mutable types for things that are mutable in nature and immutable types for things that are fixed in nature helps to clarify the intent of the code._

[built-in types](https://www.guru99.com/mutable-and-immutable-in-python.html#9) (unless specified otherwise):

* mutable: `list`, arrays (Array data structures need to be imported via NumPy package or array module, so arrays are not actually built-ins), `dict`, `set`
* immutable: [`tuple`](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences), [`int`, `float`, `complex`](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex), [`NoneType`](https://www.pythontutorial.net/advanced-python/python-none/) (`None` is a special object of the `NoneType` class), `bool`, `str`, `frozenset`

[lists vs arrays](https://learnpython.com/blog/python-array-vs-list/)

Joining strings with list comprehensions:

Bad
```python
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
    nums += str(n)   # slow and inefficient
print(nums)
```

Better
```python
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = []
for n in range(20):
    nums.append(str(n))
print("".join(nums))  # much more efficient
```

Best
```python
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print("".join(nums))
```

_With strings, using `join()` is not always best. In the instances where you are creating a new string from a pre-determined number of strings, using the addition operator is actually faster. But in cases like above or in cases where you are adding to an existing string, using `join()` should be your preferred method._

```python
foo = 'foo'
bar = 'bar'

foobar = foo + bar  # This is good
foo += 'ooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'ooo'])
```
