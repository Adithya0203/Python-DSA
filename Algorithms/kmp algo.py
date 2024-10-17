def computeLPS(pattern):
    n = len(pattern)
    lps = [0] * n
    i = 1
    length = 0

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    m = len(text)
    n = len(pattern)
    lps = computeLPS(pattern)

    i = 0
    j = 0
    while i < m:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == n:
            print("Pattern found at index", i - j)
            j = lps[j - 1]

        elif i < m and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    kmp(text, pattern)