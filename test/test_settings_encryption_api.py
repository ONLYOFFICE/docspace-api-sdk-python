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

from docspace-api-python.api.settings_encryption_api import SettingsEncryptionApi


class TestSettingsEncryptionApi(unittest.TestCase):
    """SettingsEncryptionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsEncryptionApi()

    def tearDown(self) -> None:
        pass

    def test_get_storage_encryption_progress(self) -> None:
        """Test case for get_storage_encryption_progress

        Get the storage encryption progress
        """
        pass

    def test_get_storage_encryption_settings(self) -> None:
        """Test case for get_storage_encryption_settings

        Get the storage encryption settings
        """
        pass

    def test_start_storage_encryption(self) -> None:
        """Test case for start_storage_encryption

        Start the storage encryption process
        """
        pass


if __name__ == '__main__':
    unittest.main()
