from sandbox.tasks import add

result = add.delay(4, 4)
print(result.ready())
print(result.get(propagate=False))