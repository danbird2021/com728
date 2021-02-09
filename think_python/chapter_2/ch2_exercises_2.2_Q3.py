#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

start_time = 6.52
print(f"Start time: {start_time}am")

easy_pace = 08.15
print(f"Easy pace: {easy_pace} per mile")

easy_pace_distance = 2
print(f"Total miles done on easy pace: {easy_pace_distance} miles")

easy_pace_elapsed_decimal = easy_pace * easy_pace_distance
print(f"Elapsed time on easy pace (decimal): {easy_pace_elapsed_decimal}")

easy_pace_elapsed_mins = easy_pace_elapsed_decimal


print(f"Elapsed time on easy pace (minutes): {easy_pace_elapsed_mins}")

fast_pace = 07.12
print(f"Up tempo pace: {fast_pace} per mile")

fast_pace_distance = 3
print(f"Total miles done on up tempo pace: {fast_pace_distance} miles")

fast_pace_elapsed_decimal = fast_pace * fast_pace_distance
print(f"Elapsed time on fast pace: {fast_pace_elapsed_decimal}")


fast_pace_elapsed_mins = fast_pace_elapsed_decimal

print(f"Elapsed time on fast pace (minutes): {fast_pace_elapsed_mins}")

time_elapsed = easy_pace_elapsed_mins + fast_pace_elapsed_mins

print(f"Time elapsed (decimal): {time_elapsed}")

#hours = int(time_elapsed)
minutes = (time_elapsed*60) % 60
seconds = (time_elapsed*3600) % 60

print("Time elapsed (minutes):%02d.%02d" % (minutes, seconds))