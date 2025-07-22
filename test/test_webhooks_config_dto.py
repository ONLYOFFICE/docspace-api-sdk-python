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

from docspace-api-sdk.models.webhooks_config_dto import WebhooksConfigDto

class TestWebhooksConfigDto(unittest.TestCase):
    """WebhooksConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksConfigDto:
        """Test WebhooksConfigDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksConfigDto`
        """
        model = WebhooksConfigDto()
        if include_optional:
            return WebhooksConfigDto(
                id = 9846,
                name = 'Winfield Upton',
                uri = 'some text',
                enabled = True,
                ssl = True,
                triggers = 0,
                target_id = 'some text',
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
                created_on = '2008-04-10T06:30+04:00',
                modified_by = docspace-api-sdk.models.employee_dto.EmployeeDto(
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
                modified_on = '2008-04-10T06:30+04:00',
                last_failure_on = '2008-04-10T06:30+04:00',
                last_failure_content = 'some text',
                last_success_on = '2008-04-10T06:30+04:00'
            )
        else:
            return WebhooksConfigDto(
        )
        """

    def testWebhooksConfigDto(self):
        """Test WebhooksConfigDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
