class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        moves=min(x,y//4)

        if(moves%2==1):
            return "Alice"
        else:
            return "Bob"

x = 4
y = 11

obj=Solution()
print(obj.winningPlayer(x,y))
