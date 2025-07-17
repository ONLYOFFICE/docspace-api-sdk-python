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

from docspace-api-python.api.settings_greeting_settings_api import SettingsGreetingSettingsApi


class TestSettingsGreetingSettingsApi(unittest.TestCase):
    """SettingsGreetingSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsGreetingSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_greeting_settings(self) -> None:
        """Test case for get_greeting_settings

        Get greeting settings
        """
        pass

    def test_get_is_default_greeting_settings(self) -> None:
        """Test case for get_is_default_greeting_settings

        Check the default greeting settings
        """
        pass

    def test_restore_greeting_settings(self) -> None:
        """Test case for restore_greeting_settings

        Restore the greeting settings
        """
        pass

    def test_save_greeting_settings(self) -> None:
        """Test case for save_greeting_settings

        Save the greeting settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
