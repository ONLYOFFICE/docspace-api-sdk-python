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

from docspace-api-sdk.models.room_template_dto import RoomTemplateDto

class TestRoomTemplateDto(unittest.TestCase):
    """RoomTemplateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomTemplateDto:
        """Test RoomTemplateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomTemplateDto`
        """
        model = RoomTemplateDto()
        if include_optional:
            return RoomTemplateDto(
                room_id = 9846,
                title = 'legacy_1080p_small_wooden_mouse',
                logo = docspace-api-sdk.models.logo_request.LogoRequest(
                    tmp_file = 'some text', 
                    x = 1234, 
                    y = 1234, 
                    width = 56, 
                    height = 56, ),
                copy_logo = True,
                share = ["some text"],
                groups = ["75a5f745-f697-4418-b38d-0fe0d277e258"],
                public = True,
                tags = ["some text"],
                color = 'some text',
                cover = 'some text',
                quota = 1234
            )
        else:
            return RoomTemplateDto(
                room_id = 9846,
        )
        """

    def testRoomTemplateDto(self):
        """Test RoomTemplateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
