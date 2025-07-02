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

from docspace-api-python.models.payment_settings_wrapper import PaymentSettingsWrapper

class TestPaymentSettingsWrapper(unittest.TestCase):
    """PaymentSettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentSettingsWrapper:
        """Test PaymentSettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentSettingsWrapper`
        """
        model = PaymentSettingsWrapper()
        if include_optional:
            return PaymentSettingsWrapper(
                response = docspace-api-python.models.payment_settings_dto.PaymentSettingsDto(
                    sales_email = 'some text', 
                    feedback_and_support_url = 'some text', 
                    buy_url = 'some text', 
                    standalone = True, 
                    current_license = docspace-api-python.models.current_license_info.CurrentLicenseInfo(
                        trial = True, 
                        due_date = '2008-04-10T06:30+04:00', ), 
                    max = 1234, ),
                count = 56,
                links = [
                    docspace-api-python.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return PaymentSettingsWrapper(
        )
        """

    def testPaymentSettingsWrapper(self):
        """Test PaymentSettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
