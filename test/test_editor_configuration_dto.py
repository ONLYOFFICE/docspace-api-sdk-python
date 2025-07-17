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

from docspace-api-python.models.editor_configuration_dto import EditorConfigurationDto

class TestEditorConfigurationDto(unittest.TestCase):
    """EditorConfigurationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditorConfigurationDto:
        """Test EditorConfigurationDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditorConfigurationDto`
        """
        model = EditorConfigurationDto()
        if include_optional:
            return EditorConfigurationDto(
                callback_url = 'some text',
                co_editing = docspace-api-python.models.co_editing_config.CoEditingConfig(
                    change = True, 
                    fast = True, 
                    mode = 0, ),
                create_url = 'some text',
                customization = docspace-api-python.models.customization_config_dto.CustomizationConfigDto(
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
                        text = 'some text', ), ),
                embedded = docspace-api-python.models.embedded_config.EmbeddedConfig(
                    embed_url = 'some text', 
                    save_url = 'some text', 
                    share_link_param = 'some text', 
                    share_url = 'some text', 
                    toolbar_docked = 'some text', ),
                encryption_keys = docspace-api-python.models.encryption_keys_config.EncryptionKeysConfig(
                    crypto_engine_id = 'some text', 
                    private_key_enc = 'some text', 
                    public_key = 'some text', ),
                lang = 'some text',
                mode = 'some text',
                mode_write = True,
                plugins = docspace-api-python.models.plugins_config.PluginsConfig(
                    plugins_data = ["some text"], ),
                recent = [
                    docspace-api-python.models.recent_config.RecentConfig(
                        folder = 'some text', 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        url = 'some text', )
                    ],
                templates = [
                    docspace-api-python.models.templates_config.TemplatesConfig(
                        image = 'some text', 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        url = 'some text', )
                    ],
                user = docspace-api-python.models.user_config.UserConfig(
                    id = '9846', 
                    name = 'Winfield Upton', 
                    image = 'some text', 
                    roles = ["some text"], )
            )
        else:
            return EditorConfigurationDto(
        )
        """

    def testEditorConfigurationDto(self):
        """Test EditorConfigurationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
