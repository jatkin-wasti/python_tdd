# Test Driven Development
## Types of testing
- Unit testing
- TDD
### Python has several modules that we can use to test our code
- pytest
- unittest
#### Why TDD?
- Releasing a product that hasn't been properly tested can lead to financial loss or in some cases loss to life
- TDD helps us minimise the risk of failure when sending a product to production
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

```pytest -v```