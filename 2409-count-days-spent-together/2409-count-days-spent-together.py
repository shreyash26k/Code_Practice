class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            total_days = day
            for m in range(month - 1):
                total_days += days_in_months[m]
            return total_days
        a1 = date_to_day(arriveAlice)
        l1 = date_to_day(leaveAlice)
        a2 = date_to_day(arriveBob)
        l2 = date_to_day(leaveBob)
        
        start = max(a1, a2)
        end = min(l1, l2)
        
        return max(0, end - start + 1)