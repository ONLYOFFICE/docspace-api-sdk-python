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

from docspace-api-sdk.api.security_active_connections_api import SecurityActiveConnectionsApi


class TestSecurityActiveConnectionsApi(unittest.TestCase):
    """SecurityActiveConnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityActiveConnectionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_active_connections(self) -> None:
        """Test case for get_all_active_connections

        Get active connections
        """
        pass

    def test_log_out_active_connection(self) -> None:
        """Test case for log_out_active_connection

        Log out from the connection
        """
        pass

    def test_log_out_all_active_connections_change_password(self) -> None:
        """Test case for log_out_all_active_connections_change_password

        Log out and change password
        """
        pass

    def test_log_out_all_active_connections_for_user(self) -> None:
        """Test case for log_out_all_active_connections_for_user

        Log out for the user by ID
        """
        pass

    def test_log_out_all_except_this_connection(self) -> None:
        """Test case for log_out_all_except_this_connection

        Log out from all connections except the current one
        """
        pass


if __name__ == '__main__':
    unittest.main()
