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

from docspace-api-python.models.files_settings_wrapper import FilesSettingsWrapper

class TestFilesSettingsWrapper(unittest.TestCase):
    """FilesSettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilesSettingsWrapper:
        """Test FilesSettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilesSettingsWrapper`
        """
        model = FilesSettingsWrapper()
        if include_optional:
            return FilesSettingsWrapper(
                response = docspace-api-python.models.files_settings_dto.FilesSettingsDto(
                    exts_image_previewed = ["some text"], 
                    exts_media_previewed = ["some text"], 
                    exts_web_previewed = ["some text"], 
                    exts_web_edited = ["some text"], 
                    exts_web_encrypt = ["some text"], 
                    exts_web_reviewed = ["some text"], 
                    exts_web_custom_filter_editing = ["some text"], 
                    exts_web_restricted_editing = ["some text"], 
                    exts_web_commented = ["some text"], 
                    exts_web_template = ["some text"], 
                    exts_co_authoring = ["some text"], 
                    exts_must_convert = ["some text"], 
                    exts_convertible = [{"key":"some text","value":["some text"]}], 
                    exts_uploadable = ["some text"], 
                    exts_archive = ["some text"], 
                    exts_video = ["some text"], 
                    exts_audio = ["some text"], 
                    exts_image = ["some text"], 
                    exts_spreadsheet = ["some text"], 
                    exts_presentation = ["some text"], 
                    exts_document = ["some text"], 
                    internal_formats = [{"value":"some text"}], 
                    master_form_extension = 'some text', 
                    param_version = 'some text', 
                    param_out_type = 'some text', 
                    file_download_url_string = 'some text', 
                    file_web_viewer_url_string = 'some text', 
                    file_web_viewer_external_url_string = 'some text', 
                    file_web_editor_url_string = 'some text', 
                    file_web_editor_external_url_string = 'some text', 
                    file_redirect_preview_url_string = 'some text', 
                    file_thumbnail_url_string = 'some text', 
                    confirm_delete = True, 
                    enable_third_party = True, 
                    external_share = True, 
                    external_share_social_media = True, 
                    store_original_files = True, 
                    keep_new_file_name = True, 
                    display_file_extension = True, 
                    convert_notify = True, 
                    hide_confirm_cancel_operation = True, 
                    hide_confirm_convert_save = True, 
                    hide_confirm_convert_open = True, 
                    hide_confirm_room_lifetime = True, 
                    default_order = docspace-api-python.models.order_by.OrderBy(
                        is_asc = True, 
                        property = 0, ), 
                    forcesave = True, 
                    store_forcesave = True, 
                    recent_section = True, 
                    favorites_section = True, 
                    templates_section = True, 
                    download_tar_gz = True, 
                    automatically_clean_up = docspace-api-python.models.auto_clean_up_data.AutoCleanUpData(
                        is_auto_clean_up = True, 
                        gap = 1, ), 
                    can_search_by_content = True, 
                    default_sharing_access_rights = [
                        0
                        ], 
                    max_upload_thread_count = 1234, 
                    chunk_upload_size = 1234, 
                    open_editor_in_same_tab = True, ),
                count = 56,
                links = [
                    docspace-api-python.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return FilesSettingsWrapper(
        )
        """

    def testFilesSettingsWrapper(self):
        """Test FilesSettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
