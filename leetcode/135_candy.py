class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        
        # Left-to-right: handle ascending runs from the left
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right-to-left: handle ascending runs from the right
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
  
if __name__ == "__main__":
    sol = Solution()
    print(sol.candy([1, 0, 2]))      # expected: 5
    print(sol.candy([1, 2, 2]))      # expected: 4
    print(sol.candy([1, 3, 2, 2, 1])) # tricky case