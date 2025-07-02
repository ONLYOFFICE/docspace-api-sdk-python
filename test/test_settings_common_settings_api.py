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

from docspace-api-python.api.settings_common_settings_api import SettingsCommonSettingsApi


class TestSettingsCommonSettingsApi(unittest.TestCase):
    """SettingsCommonSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsCommonSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_close_admin_helper(self) -> None:
        """Test case for close_admin_helper

        Close the admin helper
        """
        pass

    def test_complete_wizard(self) -> None:
        """Test case for complete_wizard

        Complete the Wizard settings
        """
        pass

    def test_configure_deep_link(self) -> None:
        """Test case for configure_deep_link

        Configure the deep link settings
        """
        pass

    def test_delete_portal_color_theme(self) -> None:
        """Test case for delete_portal_color_theme

        Delete a color theme
        """
        pass

    def test_get_deep_link_settings(self) -> None:
        """Test case for get_deep_link_settings

        Get the deep link settings
        """
        pass

    def test_get_payment_settings(self) -> None:
        """Test case for get_payment_settings

        Get the payment settings
        """
        pass

    def test_get_portal_color_theme(self) -> None:
        """Test case for get_portal_color_theme

        Get a color theme
        """
        pass

    def test_get_portal_hostname(self) -> None:
        """Test case for get_portal_hostname

        Get hostname
        """
        pass

    def test_get_portal_logo(self) -> None:
        """Test case for get_portal_logo

        Get a portal logo
        """
        pass

    def test_get_portal_settings(self) -> None:
        """Test case for get_portal_settings

        Get the portal settings
        """
        pass

    def test_get_socket_settings(self) -> None:
        """Test case for get_socket_settings

        Get the socket settings
        """
        pass

    def test_get_supported_cultures(self) -> None:
        """Test case for get_supported_cultures

        Get supported languages
        """
        pass

    def test_get_tenant_user_invitation_settings(self) -> None:
        """Test case for get_tenant_user_invitation_settings

        Get the user invitation settings
        """
        pass

    def test_get_time_zones(self) -> None:
        """Test case for get_time_zones

        Get time zones
        """
        pass

    def test_save_dns_settings(self) -> None:
        """Test case for save_dns_settings

        Save the DNS settings
        """
        pass

    def test_save_mail_domain_settings(self) -> None:
        """Test case for save_mail_domain_settings

        Save the mail domain settings
        """
        pass

    def test_save_portal_color_theme(self) -> None:
        """Test case for save_portal_color_theme

        Save a color theme
        """
        pass

    def test_update_email_activation_settings(self) -> None:
        """Test case for update_email_activation_settings

        Update the email activation settings
        """
        pass

    def test_update_invitation_settings(self) -> None:
        """Test case for update_invitation_settings

        Update user invitation settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
