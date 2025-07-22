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

from docspace-api-sdk.api.settings_sso_api import SettingsSSOApi


class TestSettingsSSOApi(unittest.TestCase):
    """SettingsSSOApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsSSOApi()

    def tearDown(self) -> None:
        pass

    def test_get_default_sso_settings_v2(self) -> None:
        """Test case for get_default_sso_settings_v2

        Get the default SSO settings
        """
        pass

    def test_get_sso_settings_v2(self) -> None:
        """Test case for get_sso_settings_v2

        Get the SSO settings
        """
        pass

    def test_get_sso_settings_v2_constants(self) -> None:
        """Test case for get_sso_settings_v2_constants

        Get the SSO settings constants
        """
        pass

    def test_reset_sso_settings_v2(self) -> None:
        """Test case for reset_sso_settings_v2

        Reset the SSO settings
        """
        pass

    def test_save_sso_settings_v2(self) -> None:
        """Test case for save_sso_settings_v2

        Save the SSO settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
