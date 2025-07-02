# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



import unittest

from docspace-api-python.api.portal_payment_api import PortalPaymentApi


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

    def test_get_accounting_currencies(self) -> None:
        """Test case for get_accounting_currencies

        Get list of currencies
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

    def test_open_customer_session(self) -> None:
        """Test case for open_customer_session

        Open customer session
        """
        pass

    def test_perform_customer_operation(self) -> None:
        """Test case for perform_customer_operation

        Perform customer operation
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
