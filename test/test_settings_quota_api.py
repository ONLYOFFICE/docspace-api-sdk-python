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

from docspace-api-python.api.settings_quota_api import SettingsQuotaApi


class TestSettingsQuotaApi(unittest.TestCase):
    """SettingsQuotaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsQuotaApi()

    def tearDown(self) -> None:
        pass

    def test_get_user_quota_settings(self) -> None:
        """Test case for get_user_quota_settings

        Get the user quota settings
        """
        pass

    def test_save_room_quota_settings(self) -> None:
        """Test case for save_room_quota_settings

        Save the room quota settings
        """
        pass

    def test_set_tenant_quota_settings(self) -> None:
        """Test case for set_tenant_quota_settings

        Save the tenant quota settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
