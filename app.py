import streamlit as st
import pandas as pd

from core.repo_cloner import (clone_repository)
from core.file_scanner import (get_python_files)
from reviewer.orchestrator import (run_review)

if "last_repo" not in st.session_state:
    st.session_state.last_repo = None


st.title("AI Code Review Agent")

repo = st.text_input("Repository URL")

if st.button("Review Repository"):

    st.cache_data.clear()

    result = clone_repository(repo)

    if not result["success"]:

        st.error(result["error"])

    else:
        st.session_state.last_repo = result["path"]

        files = get_python_files(result["path"])

        with st.spinner("Reviewing..."):

            reviews = run_review(
                files
            )

        df = pd.DataFrame(
            reviews
        )

        st.dataframe(
            df
        )

        severity = (
            st.selectbox(
                "Severity",
                [
                    "All",
                    "Low",
                    "Medium",
                    "High"
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

        st.download_button(

            "Download JSON",

            df.to_json(),

            "review.json"
        )