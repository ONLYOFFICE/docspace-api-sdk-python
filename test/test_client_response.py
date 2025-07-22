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

from docspace-api-sdk.models.client_response import ClientResponse

class TestClientResponse(unittest.TestCase):
    """ClientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientResponse:
        """Test ClientResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientResponse`
        """
        model = ClientResponse()
        if include_optional:
            return ClientResponse(
                name = '',
                description = '',
                tenant = 56,
                scopes = [
                    ''
                    ],
                enabled = True,
                client_id = '',
                client_secret = '',
                website_url = '',
                terms_url = '',
                policy_url = '',
                logo = '',
                authentication_methods = [
                    ''
                    ],
                redirect_uris = [
                    ''
                    ],
                allowed_origins = [
                    ''
                    ],
                logout_redirect_uris = [
                    ''
                    ],
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                modified_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_by = '',
                is_public = True
            )
        else:
            return ClientResponse(
        )
        """

    def testClientResponse(self):
        """Test ClientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
