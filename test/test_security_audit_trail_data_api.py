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

from docspace-api-python.api.security_audit_trail_data_api import SecurityAuditTrailDataApi


class TestSecurityAuditTrailDataApi(unittest.TestCase):
    """SecurityAuditTrailDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityAuditTrailDataApi()

    def tearDown(self) -> None:
        pass

    def test_create_audit_trail_report(self) -> None:
        """Test case for create_audit_trail_report

        Generate the audit trail report
        """
        pass

    def test_get_audit_events_by_filter(self) -> None:
        """Test case for get_audit_events_by_filter

        Get filtered audit trail data
        """
        pass

    def test_get_audit_settings(self) -> None:
        """Test case for get_audit_settings

        Get the audit trail settings
        """
        pass

    def test_get_audit_trail_mappers(self) -> None:
        """Test case for get_audit_trail_mappers

        Get audit trail mappers
        """
        pass

    def test_get_audit_trail_types(self) -> None:
        """Test case for get_audit_trail_types

        Get audit trail types
        """
        pass

    def test_get_last_audit_events(self) -> None:
        """Test case for get_last_audit_events

        Get audit trail data
        """
        pass

    def test_set_audit_settings(self) -> None:
        """Test case for set_audit_settings

        Set the audit trail settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
