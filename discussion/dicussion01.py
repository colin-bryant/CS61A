# Q1: Race
def race(x,y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.
    >>> race(5, 7) # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x  and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise,hare,minutes=0,0,0
    while minutes == 0 or tortoise - hare:
        tortoise=tortoise + x
        if minutes % 10 <  5:
            hare=hare +y
        minutes = minutes + 1
    return minutes
c=race(2, 4)
# print(c)
# Q2 : FizzBuzz
# • If i is divisible by both 3 and 5, print fizzbuzz.
# • If i is divisible by 3 (but not 5), print fizz.
# • If i is divisible by 5 (but not 3), print buzz.
# • Otherwise, print the number i.
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1
    while i<=n:
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1
result=fizzbuzz(16)
print(result)
