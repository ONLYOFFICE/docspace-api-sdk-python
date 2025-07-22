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

from docspace-api-sdk.models.tenant_wrapper import TenantWrapper

class TestTenantWrapper(unittest.TestCase):
    """TenantWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantWrapper:
        """Test TenantWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantWrapper`
        """
        model = TenantWrapper()
        if include_optional:
            return TenantWrapper(
                response = docspace-api-sdk.models.tenant_dto.TenantDto(
                    affiliate_id = 'some text', 
                    tenant_alias = 'some text', 
                    calls = True, 
                    campaign = 'some text', 
                    creation_date_time = '2008-04-10T06:30+04:00', 
                    hosted_region = 'some text', 
                    tenant_id = 1234, 
                    industry = 0, 
                    language = 'some text', 
                    last_modified = '2008-04-10T06:30+04:00', 
                    mapped_domain = 'some text', 
                    name = 'Winfield Upton', 
                    owner_id = '75a5f745-f697-4418-b38d-0fe0d277e258', 
                    payment_id = 'some text', 
                    spam = True, 
                    status = 0, 
                    status_change_date = '2008-04-10T06:30+04:00', 
                    time_zone = 'some text', 
                    trusted_domains = ["some text"], 
                    trusted_domains_raw = 'some text', 
                    trusted_domains_type = 0, 
                    version = 1234, 
                    version_changed = '2008-04-10T06:30+04:00', 
                    region = 'some text', ),
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
            return TenantWrapper(
        )
        """

    def testTenantWrapper(self):
        """Test TenantWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
