import os

IGNORE = ["venv",".git","__pycache__","tests","build"]
def get_python_files(root):
    files = []
    for path, dirs, filenames in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(path, f))
    return files