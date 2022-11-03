"""В примере кода ниже генерируется список фиксаций состояния счета игры в течение матча.
Разработайте функцию get_score(game_stamps, offset), которая вернет счет на момент offset в списке game_stamps.
Нужно суметь понять суть написанного кода, заметить нюансы, разработать функцию вписывающуюся стилем в существующий код,
желательно адекватной алгоритмической сложности."""

from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    # for i in game_stamps:
    #     if i['offset'] == offset:
    #         return i['home'], i['away']
    start = 0
    end = len(game_stamps)
    mid = 0
    step = 0
    while start <= end:
        step += 1
        mid = (start + end) // 2

        if game_stamps[mid]['offset'] == offset:  # offset in middle - RETURN
            return game_stamps[mid]['score']['home'], game_stamps[mid]['score']['away']
        elif game_stamps[mid]['offset'] > offset:  # if offset in left side
            end = mid - 1
        elif game_stamps[mid]['offset'] < offset:  # if offset in right side
            start = mid + 1
    return game_stamps[mid]['score']['home'], game_stamps[mid]['score'][
        'away'], mid  # if searching offset is not in stamps list -> return the nearest offset data


print(get_score(game_stamps, 30))
