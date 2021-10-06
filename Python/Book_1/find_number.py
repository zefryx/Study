print ("""Hi! Enter a number that is
not less than 80 and not more than 150 and
not less than 90 or equal to 150.

There can be many such nubbers.
Find at least one of them.""")

x = int(input("Enter a number: "))

res = (not(x<80) and not(x>150)\
       and not(x<90) or (x==150))

if (res):
    print("Congratulation! You find the number!")
else:
    print("Unfortunately not that.")

input("Press Enter to EXIT ")
quit()
