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

from docspace-api-python.models.check_doc_service_url_request_dto import CheckDocServiceUrlRequestDto

class TestCheckDocServiceUrlRequestDto(unittest.TestCase):
    """CheckDocServiceUrlRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckDocServiceUrlRequestDto:
        """Test CheckDocServiceUrlRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckDocServiceUrlRequestDto`
        """
        model = CheckDocServiceUrlRequestDto()
        if include_optional:
            return CheckDocServiceUrlRequestDto(
                doc_service_url = 'some text',
                doc_service_url_internal = 'some text',
                doc_service_url_portal = 'some text',
                doc_service_signature_secret = 'some text',
                doc_service_signature_header = 'some text',
                doc_service_ssl_verification = True
            )
        else:
            return CheckDocServiceUrlRequestDto(
        )
        """

    def testCheckDocServiceUrlRequestDto(self):
        """Test CheckDocServiceUrlRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
