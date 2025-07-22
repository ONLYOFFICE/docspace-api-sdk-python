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

from docspace-api-sdk.models.file_integer_array_wrapper import FileIntegerArrayWrapper

class TestFileIntegerArrayWrapper(unittest.TestCase):
    """FileIntegerArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileIntegerArrayWrapper:
        """Test FileIntegerArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileIntegerArrayWrapper`
        """
        model = FileIntegerArrayWrapper()
        if include_optional:
            return FileIntegerArrayWrapper(
                response = [
                    docspace-api-sdk.models.file_dto_integer.FileDtoInteger(
                        title = 'Some titile.txt/ Some title', 
                        access = 0, 
                        shared = False, 
                        created = docspace-api-sdk.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        created_by = docspace-api-sdk.models.employee_dto.EmployeeDto(
                            id = '', 
                            display_name = 'Mike Zanyatski', 
                            title = 'Manager', 
                            avatar = 'some text', 
                            avatar_original = 'some text', 
                            avatar_max = 'some text', 
                            avatar_medium = 'some text', 
                            avatar_small = 'url to small avatar', 
                            profile_url = 'some text', 
                            has_avatar = True, 
                            is_anonim = True, ), 
                        updated = docspace-api-sdk.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        auto_delete = , 
                        root_folder_type = 0, 
                        parent_room_type = 0, 
                        updated_by = docspace-api-sdk.models.employee_dto.EmployeeDto(
                            id = '', 
                            display_name = 'Mike Zanyatski', 
                            title = 'Manager', 
                            avatar = 'some text', 
                            avatar_original = 'some text', 
                            avatar_max = 'some text', 
                            avatar_medium = 'some text', 
                            avatar_small = 'url to small avatar', 
                            profile_url = 'some text', 
                            has_avatar = True, 
                            is_anonim = True, ), 
                        provider_item = True, 
                        provider_key = 'some text', 
                        provider_id = 1234, 
                        order = 'some text', 
                        id = 10, 
                        root_folder_id = 1234, 
                        origin_id = 1234, 
                        origin_room_id = 1234, 
                        origin_title = 'some text', 
                        origin_room_title = 'some text', 
                        can_share = True, 
                        security = [{"value":true}], 
                        request_token = 'some text', 
                        folder_id = 9846, 
                        version = 3, 
                        version_group = 1, 
                        content_length = '12345', 
                        pure_content_length = 1234, 
                        file_status = 0, 
                        mute = False, 
                        view_url = 'https://www.onlyoffice.com/viewfile?fileid=2221', 
                        web_url = 'some text', 
                        short_web_url = 'some text', 
                        file_type = 0, 
                        file_exst = '.txt', 
                        comment = 'some text', 
                        encrypted = False, 
                        thumbnail_url = 'some text', 
                        thumbnail_status = 0, 
                        locked = True, 
                        locked_by = 'some text', 
                        has_draft = False, 
                        form_filling_status = 0, 
                        is_form = False, 
                        custom_filter_enabled = True, 
                        custom_filter_enabled_by = 'some text', 
                        start_filling = False, 
                        in_process_folder_id = 1234, 
                        in_process_folder_title = 'some text', 
                        draft_location = docspace-api-sdk.models.draft_location_integer.DraftLocationInteger(
                            folder_id = 9846, 
                            folder_title = 'some text', 
                            file_id = 9846, 
                            file_title = 'some text', ), 
                        view_accessibility = [{"value":true}], 
                        available_external_rights = [{"key":"some text","value":true}], 
                        last_opened = , 
                        expired = , 
                        file_entry_type = 1, )
                    ],
                count = 56,
                links = [
                    docspace-api-sdk.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return FileIntegerArrayWrapper(
        )
        """

    def testFileIntegerArrayWrapper(self):
        """Test FileIntegerArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
