# start of loop

# initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("There are {} seats"
          "left".format(MAX_TICKETS - count))

    # Get details . . .
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("All available tickets have been sold")
else:
    print ("There are {} tickets. \n"
           "There are {} tickets seats still available"
           .format(count, MAX_TICKETS - count)
