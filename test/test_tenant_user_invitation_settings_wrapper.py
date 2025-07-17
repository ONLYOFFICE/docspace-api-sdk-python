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

from docspace-api-python.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper

class TestTenantUserInvitationSettingsWrapper(unittest.TestCase):
    """TenantUserInvitationSettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantUserInvitationSettingsWrapper:
        """Test TenantUserInvitationSettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantUserInvitationSettingsWrapper`
        """
        model = TenantUserInvitationSettingsWrapper()
        if include_optional:
            return TenantUserInvitationSettingsWrapper(
                response = docspace-api-python.models.tenant_user_invitation_settings_dto.TenantUserInvitationSettingsDto(
                    allow_inviting_members = True, 
                    allow_inviting_guests = True, ),
                count = 56,
                links = [
                    docspace-api-python.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return TenantUserInvitationSettingsWrapper(
        )
        """

    def testTenantUserInvitationSettingsWrapper(self):
        """Test TenantUserInvitationSettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
