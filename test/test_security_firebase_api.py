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

from docspace-api-sdk.api.security_firebase_api import SecurityFirebaseApi


class TestSecurityFirebaseApi(unittest.TestCase):
    """SecurityFirebaseApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityFirebaseApi()

    def tearDown(self) -> None:
        pass

    def test_doc_register_pusn_notification_device(self) -> None:
        """Test case for doc_register_pusn_notification_device

        Save the Documents Firebase device token
        """
        pass

    def test_subscribe_documents_push_notification(self) -> None:
        """Test case for subscribe_documents_push_notification

        Subscribe to Documents push notification
        """
        pass


if __name__ == '__main__':
    unittest.main()
