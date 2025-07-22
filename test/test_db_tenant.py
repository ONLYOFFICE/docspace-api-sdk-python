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

from docspace-api-sdk.models.db_tenant import DbTenant

class TestDbTenant(unittest.TestCase):
    """DbTenant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DbTenant:
        """Test DbTenant
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DbTenant`
        """
        model = DbTenant()
        if include_optional:
            return DbTenant(
                id = 9846,
                name = 'Winfield Upton',
                alias = 'some text',
                mapped_domain = 'some text',
                version = 1234,
                version_changed = '2008-04-10T06:30+04:00',
                version_changed = '2008-04-10T06:30+04:00',
                language = 'some text',
                time_zone = 'some text',
                trusted_domains_raw = 'some text',
                trusted_domains_enabled = 0,
                status = 0,
                status_changed = '2008-04-10T06:30+04:00',
                status_changed_hack = '2008-04-10T06:30+04:00',
                creation_date_time = '2008-04-10T06:30+04:00',
                owner_id = '75a5f745-f697-4418-b38d-0fe0d277e258',
                payment_id = 'some text',
                industry = 0,
                last_modified = '2008-04-10T06:30+04:00',
                calls = True,
                partner = docspace-api-sdk.models.db_tenant_partner.DbTenantPartner(
                    tenant_id = 1234, 
                    partner_id = 'some text', 
                    affiliate_id = 'some text', 
                    campaign = 'some text', )
            )
        else:
            return DbTenant(
        )
        """

    def testDbTenant(self):
        """Test DbTenant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
