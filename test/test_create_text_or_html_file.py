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

from docspace-api-python.models.create_text_or_html_file import CreateTextOrHtmlFile

class TestCreateTextOrHtmlFile(unittest.TestCase):
    """CreateTextOrHtmlFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTextOrHtmlFile:
        """Test CreateTextOrHtmlFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTextOrHtmlFile`
        """
        model = CreateTextOrHtmlFile()
        if include_optional:
            return CreateTextOrHtmlFile(
                title = 'legacy_1080p_small_wooden_mouse',
                content = 'some text',
                create_new_if_exist = True
            )
        else:
            return CreateTextOrHtmlFile(
                title = 'legacy_1080p_small_wooden_mouse',
        )
        """

    def testCreateTextOrHtmlFile(self):
        """Test CreateTextOrHtmlFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
