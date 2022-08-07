# In terms of importing modules, both the following imports work, but the latter is preferred: https://docs.python-guide.org/writing/structure/#modules
# Good way to import module (technique 1):
#   from sample.core import hmm
# Best way to import module (technique 2):
#   import sample.core as samplecore
# In terms of importing a package: https://docs.python-guide.org/writing/structure/#packages
# technique 3
import sample

def main():
  # technique 1:
  #hmm()
  # technique 2:
  #samplecore.hmm()
  # technique 3:
  sample.hmm()
if __name__ == '__main__':
  main()

# To run this from command line, run the following:
# python3 main.py