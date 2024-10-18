from github import Github
import os

def main():
    # Initialize GitHub API with token
    g = Github(os.getenv("GITHUB_API_TOKEN"))

    # Specify the organization or user
    org_name = "khulnasoft"
    org = g.get_organization(org_name)

    # Fetch all repositories in the organization
    for repo in org.get_repos():
        print(f"Processing repository: {repo.full_name}")

        # Run your logic for snapshot, forks, stargazers, etc.
        snapshot_dir = "newsnapshots"
        forks_out = "forks-raw.csv"
        stars_out = "stars-raw.csv"

        # Example: Fetch and process forks and stargazers
        forks = repo.get_forks()
        stars = repo.get_stargazers()

        # Save or process forks and stars as needed
        # This is a placeholder for your actual logic to save to CSV, etc.

if __name__ == "__main__":
    main()
