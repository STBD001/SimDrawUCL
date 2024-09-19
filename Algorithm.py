import random

# Define the pots
pot_1 = {'Real Madryt': 'ESP', 'Manchester City': 'ENG', 'Bayern Monachium': 'GER', 'Paris Saint-Germain': 'FRA',
         'Liverpool': 'ENG', 'Inter': 'ITA', 'Borussia Dortmund': 'GER', 'RB Lipsk': 'GER', 'FC Barcelona': 'ESP'}

pot_2 = {'Bayer Leverkusen': 'GER', 'Atletico Madryt': 'ESP', 'Atalanta Bergamo': 'ITA', 'Juventus': 'ITA',
         'Benfica': 'POR', 'Arsenal': 'ENG', 'Club Brugge': 'BEL', 'Szachtar Donieck': 'UKR', 'AC Milan': 'ITA'}

pot_3 = {'Feyenoord': 'NLD', 'Sporting CP': 'POR', 'PSV': 'NLD', 'Dinamo Zagrzeb': 'CRO', 'RB Salzburg': 'AUT',
         'Lille': 'FRA', 'Crvena zvezda': 'SRB', 'Young Boys Berno': 'SUI', 'Celtic Glasgow': 'SCO'}

pot_4 = {'Slovan Bratysława': 'SVK', 'AS Monaco': 'FRA', 'Sparta Praga': 'CZE', 'Aston Villa': 'ENG',
         'Bologna FC 1909': 'ITA', 'Girona FC': 'ESP', 'VfB Stuttgart': 'GER', 'Sturm Graz': 'AUT',
         'Stade Brestois 29': 'FRA'}

all_teams = {**pot_1, **pot_2, **pot_3, **pot_4}


def draw_simplified():
    matches = {team: [] for team in all_teams}
    pots = [pot_1, pot_2, pot_3, pot_4]
    num_opponents = 8

    for team in all_teams:
        while len(matches[team]) < num_opponents:
            possible_opponents = []
            for pot in pots:
                if team in pot:
                    continue
                possible_opponents += [
                    opponent for opponent in pot
                    if all_teams[opponent] != all_teams[team] and len(matches[opponent]) < num_opponents
                       and opponent not in matches[team]  # Ensure no duplicate opponents
                ]


            if not possible_opponents:
                return draw_simplified()


            opponent = random.choice(possible_opponents)
            matches[team].append(opponent)
            matches[opponent].append(team)

    return matches


def print_matches(matches):
    for team, opponents in matches.items():
        print(f"{team} zagra przeciwko: {', '.join(opponents)}\n")