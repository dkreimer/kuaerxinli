# File that holds different functions that process a score object to spit out the final value

def addition(score):
    return score.score

def average(score):
    total_q = score.result.question_set.count()
    return float(score.score) / float(total_q)

PROCESS_DICT = {
    "ADD": addition,
    "AVG": average,
}