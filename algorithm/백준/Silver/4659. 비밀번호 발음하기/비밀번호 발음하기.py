import sys

vowels = ["a", "e", "i", "o", "u"]


def check(t):
    n = len(t)
    is_contain_vowel = False
    for i in range(n):
        if t[i] in vowels:
            is_contain_vowel = True

        if (
                i + 2 < n
                and ((t[i] in vowels and t[i + 1] in vowels and t[i + 2] in vowels)
                     or (t[i] not in vowels and t[i + 1] not in vowels and t[i + 2] not in vowels))
        ):
            print(f"<{t}> is not acceptable.")
            return

        # 3번 조건
        if i + 1 < n and t[i] == t[i + 1] and t[i: i + 2] not in ["ee", "oo"]:
            print(f"<{t}> is not acceptable.")
            return

    # 1번 조건
    if not is_contain_vowel:
        print(f"<{t}> is not acceptable.")
        return

    print(f"<{t}> is acceptable.")
    return


while True:
    t = sys.stdin.readline().rstrip()
    if t == "end":
        break

    check(t)
