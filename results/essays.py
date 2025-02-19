import os

dataset_path = "/Users/ninjinodkhuu/.cache/kagglehub/datasets/sunilthite/llm-detect-ai-generated-text-dataset/versions/1"

# List all files in the dataset directory
files = os.listdir(dataset_path)
print("Files in dataset:", files)
