from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        hour, minute = -1, -1
        
        for h1, h2, m1, m2 in permutations(A):
            cur_hour, cur_min = 10*h1 + h2, 10*m1 + m2
            if cur_hour >= 24 or cur_min >= 60:
                continue
                
            if cur_hour * 60 + cur_min > hour*60 + minute:
                hour, minute = cur_hour, cur_min
                        
        if (hour, minute) == (-1, -1):
            return ""
        else:
            clock_string = [f'{hour:02}', f'{minute:02}']
            print(clock_string)
            return ':'.join( clock_string )
