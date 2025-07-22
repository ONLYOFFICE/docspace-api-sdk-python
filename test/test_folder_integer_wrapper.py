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

from docspace-api-sdk.models.folder_integer_wrapper import FolderIntegerWrapper

class TestFolderIntegerWrapper(unittest.TestCase):
    """FolderIntegerWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FolderIntegerWrapper:
        """Test FolderIntegerWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FolderIntegerWrapper`
        """
        model = FolderIntegerWrapper()
        if include_optional:
            return FolderIntegerWrapper(
                response = docspace-api-sdk.models.folder_dto_integer.FolderDtoInteger(
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
                    parent_id = 10, 
                    files_count = 5, 
                    folders_count = 7, 
                    is_shareable = True, 
                    is_favorite = True, 
                    new = 1234, 
                    mute = True, 
                    tags = ["some text"], 
                    logo = docspace-api-sdk.models.logo.Logo(
                        original = 'some text', 
                        large = 'some text', 
                        medium = 'some text', 
                        small = 'some text', 
                        color = 'some text', 
                        cover = docspace-api-sdk.models.logo_cover.LogoCover(
                            id = '9846', 
                            data = 'some text', ), ), 
                    pinned = True, 
                    room_type = 1, 
                    private = True, 
                    indexing = True, 
                    deny_download = True, 
                    lifetime = docspace-api-sdk.models.room_data_lifetime_dto.RoomDataLifetimeDto(
                        delete_permanently = True, 
                        period = 0, 
                        value = 1234, 
                        enabled = True, ), 
                    watermark = docspace-api-sdk.models.watermark_dto.WatermarkDto(
                        additions = 1, 
                        text = 'some text', 
                        rotate = 1234, 
                        image_scale = 1234, 
                        image_url = 'some text', 
                        image_height = -8.5, 
                        image_width = -8.5, ), 
                    type = 0, 
                    in_room = True, 
                    quota_limit = 1234, 
                    is_custom_quota = True, 
                    used_space = 1234, 
                    external = True, 
                    password_protected = True, 
                    expired = True, 
                    file_entry_type = 1, ),
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
            return FolderIntegerWrapper(
        )
        """

    def testFolderIntegerWrapper(self):
        """Test FolderIntegerWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
