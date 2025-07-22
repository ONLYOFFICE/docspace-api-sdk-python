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

from docspace-api-sdk.models.audit_event_dto import AuditEventDto

class TestAuditEventDto(unittest.TestCase):
    """AuditEventDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuditEventDto:
        """Test AuditEventDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuditEventDto`
        """
        model = AuditEventDto()
        if include_optional:
            return AuditEventDto(
                id = 9846,
                var_date = docspace-api-sdk.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
                user = 'some text',
                user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28',
                action = 'some text',
                action_id = 1000,
                ip = 'some text',
                country = 'some text',
                city = 'some text',
                browser = 'some text',
                platform = 'some text',
                page = 'some text',
                action_type = 0,
                product = 0,
                module = 0,
                target = ["some text"],
                entries = [
                    0
                    ],
                context = 'some text'
            )
        else:
            return AuditEventDto(
        )
        """

    def testAuditEventDto(self):
        """Test AuditEventDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
