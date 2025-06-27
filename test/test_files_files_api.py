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

from docspace.api.files_files_api import FilesFilesApi


class TestFilesFilesApi(unittest.TestCase):
    """FilesFilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesFilesApi()

    def tearDown(self) -> None:
        pass

    def test_add_templates(self) -> None:
        """Test case for add_templates

        Add template files
        """
        pass

    def test_change_version_history(self) -> None:
        """Test case for change_version_history

        Change version history
        """
        pass

    def test_check_fill_form_draft(self) -> None:
        """Test case for check_fill_form_draft

        Check the form draft filling
        """
        pass

    def test_copy_file_as(self) -> None:
        """Test case for copy_file_as

        Copy a file
        """
        pass

    def test_create_edit_session(self) -> None:
        """Test case for create_edit_session

        Create the editing session
        """
        pass

    def test_create_file(self) -> None:
        """Test case for create_file

        Create a file
        """
        pass

    def test_create_file_in_my_documents(self) -> None:
        """Test case for create_file_in_my_documents

        Create a file in the \"My documents\" section
        """
        pass

    def test_create_html_file(self) -> None:
        """Test case for create_html_file

        Create an HTML file
        """
        pass

    def test_create_html_file_in_my_documents(self) -> None:
        """Test case for create_html_file_in_my_documents

        Create an HTML file in the \"My documents\" section
        """
        pass

    def test_create_primary_external_link(self) -> None:
        """Test case for create_primary_external_link

        Create primary external link
        """
        pass

    def test_create_text_file(self) -> None:
        """Test case for create_text_file

        Create a text file
        """
        pass

    def test_create_text_file_in_my_documents(self) -> None:
        """Test case for create_text_file_in_my_documents

        Create a text file in the \"My documents\" section
        """
        pass

    def test_create_thumbnails(self) -> None:
        """Test case for create_thumbnails

        Create file thumbnails
        """
        pass

    def test_delete_file(self) -> None:
        """Test case for delete_file

        Delete a file
        """
        pass

    def test_delete_recent(self) -> None:
        """Test case for delete_recent

        Delete recent files
        """
        pass

    def test_delete_templates(self) -> None:
        """Test case for delete_templates

        Delete template files
        """
        pass

    def test_get_all_form_roles(self) -> None:
        """Test case for get_all_form_roles

        Get form roles
        """
        pass

    def test_get_edit_diff_url(self) -> None:
        """Test case for get_edit_diff_url

        Get changes URL
        """
        pass

    def test_get_edit_history(self) -> None:
        """Test case for get_edit_history

        Get version history
        """
        pass

    def test_get_file_history(self) -> None:
        """Test case for get_file_history

        Get file history
        """
        pass

    def test_get_file_info(self) -> None:
        """Test case for get_file_info

        Get file information
        """
        pass

    def test_get_file_links(self) -> None:
        """Test case for get_file_links

        Get file external links
        """
        pass

    def test_get_file_primary_external_link(self) -> None:
        """Test case for get_file_primary_external_link

        Get primary external link
        """
        pass

    def test_get_file_version_info(self) -> None:
        """Test case for get_file_version_info

        Get file versions
        """
        pass

    def test_get_fill_result(self) -> None:
        """Test case for get_fill_result

        Get form-filling result
        """
        pass

    def test_get_presigned_file_uri(self) -> None:
        """Test case for get_presigned_file_uri

        Get file download link asynchronously
        """
        pass

    def test_get_presigned_uri(self) -> None:
        """Test case for get_presigned_uri

        Get file download link
        """
        pass

    def test_get_protected_file_users(self) -> None:
        """Test case for get_protected_file_users

        Get users access rights to the protected file
        """
        pass

    def test_get_reference_data(self) -> None:
        """Test case for get_reference_data

        Get reference data
        """
        pass

    def test_is_form_pdf(self) -> None:
        """Test case for is_form_pdf

        Check the PDF file
        """
        pass

    def test_lock_file(self) -> None:
        """Test case for lock_file

        Lock a file
        """
        pass

    def test_manage_form_filling(self) -> None:
        """Test case for manage_form_filling

        Perform form filling action
        """
        pass

    def test_open_edit_file(self) -> None:
        """Test case for open_edit_file

        Open a file configuration
        """
        pass

    def test_restore_file_version(self) -> None:
        """Test case for restore_file_version

        Restore a file version
        """
        pass

    def test_save_editing_file_from_form(self) -> None:
        """Test case for save_editing_file_from_form

        Save file edits
        """
        pass

    def test_save_file_as_pdf(self) -> None:
        """Test case for save_file_as_pdf

        Save a file as PDF
        """
        pass

    def test_save_form_role_mapping(self) -> None:
        """Test case for save_form_role_mapping

        Save form role mapping
        """
        pass

    def test_set_custom_filter_tag(self) -> None:
        """Test case for set_custom_filter_tag

        Set the Custom Filter editing mode
        """
        pass

    def test_set_external_link(self) -> None:
        """Test case for set_external_link

        Set an external link
        """
        pass

    def test_set_file_order(self) -> None:
        """Test case for set_file_order

        Set file order
        """
        pass

    def test_set_files_order(self) -> None:
        """Test case for set_files_order

        Set order of files
        """
        pass

    def test_start_edit_file(self) -> None:
        """Test case for start_edit_file

        Start file editing
        """
        pass

    def test_start_filling_file(self) -> None:
        """Test case for start_filling_file

        Start file filling
        """
        pass

    def test_track_edit_file(self) -> None:
        """Test case for track_edit_file

        Track file editing
        """
        pass

    def test_update_file(self) -> None:
        """Test case for update_file

        Update a file
        """
        pass


if __name__ == '__main__':
    unittest.main()
