import sc2reader
import os
import datetime
import glob

total_time_seconds = 0
total_time = 0
replays = [f for f in glob.glob("*.SC2Replay")]

for each in replays:
    replay = sc2reader.load_replay(each, load_level=0)
    total_time_seconds += replay.length.seconds
    # print(replay.filename)
    # print(replay.length.seconds)

total_time = str(datetime.timedelta(seconds=total_time_seconds))
print(total_time)
print(total_time_seconds/3600, " hours")
