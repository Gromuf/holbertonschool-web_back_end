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


if __name__ == '__main__':
    unittest.main()
