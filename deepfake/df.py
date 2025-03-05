#use deepface to find the dominant emotion in each frame and create a file stating the percentage of each emotion

import os
from deepface import DeepFace
import pandas as pd

# directory containing the frames
frames_dir = "/Users/ninjinodkhuu/School/Spring 2025/Directed Studies/senti/data/extracted_frames"

# list for results
emotions_data = []

# loop through the images
for filename in os.listdir(frames_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # get the video number 
        video_number = filename.split('_')[0]  # Splits on '_' and takes the first part as video number
        image_path = os.path.join(frames_dir, filename)

        try:
            # get emotion
            result = DeepFace.analyze(image_path, actions=['emotion'], enforce_detection=False)

            if len(result) > 0:
                # get dominant emotion and percentage
                dominant_emotion = result[0]['dominant_emotion']
                dominant_emotion_percentage = result[0]['emotion'][dominant_emotion]

                # get other emotions and percentages
                emotions = result[0]['emotion']

                # store frame name, video number, dominant emotion, emotion percentages
                emotions_data.append({
                    'Video': video_number,  
                    'Frame': filename,
                    'Dominant Emotion': dominant_emotion,
                    'Dominant Emotion Percentage': dominant_emotion_percentage,
                    **emotions  # add the other emotions and their percentages
                })
            else:
                print(f"Warning: No face detected in {filename}, skipping...")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

# store the results in tab form
df = pd.DataFrame(emotions_data)

# output file path
output_file = "/Users/ninjinodkhuu/School/Spring 2025/Directed Studies/senti/data/emotions_results.csv"

# save file
df.to_csv(output_file, index=False)

#print confirmation
print(f"data saved to {output_file}")
