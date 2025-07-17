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

from docspace-api-python.models.create_client_request import CreateClientRequest

class TestCreateClientRequest(unittest.TestCase):
    """CreateClientRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateClientRequest:
        """Test CreateClientRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateClientRequest`
        """
        model = CreateClientRequest()
        if include_optional:
            return CreateClientRequest(
                name = 'Example Client',
                description = 'Description of the client',
                logo = 'data:image/png;base64,...',
                scopes = ["read","write"],
                allow_pkce = True,
                is_public = False,
                website_url = 'http://example.com',
                terms_url = 'http://example.com/terms',
                policy_url = 'http://example.com/policy',
                redirect_uris = ["http://example.com/redirect"],
                allowed_origins = ["http://example.com"],
                logout_redirect_uri = 'http://example.com/logout'
            )
        else:
            return CreateClientRequest(
                redirect_uris = ["http://example.com/redirect"],
                allowed_origins = ["http://example.com"],
        )
        """

    def testCreateClientRequest(self):
        """Test CreateClientRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
