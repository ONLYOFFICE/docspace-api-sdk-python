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

from docspace-api-python.api.settings_rebranding_api import SettingsRebrandingApi


class TestSettingsRebrandingApi(unittest.TestCase):
    """SettingsRebrandingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsRebrandingApi()

    def tearDown(self) -> None:
        pass

    def test_delete_additional_white_label_settings(self) -> None:
        """Test case for delete_additional_white_label_settings

        Delete the additional white label settings
        """
        pass

    def test_delete_company_white_label_settings(self) -> None:
        """Test case for delete_company_white_label_settings

        Delete the company white label settings
        """
        pass

    def test_get_additional_white_label_settings(self) -> None:
        """Test case for get_additional_white_label_settings

        Get the additional white label settings
        """
        pass

    def test_get_company_white_label_settings(self) -> None:
        """Test case for get_company_white_label_settings

        Get the company white label settings
        """
        pass

    def test_get_enable_whitelabel(self) -> None:
        """Test case for get_enable_whitelabel

        Check the white label availability
        """
        pass

    def test_get_is_default_white_label_logo_text(self) -> None:
        """Test case for get_is_default_white_label_logo_text

        Check the default white label logo text
        """
        pass

    def test_get_is_default_white_label_logos(self) -> None:
        """Test case for get_is_default_white_label_logos

        Check the default white label logos
        """
        pass

    def test_get_licensor_data(self) -> None:
        """Test case for get_licensor_data

        Get the licensor data
        """
        pass

    def test_get_white_label_logo_text(self) -> None:
        """Test case for get_white_label_logo_text

        Get the white label logo text
        """
        pass

    def test_get_white_label_logos(self) -> None:
        """Test case for get_white_label_logos

        Get the white label logos
        """
        pass

    def test_restore_white_label_logo_text(self) -> None:
        """Test case for restore_white_label_logo_text

        Restore the white label logo text
        """
        pass

    def test_restore_white_label_logos(self) -> None:
        """Test case for restore_white_label_logos

        Restore the white label logos
        """
        pass

    def test_save_additional_white_label_settings(self) -> None:
        """Test case for save_additional_white_label_settings

        Save the additional white label settings
        """
        pass

    def test_save_company_white_label_settings(self) -> None:
        """Test case for save_company_white_label_settings

        Save the company white label settings
        """
        pass

    def test_save_white_label_logo_text(self) -> None:
        """Test case for save_white_label_logo_text

        Save the white label logo text settings
        """
        pass

    def test_save_white_label_settings(self) -> None:
        """Test case for save_white_label_settings

        Save the white label logos
        """
        pass

    def test_save_white_label_settings_from_files(self) -> None:
        """Test case for save_white_label_settings_from_files

        Save the white label logos from files
        """
        pass


if __name__ == '__main__':
    unittest.main()
