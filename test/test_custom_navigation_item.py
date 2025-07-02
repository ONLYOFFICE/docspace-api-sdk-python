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

from docspace-api-python.models.custom_navigation_item import CustomNavigationItem

class TestCustomNavigationItem(unittest.TestCase):
    """CustomNavigationItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomNavigationItem:
        """Test CustomNavigationItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomNavigationItem`
        """
        model = CustomNavigationItem()
        if include_optional:
            return CustomNavigationItem(
                id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28',
                label = 'Label',
                url = 'Url',
                big_img = 'data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkAgMAAAANjH3HAAAADFBMVEUAAADJycnJycnJycmiuNtHAAAAA3RSTlMAf4C\/aSLHAAAAyElEQVR4Xu3NsQ3CMBSE4YubFB4ilHQegdGSjWACvEpGoEyBYiL05AdnXUGHolx10lf82MmOpfLeo5UoJUhBlpKkRCnhUy7b9XCWkqQMUkYlXVHSf8kTvkHKqKQrSnopg5SRxTMklLmS1MwaSWpmCSQ1MyOzWGZCYrEMEFksA4QqlAFuJJYBcCKxjM3FMySeIfEMC2dMOONCGZZgmdr1ly3TSrJMK9EyJBaaGrHQikYstAiJZRYSyiQEdyg5S8Evckih\/YPscsdej0H6dc0TYw4AAAAASUVORK5CYII=',
                small_img = 'data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8\/9hAAAAUUlEQVR4AWMY\/KC5o\/cAEP9HxxgKcSpCGELYADyu2E6mAQjNxBlAWPNxkHdwGkBIM3KYYDUAr2ZCAE+oH8eujrAXDsA0k2EAAtDXAGLx4MpsADUgvkRKUlqfAAAAAElFTkSuQmCC',
                show_in_menu = True,
                show_on_home_page = True
            )
        else:
            return CustomNavigationItem(
        )
        """

    def testCustomNavigationItem(self):
        """Test CustomNavigationItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
