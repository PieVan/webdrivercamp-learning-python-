#!/usr/bin/python3

def calc_weight(list_=[]):
    if len(list_) == 0:
        return 0
    else:
        temp_score = sum(map(lambda score: score[0] * score[1],list_))
        temp_weight = sum(map(lambda weight: weight[1],list_))

    return temp_score/temp_weight


if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
