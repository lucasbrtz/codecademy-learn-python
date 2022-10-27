def win_percentage(wins, losses):
    return (100 * wins) / (wins + losses)


print(win_percentage(5, 5))
print(win_percentage(10, 0))
