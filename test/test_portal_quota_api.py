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

from docspace-api-sdk.api.portal_quota_api import PortalQuotaApi


class TestPortalQuotaApi(unittest.TestCase):
    """PortalQuotaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalQuotaApi()

    def tearDown(self) -> None:
        pass

    def test_get_portal_quota(self) -> None:
        """Test case for get_portal_quota

        Get a portal quota
        """
        pass

    def test_get_portal_tariff(self) -> None:
        """Test case for get_portal_tariff

        Get a portal tariff
        """
        pass

    def test_get_portal_used_space(self) -> None:
        """Test case for get_portal_used_space

        Get the portal used space
        """
        pass

    def test_get_right_quota(self) -> None:
        """Test case for get_right_quota

        Get the recommended quota
        """
        pass


if __name__ == '__main__':
    unittest.main()
