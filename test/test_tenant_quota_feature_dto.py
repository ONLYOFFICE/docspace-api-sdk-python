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

from docspace-api-sdk.models.tenant_quota_feature_dto import TenantQuotaFeatureDto

class TestTenantQuotaFeatureDto(unittest.TestCase):
    """TenantQuotaFeatureDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantQuotaFeatureDto:
        """Test TenantQuotaFeatureDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantQuotaFeatureDto`
        """
        model = TenantQuotaFeatureDto()
        if include_optional:
            return TenantQuotaFeatureDto(
                id = '9846',
                title = 'legacy_1080p_small_wooden_mouse',
                image = 'some text',
                value = {"int":1234,"string":"some text","boolean":true},
                type = 'some text',
                used = docspace-api-sdk.models.feature_used_dto.FeatureUsedDto(
                    value = {"int":1234,"string":"some text","boolean":true}, 
                    title = 'legacy_1080p_small_wooden_mouse', ),
                price_title = 'some text'
            )
        else:
            return TenantQuotaFeatureDto(
        )
        """

    def testTenantQuotaFeatureDto(self):
        """Test TenantQuotaFeatureDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
