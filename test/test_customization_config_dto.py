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

from docspace-api-python.models.customization_config_dto import CustomizationConfigDto

class TestCustomizationConfigDto(unittest.TestCase):
    """CustomizationConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomizationConfigDto:
        """Test CustomizationConfigDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomizationConfigDto`
        """
        model = CustomizationConfigDto()
        if include_optional:
            return CustomizationConfigDto(
                about = True,
                customer = docspace-api-python.models.customer_config_dto.CustomerConfigDto(
                    address = 'some text', 
                    logo = 'some text', 
                    logo_dark = 'some text', 
                    mail = 'some text', 
                    name = 'Winfield Upton', 
                    www = 'some text', ),
                anonymous = docspace-api-python.models.anonymous_config_dto.AnonymousConfigDto(
                    request = True, ),
                feedback = docspace-api-python.models.feedback_config.FeedbackConfig(
                    url = 'some text', 
                    visible = True, ),
                forcesave = True,
                goback = docspace-api-python.models.goback_config.GobackConfig(
                    url = 'some text', ),
                review = docspace-api-python.models.review_config.ReviewConfig(
                    review_display = 'some text', ),
                logo = docspace-api-python.models.logo_config_dto.LogoConfigDto(
                    image = 'some text', 
                    image_dark = 'some text', 
                    image_light = 'some text', 
                    image_embedded = 'some text', 
                    url = 'some text', 
                    visible = True, ),
                mention_share = True,
                submit_form = docspace-api-python.models.submit_form.SubmitForm(
                    visible = True, 
                    result_message = 'some text', ),
                start_filling_form = docspace-api-python.models.start_filling_form.StartFillingForm(
                    text = 'some text', )
            )
        else:
            return CustomizationConfigDto(
        )
        """

    def testCustomizationConfigDto(self):
        """Test CustomizationConfigDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
