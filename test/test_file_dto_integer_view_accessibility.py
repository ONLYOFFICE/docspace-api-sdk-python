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

from docspace-api-sdk.models.file_dto_integer_view_accessibility import FileDtoIntegerViewAccessibility

class TestFileDtoIntegerViewAccessibility(unittest.TestCase):
    """FileDtoIntegerViewAccessibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileDtoIntegerViewAccessibility:
        """Test FileDtoIntegerViewAccessibility
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileDtoIntegerViewAccessibility`
        """
        model = FileDtoIntegerViewAccessibility()
        if include_optional:
            return FileDtoIntegerViewAccessibility(
                image_view = True,
                media_view = True,
                web_view = True,
                web_edit = True,
                web_review = True,
                web_custom_filter_editing = True,
                web_restricted_editing = True,
                web_comment = True,
                co_auhtoring = True,
                can_convert = True,
                must_convert = True
            )
        else:
            return FileDtoIntegerViewAccessibility(
        )
        """

    def testFileDtoIntegerViewAccessibility(self):
        """Test FileDtoIntegerViewAccessibility"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
