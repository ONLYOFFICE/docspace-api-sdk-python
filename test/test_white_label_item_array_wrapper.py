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

from docspace-api-python.models.white_label_item_array_wrapper import WhiteLabelItemArrayWrapper

class TestWhiteLabelItemArrayWrapper(unittest.TestCase):
    """WhiteLabelItemArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WhiteLabelItemArrayWrapper:
        """Test WhiteLabelItemArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WhiteLabelItemArrayWrapper`
        """
        model = WhiteLabelItemArrayWrapper()
        if include_optional:
            return WhiteLabelItemArrayWrapper(
                response = [
                    docspace-api-python.models.white_label_item_dto.WhiteLabelItemDto(
                        name = 'Winfield Upton', 
                        size = docspace-api-python.models.i_magick_geometry.IMagickGeometry(
                            aspect_ratio = True, 
                            fill_area = True, 
                            greater = True, 
                            height = 56, 
                            ignore_aspect_ratio = True, 
                            is_percentage = True, 
                            less = True, 
                            limit_pixels = True, 
                            width = 56, 
                            x = 1234, 
                            y = 1234, ), 
                        path = docspace-api-python.models.white_label_item_path_dto.WhiteLabelItemPathDto(
                            light = 'some text', 
                            dark = 'some text', ), )
                    ],
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
            return WhiteLabelItemArrayWrapper(
        )
        """

    def testWhiteLabelItemArrayWrapper(self):
        """Test WhiteLabelItemArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
