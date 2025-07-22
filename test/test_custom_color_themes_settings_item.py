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

from docspace-api-sdk.models.custom_color_themes_settings_item import CustomColorThemesSettingsItem

class TestCustomColorThemesSettingsItem(unittest.TestCase):
    """CustomColorThemesSettingsItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomColorThemesSettingsItem:
        """Test CustomColorThemesSettingsItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomColorThemesSettingsItem`
        """
        model = CustomColorThemesSettingsItem()
        if include_optional:
            return CustomColorThemesSettingsItem(
                id = 1,
                name = 'blue',
                main = docspace-api-sdk.models.custom_color_themes_settings_color_item.CustomColorThemesSettingsColorItem(
                    accent = '#4781D1', 
                    buttons = '#5299E0', ),
                text = docspace-api-sdk.models.custom_color_themes_settings_color_item.CustomColorThemesSettingsColorItem(
                    accent = '#4781D1', 
                    buttons = '#5299E0', )
            )
        else:
            return CustomColorThemesSettingsItem(
        )
        """

    def testCustomColorThemesSettingsItem(self):
        """Test CustomColorThemesSettingsItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
