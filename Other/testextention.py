def example(x: Any) -> int | str:
    if x > 0:
        return 42
    else:
        return 'not found'
a = [1, 2, 3]
b = {'key': 42}
c = {1, 2, 3}
d = (1, 'two')
e = example(10)
