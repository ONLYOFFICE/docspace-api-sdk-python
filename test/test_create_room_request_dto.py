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

from docspace.models.create_room_request_dto import CreateRoomRequestDto

class TestCreateRoomRequestDto(unittest.TestCase):
    """CreateRoomRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRoomRequestDto:
        """Test CreateRoomRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRoomRequestDto`
        """
        model = CreateRoomRequestDto()
        if include_optional:
            return CreateRoomRequestDto(
                title = 'legacy_1080p_small_wooden_mouse',
                quota = 1234,
                indexing = True,
                deny_download = True,
                lifetime = docspace.models.room_data_lifetime_dto.RoomDataLifetimeDto(
                    delete_permanently = True, 
                    period = 0, 
                    value = 1234, 
                    enabled = True, ),
                watermark = docspace.models.watermark_request_dto.WatermarkRequestDto(
                    enabled = True, 
                    additions = 1, 
                    text = 'some text', 
                    rotate = 1234, 
                    image_scale = 1234, 
                    image_url = 'some text', 
                    image_height = -8.5, 
                    image_width = -8.5, ),
                logo = docspace.models.logo_request.LogoRequest(
                    tmp_file = 'some text', 
                    x = 1234, 
                    y = 1234, 
                    width = 56, 
                    height = 56, ),
                tags = ["some text"],
                color = 'some text',
                cover = 'some text',
                room_type = 1,
                private = True,
                share = [
                    docspace.models.file_share_params.FileShareParams(
                        share_to = '75a5f745-f697-4418-b38d-0fe0d277e258', 
                        email = 'Sydney_Roberts4@hotmail.com', 
                        access = 0, )
                    ]
            )
        else:
            return CreateRoomRequestDto(
                title = 'legacy_1080p_small_wooden_mouse',
                room_type = 1,
        )
        """

    def testCreateRoomRequestDto(self):
        """Test CreateRoomRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
