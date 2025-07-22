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

from docspace-api-sdk.api.o_auth20_scope_management_api import OAuth20ScopeManagementApi


class TestOAuth20ScopeManagementApi(unittest.TestCase):
    """OAuth20ScopeManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuth20ScopeManagementApi()

    def tearDown(self) -> None:
        pass

    def test_get_scopes(self) -> None:
        """Test case for get_scopes

        Get available OAuth2 scopes
        """
        pass


if __name__ == '__main__':
    unittest.main()
