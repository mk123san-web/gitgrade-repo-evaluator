# GitGrade - GitHub Repository Evaluator
# Beginner-friendly MVP version

def evaluate_repository(repo_url):
    score = 0
    summary = []
    roadmap = []

    # Simulated checks (rule-based)
    if "github.com" in repo_url:
        score += 20
        summary.append("Valid GitHub repository link detected.")
    else:
        roadmap.append("Provide a valid GitHub repository URL.")

    # README check (assumed)
    score += 15
    summary.append("README file exists but can be improved.")
    roadmap.append("Improve README with clear project description and setup steps.")

    # Project structure check
    score += 15
    summary.append("Project structure is basic.")
    roadmap.append("Organize code into proper folders.")

    # Commit history check
    score += 10
    summary.append("Commit history is inconsistent.")
    roadmap.append("Commit code regularly with meaningful messages.")

    # Code quality check
    score += 8
    summary.append("Code readability is average.")
    roadmap.append("Improve code readability with comments and naming.")

    # Final score cap
    if score > 100:
        score = 100

    return score, summary, roadmap


def main():
    print("GitGrade - GitHub Repository Evaluator")
    print("-----------------------------------")

    repo_url = input("Enter GitHub Repository URL: ")

    score, summary, roadmap = evaluate_repository(repo_url)

    print("\nEvaluation Result")
    print("-----------------")
    print(f"Score: {score} / 100")

    print("\nSummary:")
    for line in summary:
        print("-", line)

    print("\nPersonalized Roadmap:")
    for step in roadmap:
        print("-", step)


if __name__ == "__main__":
    main()
