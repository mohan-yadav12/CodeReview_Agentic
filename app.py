import streamlit as st
import pandas as pd
import os

from core.repo_cloner import clone_repository
from core.file_scanner import get_python_files
from reviewer.orchestrator import run_review
from utils.report_generator import markdown_report


st.title(
    "AI Code Review Agent"
)


repo = st.text_input(
    "Repository URL"
)


if st.button(
    "Analyze"
):

    result = (
        clone_repository(
            repo
        )
    )

    if result[
        "success"
    ]:

        files = (
            get_python_files(
                result[
                    "path"
                ]
            )
        )

        with st.spinner(
            "Reviewing..."
        ):

            reviews = (
                run_review(
                    files
                )
            )

        df = (
            pd.DataFrame(
                reviews
            )
        )

        st.session_state[
            "df"
        ] = df


if "df" in st.session_state:

    df = (
        st.session_state[
            "df"
        ]
    )

    severity = (
        st.selectbox(

            "Severity",

            [
                "All",
                "Critical",
                "Major",
                "Minor",
                "High",
                "Medium",
                "Low"
            ]
        )
    )

    if severity != "All":

        df = (
            df[
                df[
                    "severity"
                ]
                ==
                severity
            ]
        )

    st.dataframe(
        df
    )

    markdown = (
        markdown_report(
            df
        )
    )

    st.download_button(

        "Download Markdown",

        markdown,

        "review.md"
    )

    st.download_button(

        "Download JSON",

        df.to_json(),

        "review.json"
    )

    st.download_button(

        "Download CSV",

        df.to_csv(),

        "review.csv"
    )