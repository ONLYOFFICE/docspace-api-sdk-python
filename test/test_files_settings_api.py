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

from docspace-api-python.api.files_settings_api import FilesSettingsApi


class TestFilesSettingsApi(unittest.TestCase):
    """FilesSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_change_access_to_thirdparty(self) -> None:
        """Test case for change_access_to_thirdparty

        Change the third-party settings access
        """
        pass

    def test_change_automatically_clean_up(self) -> None:
        """Test case for change_automatically_clean_up

        Update the trash bin auto-clearing setting
        """
        pass

    def test_change_default_access_rights(self) -> None:
        """Test case for change_default_access_rights

        Change the default access rights
        """
        pass

    def test_change_delete_confirm(self) -> None:
        """Test case for change_delete_confirm

        Confirm the file deletion
        """
        pass

    def test_change_download_zip_from_body(self) -> None:
        """Test case for change_download_zip_from_body

        Change the archive format (using body parameters)
        """
        pass

    def test_check_doc_service_url(self) -> None:
        """Test case for check_doc_service_url

        Check the document service URL
        """
        pass

    def test_display_file_extension(self) -> None:
        """Test case for display_file_extension

        Display a file extension
        """
        pass

    def test_external_share(self) -> None:
        """Test case for external_share

        Change the external sharing ability
        """
        pass

    def test_external_share_social_media(self) -> None:
        """Test case for external_share_social_media

        Change the external sharing ability on social networks
        """
        pass

    def test_forcesave(self) -> None:
        """Test case for forcesave

        Change the forcesaving ability
        """
        pass

    def test_get_automatically_clean_up(self) -> None:
        """Test case for get_automatically_clean_up

        Get the trash bin auto-clearing setting
        """
        pass

    def test_get_doc_service_url(self) -> None:
        """Test case for get_doc_service_url

        Get the document service URL
        """
        pass

    def test_get_files_module(self) -> None:
        """Test case for get_files_module

        Get the \"Documents\" information
        """
        pass

    def test_get_files_settings(self) -> None:
        """Test case for get_files_settings

        Get file settings
        """
        pass

    def test_hide_confirm_cancel_operation(self) -> None:
        """Test case for hide_confirm_cancel_operation

        Hide confirmation dialog when canceling operations
        """
        pass

    def test_hide_confirm_convert(self) -> None:
        """Test case for hide_confirm_convert

        Hide the confirmation dialog when converting
        """
        pass

    def test_hide_confirm_room_lifetime(self) -> None:
        """Test case for hide_confirm_room_lifetime

        Hide confirmation dialog when changing room lifetime settings
        """
        pass

    def test_is_available_privacy_room_settings(self) -> None:
        """Test case for is_available_privacy_room_settings

        Check the \"Private Room\" availability
        """
        pass

    def test_keep_new_file_name(self) -> None:
        """Test case for keep_new_file_name

        Ask a new file name
        """
        pass

    def test_set_open_editor_in_same_tab(self) -> None:
        """Test case for set_open_editor_in_same_tab

        Open document in the same browser tab
        """
        pass

    def test_store_forcesave(self) -> None:
        """Test case for store_forcesave

        Change the ability to store the forcesaved files
        """
        pass

    def test_store_original(self) -> None:
        """Test case for store_original

        Change the ability to upload original formats
        """
        pass

    def test_update_file_if_exist(self) -> None:
        """Test case for update_file_if_exist

        Update a file version if it exists
        """
        pass


if __name__ == '__main__':
    unittest.main()
