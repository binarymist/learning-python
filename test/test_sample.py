from context import sample # Notice the lack of '.' in front of context.

def test_something():
  sample.core.hmm()

def main():
  test_something()

if __name__ == '__main__':
  main()

# This (https://stackoverflow.com/questions/39134718/how-to-add-a-package-to-sys-path-for-testing) was useful for getting this to work.
# To run this from command line, run the following:
# python3 test/test_sample.py
