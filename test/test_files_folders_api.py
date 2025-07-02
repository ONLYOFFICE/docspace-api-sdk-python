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

from docspace-api-python.api.files_folders_api import FilesFoldersApi


class TestFilesFoldersApi(unittest.TestCase):
    """FilesFoldersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesFoldersApi()

    def tearDown(self) -> None:
        pass

    def test_check_upload(self) -> None:
        """Test case for check_upload

        Check file uploads
        """
        pass

    def test_create_folder(self) -> None:
        """Test case for create_folder

        Create a folder
        """
        pass

    def test_delete_folder(self) -> None:
        """Test case for delete_folder

        Delete a folder
        """
        pass

    def test_get_files_used_space(self) -> None:
        """Test case for get_files_used_space

        Get used space of files
        """
        pass

    def test_get_folder(self) -> None:
        """Test case for get_folder

        Get folder form filter
        """
        pass

    def test_get_folder_by_folder_id(self) -> None:
        """Test case for get_folder_by_folder_id

        Get a folder by ID
        """
        pass

    def test_get_folder_history(self) -> None:
        """Test case for get_folder_history

        Get folder history
        """
        pass

    def test_get_folder_info(self) -> None:
        """Test case for get_folder_info

        Get folder information
        """
        pass

    def test_get_folder_path(self) -> None:
        """Test case for get_folder_path

        Get the folder path
        """
        pass

    def test_get_folder_primary_external_link(self) -> None:
        """Test case for get_folder_primary_external_link

        Get primary external link
        """
        pass

    def test_get_folders(self) -> None:
        """Test case for get_folders

        Get subfolders
        """
        pass

    def test_get_my_folder(self) -> None:
        """Test case for get_my_folder

        Get the \"My documents\" section
        """
        pass

    def test_get_new_folder_items(self) -> None:
        """Test case for get_new_folder_items

        Get new folder items
        """
        pass

    def test_get_privacy_folder(self) -> None:
        """Test case for get_privacy_folder

        Get the \"Private Room\" section
        """
        pass

    def test_get_root_folders(self) -> None:
        """Test case for get_root_folders

        Get filtered sections
        """
        pass

    def test_get_trash_folder(self) -> None:
        """Test case for get_trash_folder

        Get the \"Trash\" section
        """
        pass

    def test_insert_file(self) -> None:
        """Test case for insert_file

        Insert a file
        """
        pass

    def test_insert_file_to_my_from_body(self) -> None:
        """Test case for insert_file_to_my_from_body

        Insert a file to the \"My documents\" section
        """
        pass

    def test_rename_folder(self) -> None:
        """Test case for rename_folder

        Rename a folder
        """
        pass

    def test_set_folder_order(self) -> None:
        """Test case for set_folder_order

        Set folder order
        """
        pass

    def test_upload_file(self) -> None:
        """Test case for upload_file

        Upload a file
        """
        pass

    def test_upload_file_to_my(self) -> None:
        """Test case for upload_file_to_my

        Upload a file to the \"My documents\" section
        """
        pass


if __name__ == '__main__':
    unittest.main()
