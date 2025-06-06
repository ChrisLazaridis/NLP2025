import os
import shutil
from pathlib import Path
from huggingface_hub import Repository

# 1. Define paths relative to project root
project_root = Path(__file__).parent
tmp_repo    = project_root / "tmp_hf_repo"

# 2. Clone the Hugging Face repo into a temporary folder
if tmp_repo.exists():
    shutil.rmtree(tmp_repo)
repo = Repository(
    local_dir=str(tmp_repo),
    clone_from="https://huggingface.co/RagerGr/NLP2025-Ambiguity",
    use_auth_token=True
)
# At this point, tmp_repo contains the full clone.

# 3. Corrected mapping of remote sub-folders → list of (local_base, subdir_name)
tasks = {
    "data_vocab": [
        (project_root/"Evaluation"/"try1", "data"),
        (project_root/"ML"/"try1",         "data")
    ],
    "models_vocab": [
        (project_root/"Evaluation"/"try1", "models"),
        (project_root/"ML"/"try1",         "models")
    ],
    "data _enronsent": [
        (project_root/"ML"/"try2",         "data"),    # ML/try2/data
        (project_root/"Evaluation"/"try2", "data")     # Evaluation/try2/data
    ],
    "models_enronsent": [
        (project_root/"ML"/"try2",         "models"),  # ML/try2/models
        (project_root/"Evaluation"/"try2", "models")   # Evaluation/try2/models
    ]
}

# 4. Copy each folder’s contents to its destinations
for remote_folder, destinations in tasks.items():
    src = tmp_repo / remote_folder
    if not src.is_dir():
        raise FileNotFoundError(f"Remote folder missing: {src}")
    for base_dir, sub in destinations:
        dest = base_dir / sub
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dest, dirs_exist_ok=True)
