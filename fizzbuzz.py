from checkint import numbercheck

fizz_or_buzz = int(numbercheck("What's your number? "))

if fizz_or_buzz % 3 == 0 and fizz_or_buzz % 5 == 0:
    print("Fizz Buzz!")
elif fizz_or_buzz % 3 == 0:
    print("Fizz!")
elif fizz_or_buzz % 5 == 0:
    print("Buzz!")

else: print("Neither fizz nor buzz! Try again.")
