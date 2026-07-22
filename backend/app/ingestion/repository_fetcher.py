import subprocess
import tempfile
from pathlib import Path


def clone_repository(repo_url):
    temp_dir = tempfile.mkdtemp()
    repo_path = Path(temp_dir) / "repository"

    print(f"Temporary directory: {temp_dir}")
    print("Cloning repository...")

    subprocess.run(
        ["git", "clone", "--depth", "1", repo_url, str(repo_path)],
        check=True
    )

    print("Repository cloned successfully!")

    return repo_path
