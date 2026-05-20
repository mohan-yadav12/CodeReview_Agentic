import streamlit as st

from core.repo_cloner import (
    clone_repository
)

from core.file_scanner import (
    get_python_files
)

from parser.ast_parser import (
    parse_file
)


st.title(
    "AI Code Review Agent"
)


repo = st.text_input(
    "GitHub Repository URL"
)


if st.button(
    "Analyze"
):

    with st.spinner(
        "Cloning..."
    ):

        result = clone_repository(
            repo
        )

    if not result[
        "success"
    ]:

        st.error(
            result[
                "error"
            ]
        )

    else:

        files = get_python_files(
            result[
                "path"
            ]
        )

        rows = []

        for f in files:

            rows.append(
                parse_file(f)
            )

        st.json(rows)