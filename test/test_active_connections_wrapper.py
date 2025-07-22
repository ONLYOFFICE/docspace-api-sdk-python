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

from docspace-api-sdk.models.active_connections_wrapper import ActiveConnectionsWrapper

class TestActiveConnectionsWrapper(unittest.TestCase):
    """ActiveConnectionsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActiveConnectionsWrapper:
        """Test ActiveConnectionsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActiveConnectionsWrapper`
        """
        model = ActiveConnectionsWrapper()
        if include_optional:
            return ActiveConnectionsWrapper(
                response = docspace-api-sdk.models.active_connections_dto.ActiveConnectionsDto(
                    login_event = 1234, 
                    items = [
                        docspace-api-sdk.models.active_connections_item_dto.ActiveConnectionsItemDto(
                            id = 9846, 
                            tenant_id = 1234, 
                            user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28', 
                            mobile = True, 
                            ip = 'some text', 
                            country = 'some text', 
                            city = 'some text', 
                            browser = 'some text', 
                            platform = 'some text', 
                            date = docspace-api-sdk.models.api_date_time.ApiDateTime(
                                utc_time = '2008-04-10T06:30+04:00', 
                                time_zone_offset = '00:00:00', ), 
                            page = 'some text', )
                        ], ),
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
            return ActiveConnectionsWrapper(
        )
        """

    def testActiveConnectionsWrapper(self):
        """Test ActiveConnectionsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
