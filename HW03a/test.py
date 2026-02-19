import unittest
from unittest.mock import patch
from GitHubApi import get_repos, get_commits

class TestGitHubAPI(unittest.TestCase):
    @patch('GitHubApi.requests.get')
    def test_get_repos_valid_user(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '[{"name": "SSW567-HWs"}, {"name": "helloworld"}]'
        repos = get_repos("Generic-Sun")
        self.assertIn("SSW567-HWs", repos)
        self.assertEqual(len(repos), 2)
        mock_get.assert_called_once_with("https://api.github.com/users/Generic-Sun/repos")

    @patch('GitHubApi.requests.get')
    def test_get_repos_invalid_user(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertEqual(get_repos("fake_user_123"), [])

    @patch('GitHubApi.requests.get')
    def test_get_commits_valid_repo(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '[{"commit": "A"}, {"commit": "B"}, {"commit": "C"}]'
        self.assertEqual(get_commits("Generic-Sun", "SSW567-HWs"), 3)

    @patch('GitHubApi.requests.get')
    def test_get_commits_invalid_repo(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertEqual(get_commits("Generic-Sun", "fake_repo"), 0)

if __name__ == "__main__":
    unittest.main()