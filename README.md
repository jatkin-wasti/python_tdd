# Test Driven Development
## Types of testing
- Unit testing: Testing an individual component of a larger project
- Integration testing: Testing the combined components together
### Python has several modules that we can use to test our code
- pytest
- unittest
#### Why TDD?
- Releasing a product that hasn't been properly tested can lead to financial loss or in some cases loss to life
- TDD helps us minimise the risk of failure when sending a product to production
- TDD is focused on creating tests BEFORE creating the functionality of a program
![TDD Diagram](TDD_image.png)
#### Steps
- We will create a file to write our tests
- We will run the test they will all fair
- We will create a file to write our code
- We will refactor and add the code to pass the tests
#### Naming convention for test files and methods
- file name: simple_calc
- test name: test_simple_calc
- Naming our functions correctly is important for the modules to recognise it as a test for the relevant function

**Installing the testing framework**
- Use pip to install the testing module required

```pip install pytest```
- Running tests in the terminal uses

```python -m pytest```
- The -m specifies the module, which in this case is pytest
- Or you can run the file normally and check the details of passed/failed tests in the Pycharm Run tab
- This gives us a breakdown of all of the tests

```python -m unittest discover -v```
- This  gives a more detailed view of the pytest results
- The -v stands for verbose
```pytest -v```
**How does pytest work?**
- pytest looks for the files starting with ```test_``` and ending with ```_test```
## Creating files to demonstrate TDD
- Importing our classes and modules
```
from simple_calc import SimpleCalc
import unittest
import pytest
```
- Creating the class that inherits from the unittest framework
- And creating an object of the imported class to use during testing
```
class CalcTest(unittest.TestCase):  # unittest.TestCase works with unittest frame work as a parent class
    # Creating an object of our class
    calc = SimpleCalc()
```
- The tests for our calculator
```
    def test_add(self):
        # What are we asking python to test for us?
        # We are asking python to test/check if 2+4 = 6 If True pass the test if False fail the test
        self.assertEqual(self.calc.add(2, 4), 6)  # boolean returned

    def test_subtract(self):
        # Testing if 4 - 2 = 2 If True pass the test if False fail the test
        self.assertEqual(self.calc.subtract(4, 2), 2)  # boolean returned

    def test_multiple(self):
        # Testing if 2 * 2 = 4 If True pass the test if False fail the test
        self.assertEqual(self.calc.multiply(2, 2), 4)  # boolean returned

    def test_divide(self):
        # Testing if 9 / 3 = 3 If True pass the test if False fail the test
        self.assertEqual(self.calc.divide(9, 3), 3)  # boolean returned
```
- We can use different conditions with assertEquals as needed