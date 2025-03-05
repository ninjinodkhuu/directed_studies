
import pandas as pd

# file containing frame analysis results
input_file = "/Users/ninjinodkhuu/School/Spring 2025/Directed Studies/senti/data/emotions_results.csv"
df = pd.read_csv(input_file)

# list of emotions
emotion_columns = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# create function to process frames by nth frame

# group by video and sum up percentages
video_emotions = df.groupby('Video')[emotion_columns].sum()

# find the emotion with the highest sum
video_emotions.insert(0, 'Dominant Emotion', video_emotions.idxmax(axis=1))

# calculate emotion percentage from the total summed probabilities for that video
video_emotions_percentage = video_emotions.copy()
video_emotions_percentage[emotion_columns] = (
    video_emotions_percentage[emotion_columns]
    .div(video_emotions_percentage[emotion_columns].sum(axis=1), axis=0) * 100  # Convert to percentage
).round(2)  # Round to two decimal places

# Define the output CSV file path
output_file = "/Users/ninjinodkhuu/School/Spring 2025/Directed Studies/senti/data/video_emotion.csv"

# Save the results as a CSV file
video_emotions_percentage.to_csv(output_file)

# Print a confirmation message
print(f"data saved to {output_file}")
