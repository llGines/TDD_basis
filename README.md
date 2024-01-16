
# Learn Testing
Project destined to show how to delevop following the Test Driven Development (TDD) paradigm.

## Test Driven Development (TDD)
TDD is a philosophy that consists of first programming the tests that a code must pass, and then programming
it according to those tests. This produces robust and optimized code.

TDD is buildt over two pillars: testing and coverage

## Testing

In iPronics we use the [pytest](https://docs.pytest.org/en/7.4.x/) library for testing.


Read our wiki about [testing](https://github.com/iPronics/iPronics-PRL/wiki/Intro-to-automated-testing)

## Coverage
[Coverage](https://coverage.readthedocs.io/en/7.4.0/) is the measure of how much code has been tested.

# Instructions
Clone this repo with "git clone git clone git@github.com:llGines/checkCalcCoverage.git --depth=1"

navigate to parent folder and install this project with 
```python3 -m pip install -e .```

When write tests, **Test** files must start with ```test_``` or end with ```_test```

run test with pytest and coverage with:
```pytest --cov-report term-missing --cov=learn_testing```

Here you will see the results of your tests and the coverage you managed. 

=======
# TDD_Exercices
Inside ```src\learn_testing```there are three directories:

```calc```: this directori has a file that realizes the mos common arithmetics operations. The tests for this program cam be seen in ```\test\test_calc``` as example

```area```: this directori is for writing a progrom with calculate the area for a rectangle, a triangle, a circle and hexagon. The code must be written for satisfiying the test written in ```\test\test_area```.

```mymates```: here, only a list with the name of your colleages are provided. First, you must write the tests following the hints in ```\test\test_list```. As second step, you must write the code that satisfies this tests.

====

If you get stuck, you can have a (quick) look to the cheat sheet in the directory root.

