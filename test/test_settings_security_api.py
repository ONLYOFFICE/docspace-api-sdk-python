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

from docspace-api-python.api.settings_security_api import SettingsSecurityApi


class TestSettingsSecurityApi(unittest.TestCase):
    """SettingsSecurityApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsSecurityApi()

    def tearDown(self) -> None:
        pass

    def test_get_enabled_modules(self) -> None:
        """Test case for get_enabled_modules

        Get the enabled modules
        """
        pass

    def test_get_is_product_administrator(self) -> None:
        """Test case for get_is_product_administrator

        Check a product administrator
        """
        pass

    def test_get_password_settings(self) -> None:
        """Test case for get_password_settings

        Get the password settings
        """
        pass

    def test_get_product_administrators(self) -> None:
        """Test case for get_product_administrators

        Get the product administrators
        """
        pass

    def test_get_web_item_security_info(self) -> None:
        """Test case for get_web_item_security_info

        Get the module availability
        """
        pass

    def test_get_web_item_settings_security_info(self) -> None:
        """Test case for get_web_item_settings_security_info

        Get the security settings
        """
        pass

    def test_set_access_to_web_items(self) -> None:
        """Test case for set_access_to_web_items

        Set the security settings to modules
        """
        pass

    def test_set_product_administrator(self) -> None:
        """Test case for set_product_administrator

        Set a product administrator
        """
        pass

    def test_set_web_item_security(self) -> None:
        """Test case for set_web_item_security

        Set the module security settings
        """
        pass

    def test_update_password_settings(self) -> None:
        """Test case for update_password_settings

        Set the password settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
