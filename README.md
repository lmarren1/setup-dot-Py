# Firm Finder

## Basic Idea

### Problem 

I am having trouble consolidating a list of technical recruiters at firms in downtown Chicago. I want something that will give me the professional contact information of technical recruiters at companies in the downtown area of Chicago. These firms must offer software development positions.

### Solution

I want to build an app that...
- Lists the (1) company email, (2) LinkedIn profile, (3) firm, and (4) firm location of technical recruiters at firms in Chicago hiring for software developers. (feature)
- To solve the above problem (problem)
- For myself and potentially other job seekers

## Implementation

I need to find the following for this application to work:
- Firm names and locations in a specifc geographic location
    - Google Maps API
- Sentiment analysis of the firms
    - What roles might they be hiring for?
    - ChatGPT
- Technical Recruiter contact information at each of these firms
    - Apollo API

## Timeline

I want to have a **minimum viable product** (CLI tool) of this app **within a week**

- [ ] Day One: Set up python project
    - venv/
        - Create
    - update_py_dependencies.py
        - Create based on system
    - requirements.txt
        - Create
    - config.json (private data)
        - Create
    - .gitignore
        - Create, add private info
    - .pre-commit-config.yaml
        - black formatter
            - run_black.py
        - isort import orderer
            - run_isort.py
        - flake8 linter
            - run_flake8.py
        - pytest
            - run_pytest.py
        - pytest-cov
            - run_pytest-cov.py
        - trailing whitespace
            - fix_trailing_whitespace.py
        - end of file fixer (file ends with one newline)
            - fix_file_end.py
        - check merge conflict

        - setup.py - handles all of this

- [ ] Day Two: Find firm names and locations in Downtown Chicago using a Google Maps API
- [ ] Day Three: Figure out sentiment analysis of firms
- [ ] Day Four: Figure out how to get recruiter contact info
