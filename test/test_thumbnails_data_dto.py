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

from docspace-api-sdk.models.thumbnails_data_dto import ThumbnailsDataDto

class TestThumbnailsDataDto(unittest.TestCase):
    """ThumbnailsDataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ThumbnailsDataDto:
        """Test ThumbnailsDataDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThumbnailsDataDto`
        """
        model = ThumbnailsDataDto()
        if include_optional:
            return ThumbnailsDataDto(
                original = 'default_user_photo_size_1280-1280.png',
                retina = 'default_user_photo_size_360-360.png',
                max = 'default_user_photo_size_200-200.png',
                big = 'default_user_photo_size_82-82.png',
                medium = 'default_user_photo_size_48-48.png',
                small = 'default_user_photo_size_32-32.png'
            )
        else:
            return ThumbnailsDataDto(
        )
        """

    def testThumbnailsDataDto(self):
        """Test ThumbnailsDataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
