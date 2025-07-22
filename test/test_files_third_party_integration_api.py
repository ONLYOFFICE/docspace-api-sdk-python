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

from docspace-api-sdk.api.files_third_party_integration_api import FilesThirdPartyIntegrationApi


class TestFilesThirdPartyIntegrationApi(unittest.TestCase):
    """FilesThirdPartyIntegrationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesThirdPartyIntegrationApi()

    def tearDown(self) -> None:
        pass

    def test_delete_third_party(self) -> None:
        """Test case for delete_third_party

        Remove a third-party account
        """
        pass

    def test_get_all_providers(self) -> None:
        """Test case for get_all_providers

        Get all providers
        """
        pass

    def test_get_backup_third_party_account(self) -> None:
        """Test case for get_backup_third_party_account

        Get a third-party account backup
        """
        pass

    def test_get_capabilities(self) -> None:
        """Test case for get_capabilities

        Get providers
        """
        pass

    def test_get_common_third_party_folders(self) -> None:
        """Test case for get_common_third_party_folders

        Get the common third-party services
        """
        pass

    def test_get_third_party_accounts(self) -> None:
        """Test case for get_third_party_accounts

        Get the third-party accounts
        """
        pass

    def test_save_third_party(self) -> None:
        """Test case for save_third_party

        Save a third-party account
        """
        pass

    def test_save_third_party_backup(self) -> None:
        """Test case for save_third_party_backup

        Save a third-party account backup
        """
        pass


if __name__ == '__main__':
    unittest.main()
