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

from docspace-api-sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper

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
                settings = docspace-api-sdk.models.additional_white_label_settings.AdditionalWhiteLabelSettings(
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
