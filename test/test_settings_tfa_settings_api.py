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

from docspace-api-sdk.api.settings_tfa_settings_api import SettingsTFASettingsApi


class TestSettingsTFASettingsApi(unittest.TestCase):
    """SettingsTFASettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsTFASettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_tfa_app_codes(self) -> None:
        """Test case for get_tfa_app_codes

        Get the TFA codes
        """
        pass

    def test_get_tfa_confirm_url(self) -> None:
        """Test case for get_tfa_confirm_url

        Get confirmation email
        """
        pass

    def test_get_tfa_settings(self) -> None:
        """Test case for get_tfa_settings

        Get the TFA settings
        """
        pass

    def test_tfa_app_generate_setup_code(self) -> None:
        """Test case for tfa_app_generate_setup_code

        Generate setup code
        """
        pass

    def test_tfa_validate_auth_code(self) -> None:
        """Test case for tfa_validate_auth_code

        Validate the TFA code
        """
        pass

    def test_unlink_tfa_app(self) -> None:
        """Test case for unlink_tfa_app

        Unlink the TFA application
        """
        pass

    def test_update_tfa_app_codes(self) -> None:
        """Test case for update_tfa_app_codes

        Update the TFA codes
        """
        pass

    def test_update_tfa_settings(self) -> None:
        """Test case for update_tfa_settings

        Update the TFA settings
        """
        pass

    def test_update_tfa_settings_link(self) -> None:
        """Test case for update_tfa_settings_link

        Get a confirmation email for updating TFA settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
