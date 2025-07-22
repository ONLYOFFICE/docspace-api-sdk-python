#
# (c) Copyright Ascensio System SIA 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import unittest

from docspace-api-sdk.api.api_keys_api import ApiKeysApi


class TestApiKeysApi(unittest.TestCase):
    """ApiKeysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApiKeysApi()

    def tearDown(self) -> None:
        pass

    def test_create_api_key(self) -> None:
        """Test case for create_api_key

        Create a user API key
        """
        pass

    def test_delete_api_key(self) -> None:
        """Test case for delete_api_key

        Delete a user API key
        """
        pass

    def test_get_all_permissions(self) -> None:
        """Test case for get_all_permissions

        Get API key permissions
        """
        pass

    def test_get_api_key(self) -> None:
        """Test case for get_api_key

        Get user API key info
        """
        pass

    def test_get_api_keys(self) -> None:
        """Test case for get_api_keys

        Get user API keys
        """
        pass

    def test_update_api_key(self) -> None:
        """Test case for update_api_key

        Update an API key
        """
        pass


if __name__ == '__main__':
    unittest.main()
