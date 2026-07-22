def discover_files(repo_path):
    files = []

    for path in repo_path.rglob("*"):
        if path.is_file():
            files.append(path)

    return files
