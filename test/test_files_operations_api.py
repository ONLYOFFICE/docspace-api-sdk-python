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

from docspace.api.files_operations_api import FilesOperationsApi


class TestFilesOperationsApi(unittest.TestCase):
    """FilesOperationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesOperationsApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_download(self) -> None:
        """Test case for bulk_download

        Bulk download
        """
        pass

    def test_check_conversion_status(self) -> None:
        """Test case for check_conversion_status

        Get conversion status
        """
        pass

    def test_check_move_or_copy_batch_items(self) -> None:
        """Test case for check_move_or_copy_batch_items

        Check and move or copy to a folder
        """
        pass

    def test_check_move_or_copy_dest_folder(self) -> None:
        """Test case for check_move_or_copy_dest_folder

        Check for moving or copying to a folder
        """
        pass

    def test_copy_batch_items(self) -> None:
        """Test case for copy_batch_items

        Copy to the folder
        """
        pass

    def test_create_upload_session(self) -> None:
        """Test case for create_upload_session

        Chunked upload
        """
        pass

    def test_delete_batch_items(self) -> None:
        """Test case for delete_batch_items

        Delete files and folders
        """
        pass

    def test_delete_file_versions(self) -> None:
        """Test case for delete_file_versions

        Delete file versions
        """
        pass

    def test_duplicate_batch_items(self) -> None:
        """Test case for duplicate_batch_items

        Duplicate files and folders
        """
        pass

    def test_empty_trash(self) -> None:
        """Test case for empty_trash

        Empty the \"Trash\" folder
        """
        pass

    def test_get_operation_statuses(self) -> None:
        """Test case for get_operation_statuses

        Get active file operations
        """
        pass

    def test_get_operation_statuses_by_type(self) -> None:
        """Test case for get_operation_statuses_by_type

        Get file operation statuses
        """
        pass

    def test_mark_as_read(self) -> None:
        """Test case for mark_as_read

        Mark as read
        """
        pass

    def test_move_batch_items(self) -> None:
        """Test case for move_batch_items

        Move or copy to a folder
        """
        pass

    def test_start_file_conversion(self) -> None:
        """Test case for start_file_conversion

        Start file conversion
        """
        pass

    def test_terminate_tasks(self) -> None:
        """Test case for terminate_tasks

        Finish active operations
        """
        pass

    def test_update_file_comment(self) -> None:
        """Test case for update_file_comment

        Update a comment
        """
        pass


if __name__ == '__main__':
    unittest.main()
