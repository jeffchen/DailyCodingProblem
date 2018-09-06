'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
def possibleDecodeCount(encodeStr):
    if len(encodeStr) == 1:
        return 1

    # first character -> always present 1 answer
    possibleCount = [1]
    # second character -> if first two characters > 26, it presents 1 answer(ex: 27, -> (2, 7))
    possibleCount.append(1) if int(encodeStr[0] + encodeStr[1]) > 26 else possibleCount.append(2)

    for i in xrange(2, len(encodeStr)):
        if int(encodeStr[i - 1] + encodeStr[i]) > 26:
            possibleCount.append(possibleCount[i - 1])
        else:
            possibleCount.append(possibleCount[i - 1] + possibleCount[i - 2])
    print possibleCount
    return possibleCount[-1]


print possibleDecodeCount("111")
