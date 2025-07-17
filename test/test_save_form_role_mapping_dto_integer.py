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

from docspace-api-python.models.save_form_role_mapping_dto_integer import SaveFormRoleMappingDtoInteger

class TestSaveFormRoleMappingDtoInteger(unittest.TestCase):
    """SaveFormRoleMappingDtoInteger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SaveFormRoleMappingDtoInteger:
        """Test SaveFormRoleMappingDtoInteger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SaveFormRoleMappingDtoInteger`
        """
        model = SaveFormRoleMappingDtoInteger()
        if include_optional:
            return SaveFormRoleMappingDtoInteger(
                form_id = 1234,
                roles = [
                    docspace-api-python.models.form_role.FormRole(
                        room_id = 9846, 
                        role_name = 'some text', 
                        role_color = 'some text', 
                        user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28', 
                        sequence = 1234, 
                        submitted = True, 
                        opened_at = '2008-04-10T06:30+04:00', 
                        submission_date = '2008-04-10T06:30+04:00', )
                    ]
            )
        else:
            return SaveFormRoleMappingDtoInteger(
        )
        """

    def testSaveFormRoleMappingDtoInteger(self):
        """Test SaveFormRoleMappingDtoInteger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
