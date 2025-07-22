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

from docspace-api-sdk.models.group_dto import GroupDto

class TestGroupDto(unittest.TestCase):
    """GroupDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupDto:
        """Test GroupDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupDto`
        """
        model = GroupDto()
        if include_optional:
            return GroupDto(
                name = 'Winfield Upton',
                parent = '75a5f745-f697-4418-b38d-0fe0d277e258',
                category = '75a5f745-f697-4418-b38d-0fe0d277e258',
                id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28',
                is_ldap = True,
                manager = docspace-api-sdk.models.employee_full_dto.EmployeeFullDto(
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
                    is_anonim = True, 
                    first_name = 'Mike', 
                    last_name = 'Zanyatski', 
                    user_name = 'Mike.Zanyatski', 
                    email = 'my@gmail.com', 
                    contacts = [
                        docspace-api-sdk.models.contact.Contact(
                            type = 'GTalk', 
                            value = 'my@gmail.com', )
                        ], 
                    birthday = docspace-api-sdk.models.api_date_time.ApiDateTime(
                        utc_time = '2008-04-10T06:30+04:00', 
                        time_zone_offset = '00:00:00', ), 
                    sex = 'male', 
                    status = 1, 
                    activation_status = 0, 
                    terminated = docspace-api-sdk.models.api_date_time.ApiDateTime(
                        utc_time = '2008-04-10T06:30+04:00', 
                        time_zone_offset = '00:00:00', ), 
                    department = 'Marketing', 
                    work_from = , 
                    groups = [
                        docspace-api-sdk.models.group_summary_dto.GroupSummaryDto(
                            id = '', 
                            name = 'Group Name', )
                        ], 
                    location = 'Palo Alto', 
                    notes = 'Notes to worker', 
                    is_admin = False, 
                    is_room_admin = True, 
                    is_ldap = False, 
                    list_admin_modules = ["projects", "crm"], 
                    is_owner = True, 
                    is_visitor = True, 
                    is_collaborator = True, 
                    culture_name = 'en-EN', 
                    mobile_phone = 'some text', 
                    mobile_phone_activation_status = 0, 
                    is_sso = False, 
                    theme = 0, 
                    quota_limit = 1234, 
                    used_space = 12345, 
                    shared = True, 
                    is_custom_quota = True, 
                    login_event_id = 1234, 
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
                    registration_date = , 
                    has_personal_folder = True, 
                    tfa_app_enabled = True, ),
                members = [
                    docspace-api-sdk.models.employee_full_dto.EmployeeFullDto(
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
                        is_anonim = True, 
                        first_name = 'Mike', 
                        last_name = 'Zanyatski', 
                        user_name = 'Mike.Zanyatski', 
                        email = 'my@gmail.com', 
                        contacts = [
                            docspace-api-sdk.models.contact.Contact(
                                type = 'GTalk', 
                                value = 'my@gmail.com', )
                            ], 
                        birthday = docspace-api-sdk.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        sex = 'male', 
                        status = 1, 
                        activation_status = 0, 
                        terminated = docspace-api-sdk.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        department = 'Marketing', 
                        work_from = , 
                        groups = [
                            docspace-api-sdk.models.group_summary_dto.GroupSummaryDto(
                                id = '', 
                                name = 'Group Name', 
                                manager = 'Jake.Zazhitski', )
                            ], 
                        location = 'Palo Alto', 
                        notes = 'Notes to worker', 
                        is_admin = False, 
                        is_room_admin = True, 
                        is_ldap = False, 
                        list_admin_modules = ["projects", "crm"], 
                        is_owner = True, 
                        is_visitor = True, 
                        is_collaborator = True, 
                        culture_name = 'en-EN', 
                        mobile_phone = 'some text', 
                        mobile_phone_activation_status = 0, 
                        is_sso = False, 
                        theme = 0, 
                        quota_limit = 1234, 
                        used_space = 12345, 
                        shared = True, 
                        is_custom_quota = True, 
                        login_event_id = 1234, 
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
                        registration_date = , 
                        has_personal_folder = True, 
                        tfa_app_enabled = True, )
                    ],
                shared = True,
                members_count = 1234
            )
        else:
            return GroupDto(
        )
        """

    def testGroupDto(self):
        """Test GroupDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
