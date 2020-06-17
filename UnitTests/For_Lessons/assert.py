def avg(marks):
    assert len(marks) != 0
    return sum(marks) / len(marks)


mark1 = [1]
print("Average of mark1:", avg(mark1))


x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"