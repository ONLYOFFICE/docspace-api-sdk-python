# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace.models.distributed_task_status import DistributedTaskStatus
from typing import Optional, Set
from typing_extensions import Self

class DocumentBuilderTaskDto(BaseModel):
    """
    The document builder task parameters.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The document builder ID.")
    error: Optional[StrictStr] = Field(default=None, description="The error message occured while the document building process.")
    percentage: Optional[StrictInt] = Field(default=None, description="The percentage of the progress of the document building process.")
    is_completed: Optional[StrictBool] = Field(default=None, description="Specifies whether the document building process is completed or not.", alias="isCompleted")
    status: Optional[DistributedTaskStatus] = None
    result_file_id: Optional[Any] = Field(default=None, description="The result file ID.", alias="resultFileId")
    result_file_name: Optional[StrictStr] = Field(default=None, description="The result file name.", alias="resultFileName")
    result_file_url: Optional[StrictStr] = Field(default=None, description="The result file URL.", alias="resultFileUrl")
    __properties: ClassVar[List[str]] = ["id", "error", "percentage", "isCompleted", "status", "resultFileId", "resultFileName", "resultFileUrl"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DocumentBuilderTaskDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if result_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.result_file_id is None and "result_file_id" in self.model_fields_set:
            _dict['resultFileId'] = None

        # set to None if result_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.result_file_name is None and "result_file_name" in self.model_fields_set:
            _dict['resultFileName'] = None

        # set to None if result_file_url (nullable) is None
        # and model_fields_set contains the field
        if self.result_file_url is None and "result_file_url" in self.model_fields_set:
            _dict['resultFileUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentBuilderTaskDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "error": obj.get("error"),
            "percentage": obj.get("percentage"),
            "isCompleted": obj.get("isCompleted"),
            "status": obj.get("status"),
            "resultFileId": obj.get("resultFileId"),
            "resultFileName": obj.get("resultFileName"),
            "resultFileUrl": obj.get("resultFileUrl")
        })
        return _obj


