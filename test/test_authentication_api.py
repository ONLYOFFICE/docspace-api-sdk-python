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

from docspace-api-sdk.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_authenticate_me(self) -> None:
        """Test case for authenticate_me

        Authenticate a user
        """
        pass

    def test_authenticate_me_from_body_with_code(self) -> None:
        """Test case for authenticate_me_from_body_with_code

        Authenticate a user by code
        """
        pass

    def test_check_confirm(self) -> None:
        """Test case for check_confirm

        Open confirmation email URL
        """
        pass

    def test_get_is_authentificated(self) -> None:
        """Test case for get_is_authentificated

        Check authentication
        """
        pass

    def test_logout(self) -> None:
        """Test case for logout

        Log out
        """
        pass

    def test_save_mobile_phone(self) -> None:
        """Test case for save_mobile_phone

        Set a mobile phone
        """
        pass

    def test_send_sms_code(self) -> None:
        """Test case for send_sms_code

        Send SMS code
        """
        pass


if __name__ == '__main__':
    unittest.main()
