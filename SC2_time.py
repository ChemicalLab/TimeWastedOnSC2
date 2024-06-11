import sc2reader
import os
import datetime
import glob
import argparse
from multiprocessing import Pool
from tqdm import tqdm

def process_replay(replay_file):
    replay = sc2reader.load_replay(replay_file, load_level=0)
    return replay.length.seconds

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the total time of the replays in the specified folder.')
    parser.add_argument('folder_path', type=str, help='The path to the folder containing the replay files')

    args = parser.parse_args()

    replays = [f for f in glob.glob(os.path.join(args.folder_path, "*.SC2Replay"))]

    with Pool() as p:
        results = list(tqdm(p.imap(process_replay, replays), total=len(replays)))

    total_time_seconds = sum(results)
    total_time = str(datetime.timedelta(seconds=total_time_seconds))

    print(total_time)
    print(total_time_seconds/3600, " hours")