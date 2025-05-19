import os
from huggingface_hub import login, snapshot_download, upload_file
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = input("Enter your Hugging Face token: ")

# Log in to Hugging Face
login(token=HF_TOKEN)

# Define the models directory and repo ID
models_dir = "models"
repo_id = "RagerGr/Seq2Seq-Ambiguity-LSTM/tree/main/models"

# Create the models directory if it doesn't exist
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
# Download the models from Hugging Face
snapshot_download(repo_id=repo_id, local_dir=models_dir)


