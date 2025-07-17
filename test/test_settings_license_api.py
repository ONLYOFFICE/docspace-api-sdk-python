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

from docspace-api-python.api.settings_license_api import SettingsLicenseApi


class TestSettingsLicenseApi(unittest.TestCase):
    """SettingsLicenseApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsLicenseApi()

    def tearDown(self) -> None:
        pass

    def test_accept_license(self) -> None:
        """Test case for accept_license

        Activate a license
        """
        pass

    def test_get_is_license_required(self) -> None:
        """Test case for get_is_license_required

        Request a license
        """
        pass

    def test_refresh_license(self) -> None:
        """Test case for refresh_license

        Refresh the license
        """
        pass

    def test_upload_license(self) -> None:
        """Test case for upload_license

        Upload a license
        """
        pass


if __name__ == '__main__':
    unittest.main()
