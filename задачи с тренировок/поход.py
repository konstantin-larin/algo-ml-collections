import sys

def main():
    river = input()

    dp_left = 0    # стартуем слева
    dp_right = 1   # чтобы встать справа перед началом — 1 переправа

    for ch in river:
        stay_left = 1 if ch in ('L', 'B') else 0
        stay_right = 1 if ch in ('R', 'B') else 0

        new_left  = min(dp_left,  dp_right + 1) + stay_left
        new_right = min(dp_right, dp_left  + 1) + stay_right

        dp_left, dp_right = new_left, new_right

    # в конце нужно оказаться на правом берегу
    return min(dp_right, dp_left + 1)

if __name__ == "__main__":
    print(main())
