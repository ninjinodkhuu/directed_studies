#Extract the frames from videos

import cv2
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_frames(video_path, output_folder, video_filename):
    # open the video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()  # read each frame
        if not ret:
            break 

        # save frame as image with name
        frame_filename = os.path.join(output_folder, f'{video_filename}_frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()


video_files = ['1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4']
output_dir = 'extracted_frames'

create_directory(output_dir)


for video in video_files:
    video_path = os.path.join('vids', video) 
    extract_frames(video_path, output_dir, video)


