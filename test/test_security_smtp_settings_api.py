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

from docspace-api-python.api.security_smtp_settings_api import SecuritySMTPSettingsApi


class TestSecuritySMTPSettingsApi(unittest.TestCase):
    """SecuritySMTPSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecuritySMTPSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_smtp_operation_status(self) -> None:
        """Test case for get_smtp_operation_status

        Get the SMTP testing process status
        """
        pass

    def test_get_smtp_settings(self) -> None:
        """Test case for get_smtp_settings

        Get the SMTP settings
        """
        pass

    def test_reset_smtp_settings(self) -> None:
        """Test case for reset_smtp_settings

        Reset the SMTP settings
        """
        pass

    def test_save_smtp_settings(self) -> None:
        """Test case for save_smtp_settings

        Save the SMTP settings
        """
        pass

    def test_test_smtp_settings(self) -> None:
        """Test case for test_smtp_settings

        Test the SMTP settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
