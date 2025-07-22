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

from docspace-api-sdk.api.o_auth20_authorization_api import OAuth20AuthorizationApi


class TestOAuth20AuthorizationApi(unittest.TestCase):
    """OAuth20AuthorizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuth20AuthorizationApi()

    def tearDown(self) -> None:
        pass

    def test_authorize_o_auth(self) -> None:
        """Test case for authorize_o_auth

        OAuth2 authorization endpoint
        """
        pass

    def test_exchange_token(self) -> None:
        """Test case for exchange_token

        OAuth2 token endpoint
        """
        pass

    def test_submit_consent(self) -> None:
        """Test case for submit_consent

        OAuth2 consent endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
