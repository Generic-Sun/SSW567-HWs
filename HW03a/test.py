import unittest
from GitHubApi import get_repos, get_commits

class TestGitHubAPI(unittest.TestCase):

    def test_get_repos_valid_user(self):
        """Test that a valid user returns a list of repositories containing expected repos."""
        repos = get_repos("Generic-Sun")
        self.assertIn("helloworld", repos, "Expected 'helloword' in user's repositories.")

    def test_get_repos_invalid_user(self):
        """Test that an invalid user gracefully returns an empty list."""
        repos = get_repos("this_user_definitely_does_not_exist_123456789")
        self.assertEqual(repos, [])

    def test_get_commits_valid_repo(self):
        """Test that a valid repo returns a commit count greater than 0."""
        commits = get_commits("Generic-Sun", "helloworld")
        self.assertGreaterEqual(commits, 1, "Expected at least 1 commit in 'helloworld'.")

    def test_get_commits_invalid_repo(self):
        """Test that querying an invalid repo gracefully returns 0 commits."""
        commits = get_commits("Generic-Sun", "fake_repo_that_does_not_exist")
        self.assertEqual(commits, 0)

if __name__ == "__main__":
    unittest.main()