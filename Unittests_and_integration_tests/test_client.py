#!/usr/bin/env python3
"""test_client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test that github org client org method returns the correct value"""
        payload = {"payload": True}
        mock_get_json.return_value = payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @parameterized.expand([
        ({"repos_url": "https://api.github.com/orgs/google/repos"},),
        ({"repos_url": "https://api.github.com/orgs/abc/repos"},),
    ])
    def test_public_repos_url(self, org_payload):
        """test that the _public_repos_url method returns the correct URL"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url,
                             org_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        test_url = "https://api.github.com/orgs/test_org/repos"
        client = GithubOrgClient("test_org")
        with patch.object(type(client),
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value=test_url
                          ) as mock_repos_url:
            repos = client.public_repos()
            self.assertEqual(repos, [
                             "repo1", "repo2", "repo3"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


if __name__ == '__main__':
    unittest.main()
