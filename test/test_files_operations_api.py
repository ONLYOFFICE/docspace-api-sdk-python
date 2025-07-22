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

from docspace-api-sdk.api.files_operations_api import FilesOperationsApi


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
