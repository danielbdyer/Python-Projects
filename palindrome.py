class Palindrome(object):
    def __init__(self):
        pass

    def isPalindrome(self,palindrome_testword):
        if palindrome_testword == palindrome_testword[::-1]:
            print(palindrome_testword + " is the exact same back to front!")
            return palindrome_testword[::-1]
        else:
            print(palindrome_testword + " is not a palindrome, as when it is reversed it reads: " + palindrome_testword[::-1])
            return palindrome_testword[::-1]
