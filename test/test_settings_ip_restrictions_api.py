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

from docspace-api-sdk.api.settings_ip_restrictions_api import SettingsIPRestrictionsApi


class TestSettingsIPRestrictionsApi(unittest.TestCase):
    """SettingsIPRestrictionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsIPRestrictionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_ip_restrictions(self) -> None:
        """Test case for get_ip_restrictions

        Get the IP portal restrictions
        """
        pass

    def test_read_ip_restrictions_settings(self) -> None:
        """Test case for read_ip_restrictions_settings

        Get the IP restriction settings
        """
        pass

    def test_save_ip_restrictions(self) -> None:
        """Test case for save_ip_restrictions

        Update the IP restrictions
        """
        pass

    def test_update_ip_restrictions_settings(self) -> None:
        """Test case for update_ip_restrictions_settings

        Update the IP restriction settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
