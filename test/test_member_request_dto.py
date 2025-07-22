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

from docspace-api-sdk.models.member_request_dto import MemberRequestDto

class TestMemberRequestDto(unittest.TestCase):
    """MemberRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberRequestDto:
        """Test MemberRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberRequestDto`
        """
        model = MemberRequestDto()
        if include_optional:
            return MemberRequestDto(
                password = 'vfmf2vO1Kp',
                password_hash = 'some text',
                email = 'Sydney_Roberts4@hotmail.com',
                type = 0,
                is_user = True,
                first_name = 'Winfield',
                last_name = 'Wyman',
                department = ["75a5f745-f697-4418-b38d-0fe0d277e258"],
                title = 'legacy_1080p_small_wooden_mouse',
                location = '001 Schroeder Run, New Tabithaport, Colombia',
                sex = 0,
                birthday = docspace-api-sdk.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
                worksfrom = docspace-api-sdk.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
                comment = 'some text',
                contacts = [
                    docspace-api-sdk.models.contact.Contact(
                        type = 'GTalk', 
                        value = 'my@gmail.com', )
                    ],
                files = 'some text',
                from_invite_link = True,
                key = 'some text',
                culture_name = 'some text',
                target = '75a5f745-f697-4418-b38d-0fe0d277e258',
                spam = True
            )
        else:
            return MemberRequestDto(
        )
        """

    def testMemberRequestDto(self):
        """Test MemberRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
