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

from docspace-api-python.models.folder_dto_string import FolderDtoString

class TestFolderDtoString(unittest.TestCase):
    """FolderDtoString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FolderDtoString:
        """Test FolderDtoString
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FolderDtoString`
        """
        model = FolderDtoString()
        if include_optional:
            return FolderDtoString(
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
                auto_delete = docspace-api-python.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
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
                id = '10',
                root_folder_id = 'some text',
                origin_id = 'some text',
                origin_room_id = 'some text',
                origin_title = 'some text',
                origin_room_title = 'some text',
                can_share = True,
                security = [{"value":true}],
                request_token = 'some text',
                parent_id = '10',
                files_count = 5,
                folders_count = 7,
                is_shareable = True,
                is_favorite = True,
                new = 1234,
                mute = True,
                tags = ["some text"],
                logo = docspace-api-python.models.logo.Logo(
                    original = 'some text', 
                    large = 'some text', 
                    medium = 'some text', 
                    small = 'some text', 
                    color = 'some text', 
                    cover = docspace-api-python.models.logo_cover.LogoCover(
                        id = '9846', 
                        data = 'some text', ), ),
                pinned = True,
                room_type = 1,
                private = True,
                indexing = True,
                deny_download = True,
                lifetime = docspace-api-python.models.room_data_lifetime_dto.RoomDataLifetimeDto(
                    delete_permanently = True, 
                    period = 0, 
                    value = 1234, 
                    enabled = True, ),
                watermark = docspace-api-python.models.watermark_dto.WatermarkDto(
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
                file_entry_type = 1
            )
        else:
            return FolderDtoString(
        )
        """

    def testFolderDtoString(self):
        """Test FolderDtoString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
