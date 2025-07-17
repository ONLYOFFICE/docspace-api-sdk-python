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

from docspace-api-python.api.settings_owner_api import SettingsOwnerApi


class TestSettingsOwnerApi(unittest.TestCase):
    """SettingsOwnerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsOwnerApi()

    def tearDown(self) -> None:
        pass

    def test_send_owner_change_instructions(self) -> None:
        """Test case for send_owner_change_instructions

        Send the owner change instructions
        """
        pass

    def test_update_portal_owner(self) -> None:
        """Test case for update_portal_owner

        Update the portal owner
        """
        pass


if __name__ == '__main__':
    unittest.main()
