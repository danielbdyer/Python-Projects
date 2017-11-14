from checkint import numbercheck

total_bill = numbercheck("What's your total amount, pre-tip? ")
tip_percentage = numbercheck("And what percentage would you like to tip? ")

post_tip = round(total_bill + ((tip_percentage/100)*total_bill), 2)

if tip_percentage < 20:
    print("That's a little stingy of you. Did they do a bad job?")
else:
    print("How generous. I'm sure they appreciate it!")

print("Your total bill amount comes to: {0}".format(post_tip))
