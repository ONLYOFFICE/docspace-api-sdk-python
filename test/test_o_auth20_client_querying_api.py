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

from docspace-api-python.api.o_auth20_client_querying_api import OAuth20ClientQueryingApi


class TestOAuth20ClientQueryingApi(unittest.TestCase):
    """OAuth20ClientQueryingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuth20ClientQueryingApi()

    def tearDown(self) -> None:
        pass

    def test_get_client(self) -> None:
        """Test case for get_client

        Get client details
        """
        pass

    def test_get_client_info(self) -> None:
        """Test case for get_client_info

        Get detailed client information
        """
        pass

    def test_get_clients(self) -> None:
        """Test case for get_clients

        Get clients
        """
        pass

    def test_get_clients_info(self) -> None:
        """Test case for get_clients_info

        Get detailed information of clients
        """
        pass

    def test_get_consents(self) -> None:
        """Test case for get_consents

        Get user consents
        """
        pass

    def test_get_public_client_info(self) -> None:
        """Test case for get_public_client_info

        Get public client information
        """
        pass


if __name__ == '__main__':
    unittest.main()
