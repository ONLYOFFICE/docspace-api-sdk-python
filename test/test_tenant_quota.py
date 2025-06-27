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

from docspace.models.tenant_quota import TenantQuota

class TestTenantQuota(unittest.TestCase):
    """TenantQuota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantQuota:
        """Test TenantQuota
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantQuota`
        """
        model = TenantQuota()
        if include_optional:
            return TenantQuota(
                tenant_id = 1234,
                name = 'Default',
                price = 10,
                price_currency_symbol = 'some text',
                price_iso_currency_symbol = 'some text',
                product_id = '9846',
                visible = True,
                wallet = True,
                due_date = '2008-04-10T06:30+04:00',
                features = 'some text',
                max_file_size = 26214400,
                max_total_size = 56,
                count_user = 1234,
                count_room_admin = 1234,
                users_in_room = 1234,
                count_room = 1234,
                non_profit = True,
                trial = True,
                free = True,
                update = True,
                audit = True,
                docs_edition = True,
                ldap = True,
                sso = True,
                statistic = True,
                branding = True,
                customization = True,
                lifetime = True,
                custom = True,
                auto_backup_restore = True,
                oauth = True,
                content_search = True,
                third_party = True,
                year = True
            )
        else:
            return TenantQuota(
        )
        """

    def testTenantQuota(self):
        """Test TenantQuota"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
