time_now = int(input("Please input the current hour in military time.\n"))                      #getting the current time from the user
alarm_hours = int(input("How many hours from now would you like your alarm to go off?\n"))      #getting the alarm duration from the user

output = (alarm_hours + time_now) % 24                                                          #calculates what the resulting time will be when the alarm goes off

if output == 12:                                                                                #checks to see if the time is noon
    print("When your alarm goes off it will be:", output, "pm")
elif output == 0:                                                                               #checks to see if the time is midnight
    output += 12
    print("When your alarm goes off it will be:", output, "am")
elif output >= 13:                                                                              #checks to see if the output is greater than 12 and thus pm
    output -= 12
    print("When your alarm goes off it will be:", output, "pm")
else:                                                                                           #deals with all other times that are not midnight, noon, or pm
    print("When your alarm goes off it will be:", output, "am")
