'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
def findMinimumRooms(arr):
    arr = sorted(arr)
    minRooms = 0

    print arr

    for i in xrange(len(arr)):
        occupiedRooms = 0
        for j in xrange(i):
            if arr[i][0] < arr[j][1]:
                occupiedRooms = occupiedRooms + 1

        if occupiedRooms >= minRooms:
            minRooms = minRooms + 1

    return minRooms

def sorting(arr):
    time = []
    for x in arr:
        time.append((x[0], 0))
        time.append((x[1], 1))

    return sorted(time)

def findMinimumRoomsFast(arr):
    sortedArr = sorting(arr)
    minRooms = 0
    counter = 0

    for x in sortedArr:
        counter = counter + 1 if x[1] == 0 else counter - 1
        if minRooms < counter:
            minRooms = counter
    return minRooms

inputArr = [(30, 75), (0, 50), (60, 150), (60, 70)]
#inputArr = [(1, 4), (5, 6), (8, 9), (2, 6)]
print findMinimumRoomsFast(inputArr)
