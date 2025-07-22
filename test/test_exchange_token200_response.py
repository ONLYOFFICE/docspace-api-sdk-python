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

from docspace-api-sdk.models.exchange_token200_response import ExchangeToken200Response

class TestExchangeToken200Response(unittest.TestCase):
    """ExchangeToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeToken200Response:
        """Test ExchangeToken200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeToken200Response`
        """
        model = ExchangeToken200Response()
        if include_optional:
            return ExchangeToken200Response(
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
                token_type = 'Bearer',
                expires_in = 3600,
                refresh_token = 'def502...'
            )
        else:
            return ExchangeToken200Response(
        )
        """

    def testExchangeToken200Response(self):
        """Test ExchangeToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
