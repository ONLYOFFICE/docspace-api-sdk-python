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

from docspace-api-sdk.api.portal_settings_api import PortalSettingsApi


class TestPortalSettingsApi(unittest.TestCase):
    """PortalSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_continue_portal(self) -> None:
        """Test case for continue_portal

        Restore a portal
        """
        pass

    def test_delete_portal(self) -> None:
        """Test case for delete_portal

        Delete a portal
        """
        pass

    def test_get_portal_information(self) -> None:
        """Test case for get_portal_information

        Get a portal
        """
        pass

    def test_get_portal_path(self) -> None:
        """Test case for get_portal_path

        Get a path to the portal
        """
        pass

    def test_send_delete_instructions(self) -> None:
        """Test case for send_delete_instructions

        Send removal instructions
        """
        pass

    def test_send_suspend_instructions(self) -> None:
        """Test case for send_suspend_instructions

        Send suspension instructions
        """
        pass

    def test_suspend_portal(self) -> None:
        """Test case for suspend_portal

        Deactivate a portal
        """
        pass


if __name__ == '__main__':
    unittest.main()
