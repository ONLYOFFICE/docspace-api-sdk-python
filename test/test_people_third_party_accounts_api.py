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

from docspace-api-python.api.people_third_party_accounts_api import PeopleThirdPartyAccountsApi


class TestPeopleThirdPartyAccountsApi(unittest.TestCase):
    """PeopleThirdPartyAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleThirdPartyAccountsApi()

    def tearDown(self) -> None:
        pass

    def test_get_third_party_auth_providers(self) -> None:
        """Test case for get_third_party_auth_providers

        Get third-party accounts
        """
        pass

    def test_link_third_party_account(self) -> None:
        """Test case for link_third_party_account

        Link a third-pary account
        """
        pass

    def test_signup_third_party_account(self) -> None:
        """Test case for signup_third_party_account

        Create a third-pary account
        """
        pass

    def test_unlink_third_party_account(self) -> None:
        """Test case for unlink_third_party_account

        Unlink a third-pary account
        """
        pass


if __name__ == '__main__':
    unittest.main()
