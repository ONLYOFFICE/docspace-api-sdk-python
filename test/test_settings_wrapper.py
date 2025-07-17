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

from docspace-api-python.models.settings_wrapper import SettingsWrapper

class TestSettingsWrapper(unittest.TestCase):
    """SettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsWrapper:
        """Test SettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsWrapper`
        """
        model = SettingsWrapper()
        if include_optional:
            return SettingsWrapper(
                response = docspace-api-python.models.settings_dto.SettingsDto(
                    timezone = 'UTC', 
                    trusted_domains = mydomain.com, 
                    trusted_domains_type = 0, 
                    culture = 'en-US', 
                    utc_offset = '-8.5', 
                    utc_hours_offset = -8.5, 
                    greeting_settings = 'Web Office Applications', 
                    owner_id = '75a5f745-f697-4418-b38d-0fe0d277e258', 
                    name_schema_id = 'some text', 
                    enabled_join = True, 
                    enable_adm_mess = True, 
                    thirdparty_enable = True, 
                    doc_space = True, 
                    standalone = True, 
                    is_ami = True, 
                    base_domain = 'some text', 
                    wizard_token = 'some text', 
                    password_hash = docspace-api-python.models.password_hasher.PasswordHasher(
                        size = 1234, 
                        iterations = 1234, 
                        salt = 'some text', ), 
                    firebase = docspace-api-python.models.firebase_dto.FirebaseDto(
                        api_key = 'some text', 
                        auth_domain = 'some text', 
                        project_id = 'some text', 
                        storage_bucket = 'some text', 
                        messaging_sender_id = 'some text', 
                        app_id = 'some text', 
                        measurement_id = 'some text', 
                        database_url = 'some text', ), 
                    version = 'some text', 
                    recaptcha_type = 0, 
                    recaptcha_public_key = 'some text', 
                    debug_info = True, 
                    socket_url = 'some text', 
                    tenant_status = 0, 
                    tenant_alias = 'some text', 
                    display_about = True, 
                    domain_validator = docspace-api-python.models.tenant_domain_validator.TenantDomainValidator(
                        regex = 'some text', 
                        min_length = 1234, 
                        max_length = 63, ), 
                    zendesk_key = 'some text', 
                    tag_manager_id = 'some text', 
                    cookie_settings_enabled = True, 
                    limited_access_space = True, 
                    limited_access_dev_tools_for_users = True, 
                    display_banners = True, 
                    user_name_regex = 'some text', 
                    invitation_limit = 1234, 
                    plugins = docspace-api-python.models.plugins_dto.PluginsDto(
                        enabled = True, 
                        upload = True, 
                        delete = True, ), 
                    deep_link = docspace-api-python.models.deep_link_dto.DeepLinkDto(
                        android_package_name = 'some text', 
                        url = 'some text', 
                        ios_package_id = 'some text', ), 
                    form_gallery = docspace-api-python.models.form_gallery_dto.FormGalleryDto(
                        path = 'some text', 
                        domain = 'some text', 
                        ext = '.txt', 
                        upload_path = 'some text', 
                        upload_domain = 'some text', 
                        upload_ext = 'some text', 
                        upload_dashboard = 'some text', ), 
                    max_image_upload_size = 1234, 
                    logo_text = 'some text', 
                    external_resources = docspace-api-python.models.culture_specific_external_resources.CultureSpecificExternalResources(
                        api = docspace-api-python.models.culture_specific_external_resource.CultureSpecificExternalResource(
                            domain = 'some text', 
                            entries = [{"key":"some text","value":"some text"}], ), 
                        common = docspace-api-python.models.culture_specific_external_resource.CultureSpecificExternalResource(
                            domain = 'some text', 
                            entries = [{"key":"some text","value":"some text"}], ), 
                        forum = , 
                        helpcenter = , 
                        integrations = , 
                        site = , 
                        social_networks = , 
                        support = , 
                        videoguides = , ), ),
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
            return SettingsWrapper(
        )
        """

    def testSettingsWrapper(self):
        """Test SettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
