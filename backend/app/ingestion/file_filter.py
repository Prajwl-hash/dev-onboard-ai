ALLOWED_EXTENSIONS = {
    # Python
    ".py",

    # JavaScript / TypeScript
    ".js",
    ".jsx",
    ".ts",
    ".tsx",

    # Java / JVM
    ".java",
    ".kt",

    # C / C++
    ".c",
    ".h",
    ".cpp",
    ".hpp",

    # Other backend languages
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".cs",

    # Web
    ".html",
    ".css",

    # Database
    ".sql",

    # Data / configuration
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".xml",

    # Documentation / text
    ".md",
    ".txt"
}

IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "dist",
    "build"
}


def filter_files(files):
    filtered_files = []

    for file in files:
        if (
            file.suffix.lower() in ALLOWED_EXTENSIONS
            and not any(
                part in IGNORED_DIRECTORIES
                for part in file.parts
            )
        ):
            filtered_files.append(file)

    return filtered_files
