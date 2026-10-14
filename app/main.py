
def calculate_team_total_rating(team: list):
    score = 0
    for player in team:
        score += player.get_rating()
    return score


def elves_concert(band):
    for dude in band:
        dude.play_elf_song()


def feast_of_the_dwarves(cohort):
    for bro in cohort:
        bro.eat_favourite_dish()
