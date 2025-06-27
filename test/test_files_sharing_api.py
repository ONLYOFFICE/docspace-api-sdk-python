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

from docspace.api.files_sharing_api import FilesSharingApi


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
