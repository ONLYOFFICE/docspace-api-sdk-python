# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



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
