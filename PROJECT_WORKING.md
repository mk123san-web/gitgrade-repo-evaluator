# How GitGrade Works

## Step 1: Input
The user provides a public GitHub repository URL.

Example:
https://github.com/sample-user/todo-app

## Step 2: Analysis (Conceptual)
The system checks:
- Whether README file exists
- Project folder structure
- Code readability (file naming, comments)
- Commit history consistency

These checks simulate how an AI mentor reviews a repository.

## Step 3: Scoring
Each parameter is assigned marks based on predefined rules.

Example:
- Structure: 25 marks
- Documentation: 20 marks
- Readability: 20 marks
- Commits: 20 marks
- Best practices: 15 marks

Total score = 100

## Step 4: Output
The system generates:
1. Repository score
2. Short quality summary
3. Personalized improvement roadmap

This helps students understand strengths and weaknesses
of their GitHub projects.
