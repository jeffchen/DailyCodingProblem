'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''
def stairCase(steps, n):
    # f(n) = f(n - 2) + f(n - 5) + f(n - 9), if steps = [2, 5, 9]
    stepList = []
    for i in xrange(n + 1):
        stepList.append(sum(stepList[i - j] for j in steps if i - j > 0))
        stepList[i] += 1 if i in steps else 0

    print stepList
    return stepList[-1]

steps = [2, 5, 9]
n = 10

print stairCase(steps, n)
