
def calculate_team_total_rating(team: list) -> int:
    score = 0
    for player in team:
        score += player.get_rating()
    return score


def elves_concert(band: list) -> None:
    for dude in band:
        dude.play_elf_song()


def feast_of_the_dwarves(cohort: list) -> None:
    for bro in cohort:
        bro.eat_favourite_dish()
