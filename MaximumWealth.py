import unittest

class Solution():
    def maximumWealth_basic(self, accounts):
        maxWealth = 0
        for customer in accounts:
            wealth = sum(customer) # sum wealth for each customer
            if maxWealth < wealth: # check if maxWealth less than wealth --> wealth is new maxWealth
                maxWealth = wealth
        return maxWealth
    
    # or one line code 
    def maximumWealth_oneLine(self, accounts):
        return max([sum(i) for i in accounts]) # use max function to find max wealth from each customer


class MyTest(unittest.TestCase):
    def test_basic(self):
        myCal = Solution()
        self.assertEqual(myCal.maximumWealth_basic([[1,2,3],[3,2,1]]), 6)
        self.assertEqual(myCal.maximumWealth_basic([[2,4],[5,9],[1,5,1]]), 14)
        self.assertEqual(myCal.maximumWealth_basic([[1,5],[7,4],[3,5]]), 11)
        self.assertEqual(myCal.maximumWealth_basic([[2,1,5],[5,1,3],[1,9,5]]), 15)
        self.assertEqual(myCal.maximumWealth_basic([[4,6],[7,2]]), 10)
    def test_oneLine(self):
        myCal = Solution()
        self.assertEqual(myCal.maximumWealth_oneLine([[1,2,3],[3,2,1]]), 6)
        self.assertEqual(myCal.maximumWealth_oneLine([[2,4],[5,9],[1,5,1]]), 14)
        self.assertEqual(myCal.maximumWealth_oneLine([[1,5],[7,4],[3,5]]), 11)
        self.assertEqual(myCal.maximumWealth_oneLine([[2,1,5],[5,1,3],[1,9,5]]), 15)
        self.assertEqual(myCal.maximumWealth_oneLine([[4,6],[7,2]]), 10)

 
if __name__ == '__main__':
  unittest.main()