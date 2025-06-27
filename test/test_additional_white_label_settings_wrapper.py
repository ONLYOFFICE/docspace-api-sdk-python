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

from docspace.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper

class TestAdditionalWhiteLabelSettingsWrapper(unittest.TestCase):
    """AdditionalWhiteLabelSettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdditionalWhiteLabelSettingsWrapper:
        """Test AdditionalWhiteLabelSettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalWhiteLabelSettingsWrapper`
        """
        model = AdditionalWhiteLabelSettingsWrapper()
        if include_optional:
            return AdditionalWhiteLabelSettingsWrapper(
                settings = docspace.models.additional_white_label_settings.AdditionalWhiteLabelSettings(
                    start_docs_enabled = True, 
                    help_center_enabled = True, 
                    feedback_and_support_enabled = True, 
                    user_forum_enabled = True, 
                    video_guides_enabled = True, 
                    license_agreements_enabled = True, 
                    last_modified = '2008-04-10T06:30+04:00', )
            )
        else:
            return AdditionalWhiteLabelSettingsWrapper(
        )
        """

    def testAdditionalWhiteLabelSettingsWrapper(self):
        """Test AdditionalWhiteLabelSettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
