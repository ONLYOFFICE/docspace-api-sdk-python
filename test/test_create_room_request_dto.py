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

from docspace-api-sdk.models.create_room_request_dto import CreateRoomRequestDto

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
                lifetime = docspace-api-sdk.models.room_data_lifetime_dto.RoomDataLifetimeDto(
                    delete_permanently = True, 
                    period = 0, 
                    value = 1234, 
                    enabled = True, ),
                watermark = docspace-api-sdk.models.watermark_request_dto.WatermarkRequestDto(
                    enabled = True, 
                    additions = 1, 
                    text = 'some text', 
                    rotate = 1234, 
                    image_scale = 1234, 
                    image_url = 'some text', 
                    image_height = -8.5, 
                    image_width = -8.5, ),
                logo = docspace-api-sdk.models.logo_request.LogoRequest(
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
                    docspace-api-sdk.models.file_share_params.FileShareParams(
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
