# Beyond 100% test coverage

*A.K.A.*

- Why 100% test coverage is not good enough
- Typing + Unit tests

# About me and the demo

<https://fluid.quest/pyconse2022>

## Problem statement

A CLI tool which

- Read a CSV file containing a list of cities and their founding year
- Does some operation, for example, printing the result

# How does `typing` help you?

- Find edge cases such as type inconsistencies
- Sniff out issues with branches (if-else statements) and mutations in your code

# Is `typing` a replacement for tests?

No! Typing will not ensure:

- Validation or correctness of your code
- Regressions won't happen in the future

A good test suite is still required to avoid such problems


## Bonus

- [`pyupgrade`](https://pypi.org/project/pyupgrade/): Let's you quickly transition to type hinting generics in Python 3.9+
- `stubgen`: CLI tool to generate 


## Thanks

![SMHI](https://www.smhi.se/polopoly_fs/1.117503.1490015865!/image/smhi-logo-120.png_gen/derivatives/Original/image/smhi-logo-120.png)
