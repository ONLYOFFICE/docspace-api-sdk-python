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

from docspace-api-sdk.models.tenant_quota_wrapper import TenantQuotaWrapper

class TestTenantQuotaWrapper(unittest.TestCase):
    """TenantQuotaWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantQuotaWrapper:
        """Test TenantQuotaWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantQuotaWrapper`
        """
        model = TenantQuotaWrapper()
        if include_optional:
            return TenantQuotaWrapper(
                response = docspace-api-sdk.models.tenant_quota.TenantQuota(
                    tenant_id = 1234, 
                    name = 'Default', 
                    price = 10, 
                    price_currency_symbol = 'some text', 
                    product_id = '9846', 
                    visible = True, 
                    features = 'some text', 
                    max_file_size = 26214400, 
                    max_total_size = 56, 
                    count_user = 1234, 
                    count_room_admin = 1234, 
                    users_in_room = 1234, 
                    count_room = 1234, 
                    non_profit = True, 
                    trial = True, 
                    free = True, 
                    update = True, 
                    audit = True, 
                    docs_edition = True, 
                    ldap = True, 
                    sso = True, 
                    statistic = True, 
                    branding = True, 
                    customization = True, 
                    lifetime = True, 
                    custom = True, 
                    auto_backup_restore = True, 
                    oauth = True, 
                    content_search = True, 
                    third_party = True, 
                    year = True, ),
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
            return TenantQuotaWrapper(
        )
        """

    def testTenantQuotaWrapper(self):
        """Test TenantQuotaWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
