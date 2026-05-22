# AI Code Review Agent 🤖🔍

A powerful, Streamlit-based web dashboard that clones a git repository, performs Abstract Syntax Tree (AST) analysis on Python code blocks, and leverages the Google Gemini LLM API to automatically perform comprehensive code reviews.

---

## 🌟 Key Features

- **Automatic Repository Cloning**: Seamlessly clones any public git repository via its URL. To keep disk space clean, the agent maintains a cache limit of the most recent 3 repositories and automatically purges older ones.
- **AST-Based Parsing**: Instead of analyzing raw file strings, the agent uses Python's Abstract Syntax Tree (`ast` module) to extract precise class and function definitions, reviewing code block-by-block.
- **LLM Review Engine**: Analyzes extracted code blocks for:
  - 🐛 Bugs & Logical Errors
  - 🔒 Security Vulnerabilities
  - ⚡ Performance Bottlenecks
  - 🛠️ Maintainability & Style Improvements
- **Interactive Review Dashboard**: An intuitive UI built with Streamlit that presents findings in a tabular dataframe, complete with severity filtering (e.g., Critical, Major, Minor, Low, etc.).
- **Multiple Export Formats**: Instantly download reports as formatted **Markdown**, **JSON**, or **CSV**.
- **Ready-To-Wire Utility Modules**: Contains helper utilities for caching LLM responses (`utils/cache.py`), logging repository scan history (`utils/history.py`), and automatically posting findings as GitHub PR comments (`utils/github_comments.py`).

---

## 📂 Project Structure

```text
├── core/
│   ├── file_scanner.py     # Filters and retrieves python files, skipping venv/git/tests
│   └── repo_cloner.py      # Clones repositories and manages directory cleanups
├── parser/
│   └── ast_parser.py       # Parses files into syntax trees to extract functions & classes
├── reviewer/
│   ├── confidence.py       # Normalizes LLM confidence scores & categorizes them
│   ├── llm_reviewer.py     # Communicates with Google Gemini API
│   ├── orchestrator.py     # Coordinates scanning, parsing, and reviewing flow
│   └── prompt_builder.py   # Formulates structured prompts with JSON schemas
├── utils/
│   ├── cache.py            # MD5-based caching for LLM responses
│   ├── github_comments.py  # Github PR commenting API helper
│   ├── history.py          # Log generator to record repo scan history
│   └── report_generator.py # Formats DataFrame outputs to Markdown reports
├── output/
│   └── history.json        # Saved local history log of analyzed repositories
├── .env.example            # Environment variables configuration template
├── app.py                  # Main Streamlit web application
└── requirements.txt        # Python dependency specifications
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.9+ and `git` installed on your machine.

### 2. Installation
Clone the repository (or copy the files) and install the necessary dependencies:

```bash
# Clone the repository
git clone <repository-url>
cd CodeReview_Agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 3. API Key Configuration
Create a `.env` file in the root directory and add your Google Gemini API Key:

```env
API_KEY=your_gemini_api_key_here
```

### 4. Running the Dashboard
Start the Streamlit application using the command below:

```bash
streamlit run app.py
```
This will start a local server and open the web dashboard in your browser (typically at `http://localhost:8501`).

---

## 🛠️ How It Works Under the Hood

1. **Cloning & Cleaning**: The app takes a public repository URL, clones it to a temporary directory in `repos/`, and performs a FIFO cleanup keeping only the 3 most recently accessed repos.
2. **Code Scan & AST Extraction**: Python files are scanned (ignoring test, build, and virtual environments). `ast_parser.py` parses each file, retrieving the source code segment for functions and classes.
3. **Structured AI Feedback**: The agent feeds each code segment to the `gemini-2.5-flash` model with a strict JSON format prompt. The response includes `issue_type`, `severity`, `review_comment`, `suggested_fix`, and `confidence_score`.
4. **Data Normalization**: Confidence scores are normalized (scaled up from decimal format if needed) and categorized as `High`, `Medium`, or `Verify This`.
5. **Interactive Filtering**: The results are parsed into a Pandas DataFrame and loaded onto the dashboard, where you can filter issues by severity and download reports.

---

## ⚡ Extension Capabilities (Included Utilities)

The project is built with extensibility in mind and includes ready-made modules under `utils/` to expand functionality:
* **Caching (`utils/cache.py`)**: Can be integrated into `llm_reviewer.py` to cache code block reviews based on MD5 hashes of code strings, avoiding repeated API costs.
* **GitHub Actions Integration (`utils/github_comments.py`)**: Can be wired to automatically comment on pull requests when integrated into a CI/CD pipeline.
* **Scan Logging (`utils/history.py`)**: Saves analysis logs under `output/history.json` to keep track of total rows and repos scanned over time.
