#create a file to see if the emotion calculated by the model matches the annotated emotion

import pandas as pd

# load the pre-nnotated emotions
labels_df = pd.read_csv("emotion_labels.csv")

# load the 
overall_df = pd.read_csv("video_emotion.csv")

# Initialize the updated DataFrame
updated_results = []

# Loop through the videos in the overall emotions DataFrame
for idx, row in overall_df.iterrows():
    video = row['Video']
    dominant_emotion = row['Dominant Emotion']
    
    # Check if the video exists in the labels DataFrame
    matching_row = labels_df[labels_df['Video Filename'] == video]
    
    if not matching_row.empty:
        # Facial Emotion from labels CSV
        facial_emotion = matching_row.iloc[0]['Facial Emotion']
    else:
        # If no match, mark it as 'Unknown'
        facial_emotion = "Unknown"
    
    # Convert both emotions to lowercase for case-insensitive comparison
    is_match = facial_emotion.lower() == dominant_emotion.lower() if isinstance(facial_emotion, str) else False
    match_result = "Match" if is_match else "No Match"
    
    # Prepare the row to append with the Dominant Emotion, Facial Emotion, and emotion percentages
    updated_results.append({
        'Video': video,
        'Match': match_result,
        'Dominant Emotion': dominant_emotion,
        'Facial Emotion': facial_emotion.lower() if isinstance(facial_emotion, str) else facial_emotion,
        'angry': round(row['angry'], 2),
        'disgust': round(row['disgust'], 2),
        'fear': round(row['fear'], 2),
        'happy': round(row['happy'], 2),
        'sad': round(row['sad'], 2),
        'surprise': round(row['surprise'], 2),
        'neutral': round(row['neutral'], 2)
    })

# Create the updated DataFrame
updated_df = pd.DataFrame(updated_results)

# Save the updated DataFrame to a new CSV file
updated_df.to_csv("comparison_results.csv", index=False)

# Print a confirmation message
print("data saved to 'comparison_results.csv'")
