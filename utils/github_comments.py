import os

from github import Github


def post_comment(
    token,
    repo_name,
    issue,
    body
):

    try:

        g = Github(
            token
        )

        repo = (
            g.get_repo(
                repo_name
            )
        )

        pr = (
            repo.get_pull(
                issue
            )
        )

        pr.create_issue_comment(
            body
        )

        return True

    except Exception as e:

        return str(
            e
        )