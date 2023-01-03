# [Common Gotchas](https://docs.python-guide.org/writing/gotchas/#common-gotchas)

## [Mutable Default Arguments](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments)

Python’s default arguments are evaluated once when the function is defined, not each time the function is called (like in most other languages).  
This means that if you use a mutable default argument and mutate it, you _will_ and have mutated that object for all future calls to the function as well.

Sometimes you can specifically leverage this behaviour to maintain state between calls of a function. This is often done when writing a caching function.

## [Late Binding Closures](https://docs.python-guide.org/writing/gotchas/#late-binding-closures)

The argument passed to the internal function is only done so on the final loop of the `for`. The solution funnily enough, is to use a default argument as just discussed above, this way the loop output is captured as the parameter.

```python
def create_multipliers():
    retVal = [lambda x : i * x for i in range(5)]
    return retVal

for multiplier in create_multipliers():
    print(multiplier(2))
```

Fix:

```python
def create_multipliers():
    retVal = [lambda x, y=i : y * x for i in range(5)]
    return retVal

for multiplier in create_multipliers():
    print(multiplier(2))
```

## [Bytecode (.pyc) Files Everywhere!](https://docs.python-guide.org/writing/gotchas/#bytecode-pyc-files-everywhere)

If you want these bytecode files to not be persisted, set `PYTHONDONTWRITEBYTECODE=1`
