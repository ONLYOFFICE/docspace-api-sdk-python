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

from docspace-api-sdk.models.third_party_params_array_wrapper import ThirdPartyParamsArrayWrapper

class TestThirdPartyParamsArrayWrapper(unittest.TestCase):
    """ThirdPartyParamsArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ThirdPartyParamsArrayWrapper:
        """Test ThirdPartyParamsArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThirdPartyParamsArrayWrapper`
        """
        model = ThirdPartyParamsArrayWrapper()
        if include_optional:
            return ThirdPartyParamsArrayWrapper(
                response = [
                    docspace-api-sdk.models.third_party_params.ThirdPartyParams(
                        auth_data = docspace-api-sdk.models.auth_data.AuthData(
                            login = 'some text', 
                            password = 'vfmf2vO1Kp', 
                            raw_token = 'some text', 
                            url = 'some text', 
                            provider = 'some text', 
                            token = docspace-api-sdk.models.o_auth20_token.OAuth20Token(
                                access_token = 'some text', 
                                refresh_token = 'some text', 
                                expires_in = 1234, 
                                client_id = 'some text', 
                                client_secret = 'some text', 
                                redirect_uri = 'some text', 
                                timestamp = '2008-04-10T06:30+04:00', 
                                is_expired = True, ), ), 
                        corporate = True, 
                        rooms_storage = True, 
                        customer_title = 'some text', 
                        provider_id = 1234, 
                        provider_key = 'some text', )
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
            return ThirdPartyParamsArrayWrapper(
        )
        """

    def testThirdPartyParamsArrayWrapper(self):
        """Test ThirdPartyParamsArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
