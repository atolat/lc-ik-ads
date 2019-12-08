# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Example 1:

# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: [[7,10],[2,4]]
# Output: true
from operator import itemgetter

def canAttendMeetings(self, intervals):
        intervals.sort(key=itemgetter(0))

        for i in range(len(intervals)-1):
            if intervals[i][0] == intervals[i+1][0]:
                return False
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True


print(canAttendMeetings([[7, 10], [2, 4]]))
