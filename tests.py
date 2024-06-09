import unittest
def reverseList(lst):
    left=0
    right=len(lst) - 1
    while left < right :
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
        return lst
class TestReverseList(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reverseList([1,3,5]),[5,3,1])
    
    def test_empty_list(self):
        self.assertEqual(reverseList([]),[])

    def test_single_element_list(self):
        self.assertEqual(reverseList([7]),[7])

    def test_even_length_list(self):
        self.assertEqual(reverseList([2, 4, 6, 8]), [8, 6, 4, 2])

    def test_odd_length_list(self):
        self.assertEqual(reverseList([11,13,17,19,23]),[23,19,17,13,11])

if  __name__ == "__main__":
    unittest.main()

import unittest

def isPalindrome(word):
    return word == word[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_example(self):
        self.assertTrue(isPalindrome("racecar"))

    def test_single_character(self):
        self.assertTrue(isPalindrome("a"))

    def test_non_palindrome(self):
        self.assertFalse(isPalindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))

    def test_case_insensitive(self):
        self.assertTrue(isPalindrome("Radar"))

    def test_whitespace(self):
        self.assertTrue(isPalindrome("A man a plan a canal Panama"))

if __name__ == "__main__":
    unittest.main()

import unittest

def coins(amount):
    quarters = amount // 25
    amount %= 25
    dimes = amount // 10
    amount %= 10
    nickels = amount // 5
    amount %= 5
    pennies = amount
    return [quarters, dimes, nickels, pennies]

class TestCoins(unittest.TestCase):
    def test_example(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test_no_change(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_large_amount(self):
        self.assertEqual(coins(999), [39, 2, 0, 4])

    def test_only_pennies(self):
        self.assertEqual(coins(3), [0, 0, 0, 3])

    def test_only_quarters(self):
        self.assertEqual(coins(100), [4, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()


