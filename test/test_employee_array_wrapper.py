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

from docspace-api-python.models.employee_array_wrapper import EmployeeArrayWrapper

class TestEmployeeArrayWrapper(unittest.TestCase):
    """EmployeeArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeArrayWrapper:
        """Test EmployeeArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmployeeArrayWrapper`
        """
        model = EmployeeArrayWrapper()
        if include_optional:
            return EmployeeArrayWrapper(
                response = [
                    docspace-api-python.models.employee_dto.EmployeeDto(
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
                        is_anonim = True, )
                    ],
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
            return EmployeeArrayWrapper(
        )
        """

    def testEmployeeArrayWrapper(self):
        """Test EmployeeArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
