
def isAllTrue(tuple):
    return all(tuple)


def main():
    true = (2, "wordle", True)
    false = (0, "wow", True)
    print(isAllTrue(true))
    print(isAllTrue(false))
