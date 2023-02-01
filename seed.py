import random

def repeatable_random_values(seed, n):
    random.seed(seed)
    return [random.random() for _ in range(n)]

# Usage example
values = repeatable_random_values(42, 10)
print(values)

print(list(range(1, 21)))