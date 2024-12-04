def p1(input):
    word = "XMAS"
    ans = 0
    word_len = len(word)
    rows = len(input)
    cols = len(input[0]) if rows > 0 else 0

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            # Horizontal right
            if j + word_len <= cols and input[i][j : j + word_len] == word:
                ans += 1
            # Horizontal left (reversed)
            if j - word_len >= -1 and input[i][j - word_len + 1 : j + 1] == word[::-1]:
                ans += 1
            # Vertical down
            if i + word_len <= rows:
                if all(input[i + k][j] == word[k] for k in range(word_len)):
                    ans += 1
            # Vertical up (reversed)
            if i - word_len >= -1:
                if all(input[i - k][j] == word[k] for k in range(word_len)):
                    ans += 1
            # Diagonal down-right
            if i + word_len <= rows and j + word_len <= cols:
                if all(input[i + k][j + k] == word[k] for k in range(word_len)):
                    ans += 1
            # Diagonal up-left (reversed)
            if i - word_len >= -1 and j - word_len >= -1:
                if all(input[i - k][j - k] == word[k] for k in range(word_len)):
                    ans += 1
            # Diagonal down-left
            if i + word_len <= rows and j - word_len >= -1:
                if all(input[i + k][j - k] == word[k] for k in range(word_len)):
                    ans += 1
            # Diagonal up-right (reversed)
            if i - word_len >= -1 and j + word_len <= cols:
                if all(input[i - k][j + k] == word[k] for k in range(word_len)):
                    ans += 1

    return ans


def p2(input):
    ans = 0

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if (
                char == "A"
                and i + 1 < len(input)
                and j + 1 < len(line)
                and i - 1 >= 0
                and j - 1 >= 0
                and "".join(sorted(input[i + 1][j - 1] + input[i - 1][j + 1])) == "MS"
                and "".join(sorted(input[i + 1][j + 1] + input[i - 1][j - 1])) == "MS"
            ):
                ans += 1

    return ans
