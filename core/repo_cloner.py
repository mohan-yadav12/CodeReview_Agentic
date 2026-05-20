from git import Repo
import shutil
import os


CLONE_DIR = "repos"


def clone_repository(repo_url):

    if os.path.exists(CLONE_DIR):
        shutil.rmtree(CLONE_DIR)

    os.makedirs(CLONE_DIR)

    try:
        Repo.clone_from(repo_url, CLONE_DIR)

        return {
            "success": True,
            "path": CLONE_DIR
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }