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

from docspace-api-sdk.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto

class TestUpdateMembersQuotaRequestDto(unittest.TestCase):
    """UpdateMembersQuotaRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateMembersQuotaRequestDto:
        """Test UpdateMembersQuotaRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateMembersQuotaRequestDto`
        """
        model = UpdateMembersQuotaRequestDto()
        if include_optional:
            return UpdateMembersQuotaRequestDto(
                user_ids = ["75a5f745-f697-4418-b38d-0fe0d277e258"],
                quota = None
            )
        else:
            return UpdateMembersQuotaRequestDto(
        )
        """

    def testUpdateMembersQuotaRequestDto(self):
        """Test UpdateMembersQuotaRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
