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

from docspace-api-python.models.new_items_dto_room_new_items_dto import NewItemsDtoRoomNewItemsDto

class TestNewItemsDtoRoomNewItemsDto(unittest.TestCase):
    """NewItemsDtoRoomNewItemsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewItemsDtoRoomNewItemsDto:
        """Test NewItemsDtoRoomNewItemsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewItemsDtoRoomNewItemsDto`
        """
        model = NewItemsDtoRoomNewItemsDto()
        if include_optional:
            return NewItemsDtoRoomNewItemsDto(
                var_date = docspace-api-python.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
                items = [
                    docspace-api-python.models.room_new_items_dto.RoomNewItemsDto(
                        room = docspace-api-python.models.file_entry_dto.FileEntryDto(
                            title = 'Some titile.txt/ Some title', 
                            access = 0, 
                            shared = False, 
                            created = docspace-api-python.models.api_date_time.ApiDateTime(
                                utc_time = '2008-04-10T06:30+04:00', 
                                time_zone_offset = '00:00:00', ), 
                            created_by = docspace-api-python.models.employee_dto.EmployeeDto(
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
                            updated = docspace-api-python.models.api_date_time.ApiDateTime(
                                utc_time = '2008-04-10T06:30+04:00', 
                                time_zone_offset = '00:00:00', ), 
                            auto_delete = , 
                            root_folder_type = 0, 
                            parent_room_type = 0, 
                            updated_by = docspace-api-python.models.employee_dto.EmployeeDto(
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
                            file_entry_type = 1, ), 
                        items = [
                            docspace-api-python.models.file_entry_dto.FileEntryDto(
                                title = 'Some titile.txt/ Some title', 
                                shared = False, 
                                provider_item = True, 
                                provider_key = 'some text', 
                                provider_id = 1234, 
                                order = 'some text', )
                            ], )
                    ]
            )
        else:
            return NewItemsDtoRoomNewItemsDto(
        )
        """

    def testNewItemsDtoRoomNewItemsDto(self):
        """Test NewItemsDtoRoomNewItemsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
