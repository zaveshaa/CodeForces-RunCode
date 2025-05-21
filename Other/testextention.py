a = 9
n = 9

def f(a: int) -> Any:
    print(a)
f(a)

def count_up_to(n: int) -> None:
    i = 1
    while i <= n:
        yield i
        i += 1
