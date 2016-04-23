# harshil912@gmail.com
# python3
# Script to check time spent
# Run the script when starting to work and occasionally press 1 to check how long have you been working

import time
from datetime import datetime
start = time.time()
print("Script started at: " + str(datetime.now().time()))
print("Enter: \n1 - Time spend until now. \n2 - Time now. \n100 - Quit:\t")
while(True):
    try:
        input_string = int(input())
    except:
        continue
    if input_string == 100:
        print("Exiting App at: " + str(int(time.time() - start)) + " seconds")
        break
    end = time.time()
    if input_string == 1:
        difference = int(end-start)
        calculation = ""
        if difference > 60:
            if difference > 3600:
                calculation += str(difference/3600) + " Hours,  "
                difference = difference%3600
                calculation += str(int(difference/60)) + " minutes."
            else:
                calculation += str(int(difference/60)) + "  minutes."
            print("Been up for: " + calculation)
        else:
            print("Been up for: " + str(int(difference))+" seconds.")
    if input_string == 2:
        print(str(datetime.now().time()))
