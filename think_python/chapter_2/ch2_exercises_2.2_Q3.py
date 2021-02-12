#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

start_time = 06.5200
print(f"Start time: {start_time}am")


easy_pace = .0815
print(f"Easy pace: {easy_pace} per mile")


easy_pace_distance = 2
print(f"Total miles done on easy pace: {easy_pace_distance} miles")


easy_pace_elapsed = easy_pace * easy_pace_distance
print(f"Elapsed time on easy pace: {easy_pace_elapsed}")

fast_pace = .0725
print(f"Up tempo pace: {fast_pace} per mile")


fast_pace_distance = 3
print(f"Total miles done on up tempo pace: {fast_pace_distance} miles")


fast_pace_elapsed = fast_pace * fast_pace_distance
print(f"Elapsed time on fast pace: {fast_pace_elapsed}")


time_elapsed =
#= easy_pace_elapsed + fast_pace_elapsed
print(f"Time elapsed: {time_elapsed}")

# end_time = start_time - time_elapsed
# print(f"End time:{end_time}")



hours = int(time_elapsed)
minutes = (time_elapsed*60) % 60
seconds = (time_elapsed*3600) % 60
print(hours)
print(minutes)
print(seconds)

print("Time elapsed:%02d:%02d.%02d" % (hours,minutes, seconds))