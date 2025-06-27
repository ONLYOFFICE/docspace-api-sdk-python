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

from docspace.api.settings_tfa_settings_api import SettingsTFASettingsApi


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
