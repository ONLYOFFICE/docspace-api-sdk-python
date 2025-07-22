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

from docspace-api-sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper

class TestMentionWrapperArrayWrapper(unittest.TestCase):
    """MentionWrapperArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentionWrapperArrayWrapper:
        """Test MentionWrapperArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentionWrapperArrayWrapper`
        """
        model = MentionWrapperArrayWrapper()
        if include_optional:
            return MentionWrapperArrayWrapper(
                response = [
                    docspace-api-sdk.models.mention_wrapper.MentionWrapper(
                        user = docspace-api-sdk.models.user_info.UserInfo(
                            id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28', 
                            first_name = 'Winfield', 
                            last_name = 'Wyman', 
                            user_name = 'some text', 
                            birth_date = '2008-04-10T06:30+04:00', 
                            sex = True, 
                            status = 1, 
                            activation_status = 0, 
                            terminated_date = '2008-04-10T06:30+04:00', 
                            title = 'legacy_1080p_small_wooden_mouse', 
                            work_from_date = '2008-04-10T06:30+04:00', 
                            email = 'Sydney_Roberts4@hotmail.com', 
                            contacts = 'some text', 
                            contacts_list = ["some text"], 
                            location = '001 Schroeder Run, New Tabithaport, Colombia', 
                            notes = 'some text', 
                            removed = True, 
                            last_modified = '2008-04-10T06:30+04:00', 
                            tenant_id = 1234, 
                            is_active = True, 
                            culture_name = 'some text', 
                            mobile_phone = 'some text', 
                            mobile_phone_activation_status = 0, 
                            sid = 'some text', 
                            ldap_qouta = 1234, 
                            sso_name_id = 'some text', 
                            sso_session_id = 'some text', 
                            create_date = '2008-04-10T06:30+04:00', 
                            created_by = '75a5f745-f697-4418-b38d-0fe0d277e258', 
                            spam = True, 
                            check_activation = True, ), 
                        email = 'Sydney_Roberts4@hotmail.com', 
                        id = '9846', 
                        image = 'some text', 
                        has_access = True, 
                        name = 'Winfield Upton', )
                    ],
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
            return MentionWrapperArrayWrapper(
        )
        """

    def testMentionWrapperArrayWrapper(self):
        """Test MentionWrapperArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
