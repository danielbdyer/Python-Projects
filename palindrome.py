#import math
potential_pal = raw_input("What word would you like to check for palindromic nature? ").lower()

def isPalindrome(potential_pal):
    if potential_pal == potential_pal[::-1]: print "Palindrome!"; return True
    else: print "Not a palindrome."; return False

isPalindrome(potential_pal)


#halfway_mark = int(math.floor(len(potential_pal))/2)+1

#def palindrome(potential_pal):
#    palindromic_flag = True
#    for index in range(0,halfway_mark):
#        if potential_pal[index] != reversed_pal[index]:
#            palindromic_flag = False
#        else:
#            palindromic_flag = True
#    if palindromic_flag == False:
#        print "This word is not a palindrome!"
#    else: print "This word is a palindrome."

#palindrome(potential_pal)
