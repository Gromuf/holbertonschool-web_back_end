#!/usr/bin/env python3
"""test_utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map, path, expected_message):
        """test_access_nested_map_exception"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), "'{}'".format(expected_message))


class TestGetJson(unittest.TestCase):
    """TestGetJson"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected_payload):
        """test_get_json"""
        from utils import get_json
        from unittest.mock import patch, Mock

        mock_response = Mock()
        mock_response.json.return_value = expected_payload

        with patch('utils.requests.get',
                   return_value=mock_response) as mock_get:
            payload = get_json(url)
            self.assertEqual(payload, expected_payload)
            mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
