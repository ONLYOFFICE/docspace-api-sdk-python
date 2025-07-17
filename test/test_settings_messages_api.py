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

from docspace-api-python.api.settings_messages_api import SettingsMessagesApi


class TestSettingsMessagesApi(unittest.TestCase):
    """SettingsMessagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsMessagesApi()

    def tearDown(self) -> None:
        pass

    def test_enable_admin_message_settings(self) -> None:
        """Test case for enable_admin_message_settings

        Enable the administrator message settings
        """
        pass

    def test_send_admin_mail(self) -> None:
        """Test case for send_admin_mail

        Send a message to the administrator
        """
        pass

    def test_send_join_invite_mail(self) -> None:
        """Test case for send_join_invite_mail

        Sends an invitation email
        """
        pass


if __name__ == '__main__':
    unittest.main()
