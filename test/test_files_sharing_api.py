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

from docspace-api-sdk.api.files_sharing_api import FilesSharingApi


class TestFilesSharingApi(unittest.TestCase):
    """FilesSharingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesSharingApi()

    def tearDown(self) -> None:
        pass

    def test_apply_external_share_password(self) -> None:
        """Test case for apply_external_share_password

        Apply external data password
        """
        pass

    def test_change_file_owner(self) -> None:
        """Test case for change_file_owner

        Change the file owner
        """
        pass

    def test_get_external_share_data(self) -> None:
        """Test case for get_external_share_data

        Get the external data
        """
        pass

    def test_get_shared_users(self) -> None:
        """Test case for get_shared_users

        Get user access rights by file ID
        """
        pass

    def test_send_editor_notify(self) -> None:
        """Test case for send_editor_notify

        Send the mention message
        """
        pass


if __name__ == '__main__':
    unittest.main()
