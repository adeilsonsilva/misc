import sys
import os

# Frames per second
FPS = 25

# Output folder
PATH = sys.argv[2]

# Output video number
N = sys.argv[3]

# Replace extension and fix file path
#vid = sys.argv[1].replace(".face", ".mov")
#vid = vid.replace("face-locations/", "")
vid = sys.argv[1]
face_locations_file = sys.argv[1].replace(".mov", ".face")
face_locations_file = "face-locations/" + face_locations_file

# Read from input file
with open(face_locations_file) as iFile:
    for line in iFile:
        frame_number, X, Y, W, H = line.rstrip().split(" ");
        frame_ss = (int(frame_number)+1) / FPS
        output = "{}_{}".format(N, frame_number)
        command = "ffmpeg -i {} -ss 0{:.2f} -vf crop={}:{}:{}:{} -frames:v 1 {}{}.jpeg -hide_banner".format(vid, frame_ss, W, H, X, Y, PATH, output)
        #print(command)
        os.system(command)
iFile.close();

