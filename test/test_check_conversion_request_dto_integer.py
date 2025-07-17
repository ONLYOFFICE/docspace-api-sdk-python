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

from docspace-api-python.models.check_conversion_request_dto_integer import CheckConversionRequestDtoInteger

class TestCheckConversionRequestDtoInteger(unittest.TestCase):
    """CheckConversionRequestDtoInteger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckConversionRequestDtoInteger:
        """Test CheckConversionRequestDtoInteger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckConversionRequestDtoInteger`
        """
        model = CheckConversionRequestDtoInteger()
        if include_optional:
            return CheckConversionRequestDtoInteger(
                file_id = 9846,
                sync = True,
                start_convert = True,
                version = 1234,
                password = 'vfmf2vO1Kp',
                output_type = 'some text',
                create_new_if_exist = True
            )
        else:
            return CheckConversionRequestDtoInteger(
        )
        """

    def testCheckConversionRequestDtoInteger(self):
        """Test CheckConversionRequestDtoInteger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
