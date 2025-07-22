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

from docspace-api-sdk.api.settings_authorization_api import SettingsAuthorizationApi


class TestSettingsAuthorizationApi(unittest.TestCase):
    """SettingsAuthorizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsAuthorizationApi()

    def tearDown(self) -> None:
        pass

    def test_get_auth_services(self) -> None:
        """Test case for get_auth_services

        Get the authorization services
        """
        pass

    def test_save_auth_keys(self) -> None:
        """Test case for save_auth_keys

        Save the authorization keys
        """
        pass


if __name__ == '__main__':
    unittest.main()
