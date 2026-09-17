def longest_non_repeating(s):
    length = 0
    window = set()
    left = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        length = max(length, right-left+1)
    return length

s = input()
print(longest_non_repeating(s))


