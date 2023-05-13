import unittest        

class Convert():
    def romanToInt(self, roman):
            i = 0
            ans = 0
            dict = {'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000}
            
            while i < len(roman) - 1:
                if dict[roman[i]] >= dict[roman[i+1]]: # if roman[i] > roman[i+1] --> plus number to ans
                    ans += dict[roman[i]]
                    i+=1
                else:
                    ans += dict[roman[i+1]] - dict[roman[i]] # if roman[i] < roman[i+1] --> subtract from next number
                    i+=2
            if i < len(roman): # check if last digit left in roman --> plus number to ans
                ans += dict[roman[i]]
            return ans


class MyTest(unittest.TestCase):
    def test_evenRoman(self):
        myCal = Convert()
        self.assertEqual(myCal.romanToInt("LXXIII"), 73)
        self.assertEqual(myCal.romanToInt("CLXXVIII"), 178)
        self.assertEqual(myCal.romanToInt("XCVIII"), 98)
        self.assertEqual(myCal.romanToInt("CI"), 101)
        self.assertEqual(myCal.romanToInt("CXXX"), 130)
    def test_oddRoman(self):
        myCal = Convert()
        self.assertEqual(myCal.romanToInt("CXCVIII"), 198)
        self.assertEqual(myCal.romanToInt("CXX"), 120)
        self.assertEqual(myCal.romanToInt("C"), 100)
        self.assertEqual(myCal.romanToInt("LXXII"), 72)
        self.assertEqual(myCal.romanToInt("XXXVIII"), 38)

 
if __name__ == '__main__':
  unittest.main()