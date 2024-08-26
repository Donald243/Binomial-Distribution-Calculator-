Binomial Distribution Calculator
This Python script calculates the probability of a specific number of successes in a series of independent trials using the binomial distribution formula. The script includes checks to ensure that all parameters meet the conditions required for a binomial distribution, such as a fixed number of trials, a constant probability of success, and independent trials.

Features:
Parameter Validation: Ensures that the number of trials, probability of success, and number of successes are valid inputs.
Binomial Probability Calculation: Uses the scipy.stats library to compute the probability mass function (PMF) for a given number of successes.
Formatted Output: Displays the result rounded to 2 significant figures for clarity.
Usage:
To use this script, simply modify the parameters (n, p, k) to fit your specific scenario:

n = number of trials (e.g., 10)
p = probability of success on each trial (e.g., 0.5)
k = number of successes of interest (e.g., 3)
Requirements:
Python 3.x
scipy library (pip install scipy)
