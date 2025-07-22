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

from docspace-api-sdk.api.settings_notifications_api import SettingsNotificationsApi


class TestSettingsNotificationsApi(unittest.TestCase):
    """SettingsNotificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsNotificationsApi()

    def tearDown(self) -> None:
        pass

    def test_get_notification_settings(self) -> None:
        """Test case for get_notification_settings

        Check notification availability
        """
        pass

    def test_get_rooms_notification_settings(self) -> None:
        """Test case for get_rooms_notification_settings

        Get room notification settings
        """
        pass

    def test_set_notification_settings(self) -> None:
        """Test case for set_notification_settings

        Enable notifications
        """
        pass

    def test_set_rooms_notification_status(self) -> None:
        """Test case for set_rooms_notification_status

        Set room notification status
        """
        pass


if __name__ == '__main__':
    unittest.main()
