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

from docspace-api-python.api.settings_login_settings_api import SettingsLoginSettingsApi


class TestSettingsLoginSettingsApi(unittest.TestCase):
    """SettingsLoginSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsLoginSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_login_settings(self) -> None:
        """Test case for get_login_settings

        Get the login settings
        """
        pass

    def test_set_default_login_settings(self) -> None:
        """Test case for set_default_login_settings

        Reset the login settings
        """
        pass

    def test_update_login_settings(self) -> None:
        """Test case for update_login_settings

        Update the login settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
