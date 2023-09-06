from django.shortcuts import render
import datetime
import time

def screen_time(request):
    # set the path and name of the log file
    log_file = "screen_time_log.txt"

    # set the frequency of logging in seconds
    log_frequency = 60

    # get the current time
    start_time = datetime.datetime.now()

    # initialize the screen time to 0 seconds
    screen_time = datetime.timedelta(seconds=0)

    # wait for the specified time before logging again
    time.sleep(log_frequency)
    
    # get the current time
    current_time = datetime.datetime.now()

    # calculate the time difference between the current time and the start time
    time_diff = current_time - start_time

    # update the screen time
    screen_time += time_diff

    # write the screen time to the log file
    with open(log_file, "a") as file:
        file.write(f"{current_time}: Screen time - {screen_time}\n")

    # format the screen time in HH:MM:SS format
    screen_time_str = str(screen_time).split('.')[0]

    # render the template with the screen time
    return render(request, 'screen_time.html', {'screen_time': screen_time_str})
