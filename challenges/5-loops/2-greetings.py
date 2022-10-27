def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings


print(add_greetings(["Owen", "Max", "Sophie"]))
