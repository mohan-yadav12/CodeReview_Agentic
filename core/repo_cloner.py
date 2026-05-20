from git import Repo
import tempfile
import os
import shutil
import uuid


BASE_DIR = "repos"

os.makedirs(
    BASE_DIR,
    exist_ok=True
)


def cleanup_old_repos():

    if not os.path.exists(BASE_DIR):
        return

    folders = []

    for f in os.listdir(BASE_DIR):

        p = os.path.join(
            BASE_DIR,
            f
        )

        if os.path.isdir(p):

            folders.append(p)

    folders = sorted(
        folders,
        key=os.path.getmtime
    )

    while len(folders) > 3:

        old = folders.pop(0)

        try:
            shutil.rmtree(
                old,
                ignore_errors=True
            )

        except:
            pass


def clone_repository(repo_url):

    cleanup_old_repos()

    repo_name = (
        "repo_"
        +
        str(
            uuid.uuid4()
        )[:8]
    )

    repo_path = os.path.join(
        BASE_DIR,
        repo_name
    )

    try:

        Repo.clone_from(
            repo_url,
            repo_path
        )

        return {

            "success": True,

            "path": repo_path
        }

    except Exception as e:

        if os.path.exists(
            repo_path
        ):
            shutil.rmtree(
                repo_path,
                ignore_errors=True
            )

        return {

            "success": False,

            "error": str(e)
        }