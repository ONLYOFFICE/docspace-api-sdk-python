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

from docspace-api-python.api.o_auth20_client_management_api import OAuth20ClientManagementApi


class TestOAuth20ClientManagementApi(unittest.TestCase):
    """OAuth20ClientManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuth20ClientManagementApi()

    def tearDown(self) -> None:
        pass

    def test_change_activation(self) -> None:
        """Test case for change_activation

        Change the client activation status
        """
        pass

    def test_create_client(self) -> None:
        """Test case for create_client

        Create a new OAuth2 client
        """
        pass

    def test_delete_client(self) -> None:
        """Test case for delete_client

        Delete an OAuth2 client
        """
        pass

    def test_regenerate_secret(self) -> None:
        """Test case for regenerate_secret

        Regenerate the client secret
        """
        pass

    def test_revoke_user_client(self) -> None:
        """Test case for revoke_user_client

        Revoke client consent
        """
        pass

    def test_update_client(self) -> None:
        """Test case for update_client

        Update an existing OAuth2 client
        """
        pass


if __name__ == '__main__':
    unittest.main()
