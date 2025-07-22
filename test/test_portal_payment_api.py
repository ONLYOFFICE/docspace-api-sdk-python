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

from docspace-api-sdk.api.portal_payment_api import PortalPaymentApi


class TestPortalPaymentApi(unittest.TestCase):
    """PortalPaymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalPaymentApi()

    def tearDown(self) -> None:
        pass

    def test_calculate_wallet_payment(self) -> None:
        """Test case for calculate_wallet_payment

        Calculate amount of the wallet payment
        """
        pass

    def test_create_customer_operations_report(self) -> None:
        """Test case for create_customer_operations_report

        Generate the customer operations report
        """
        pass

    def test_get_checkout_setup_url(self) -> None:
        """Test case for get_checkout_setup_url

        Get the checkout setup page URL
        """
        pass

    def test_get_customer_balance(self) -> None:
        """Test case for get_customer_balance

        Get the customer balance
        """
        pass

    def test_get_customer_info(self) -> None:
        """Test case for get_customer_info

        Get the customer info
        """
        pass

    def test_get_customer_operations(self) -> None:
        """Test case for get_customer_operations

        Get the customer operations
        """
        pass

    def test_get_payment_account(self) -> None:
        """Test case for get_payment_account

        Get the payment account
        """
        pass

    def test_get_payment_currencies(self) -> None:
        """Test case for get_payment_currencies

        Get currencies
        """
        pass

    def test_get_payment_quotas(self) -> None:
        """Test case for get_payment_quotas

        Get quotas
        """
        pass

    def test_get_payment_url(self) -> None:
        """Test case for get_payment_url

        Get the payment page URL
        """
        pass

    def test_get_portal_prices(self) -> None:
        """Test case for get_portal_prices

        Get prices
        """
        pass

    def test_get_quota_payment_information(self) -> None:
        """Test case for get_quota_payment_information

        Get quota payment information
        """
        pass

    def test_get_tenant_wallet_settings(self) -> None:
        """Test case for get_tenant_wallet_settings

        Get wallet auto top up settings
        """
        pass

    def test_send_payment_request(self) -> None:
        """Test case for send_payment_request

        Send a payment request
        """
        pass

    def test_set_tenant_wallet_settings(self) -> None:
        """Test case for set_tenant_wallet_settings

        Set wallet auto top up settings
        """
        pass

    def test_top_up_deposit(self) -> None:
        """Test case for top_up_deposit

        Put money on deposit
        """
        pass

    def test_update_payment(self) -> None:
        """Test case for update_payment

        Update the payment quantity
        """
        pass

    def test_update_wallet_payment(self) -> None:
        """Test case for update_wallet_payment

        Update the wallet payment quantity
        """
        pass


if __name__ == '__main__':
    unittest.main()
