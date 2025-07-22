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

from docspace-api-sdk.api.settings_webhooks_api import SettingsWebhooksApi


class TestSettingsWebhooksApi(unittest.TestCase):
    """SettingsWebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsWebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_create_webhook(self) -> None:
        """Test case for create_webhook

        Create a webhook
        """
        pass

    def test_enable_webhook(self) -> None:
        """Test case for enable_webhook

        Enable a webhook
        """
        pass

    def test_get_tenant_webhooks(self) -> None:
        """Test case for get_tenant_webhooks

        Get webhooks
        """
        pass

    def test_get_webhook_triggers(self) -> None:
        """Test case for get_webhook_triggers

        Get webhook triggers
        """
        pass

    def test_get_webhooks_logs(self) -> None:
        """Test case for get_webhooks_logs

        Get webhook logs
        """
        pass

    def test_remove_webhook(self) -> None:
        """Test case for remove_webhook

        Remove a webhook
        """
        pass

    def test_retry_webhook(self) -> None:
        """Test case for retry_webhook

        Retry a webhook
        """
        pass

    def test_retry_webhooks(self) -> None:
        """Test case for retry_webhooks

        Retry webhooks
        """
        pass

    def test_update_webhook(self) -> None:
        """Test case for update_webhook

        Update a webhook
        """
        pass


if __name__ == '__main__':
    unittest.main()
