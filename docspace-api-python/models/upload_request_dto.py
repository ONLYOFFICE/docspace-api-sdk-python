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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Tuple, Union
from docspace-api-python.models.content_disposition import ContentDisposition
from docspace-api-python.models.content_type import ContentType
from typing import Optional, Set
from typing_extensions import Self

class UploadRequestDto(BaseModel):
    """
    The request parameters for uploading a file.
    """ # noqa: E501
    file: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]] = Field(default=None, description="The file to be uploaded.")
    content_type: Optional[ContentType] = Field(default=None, alias="contentType")
    content_disposition: Optional[ContentDisposition] = Field(default=None, alias="contentDisposition")
    files: Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]] = Field(default=None, description="The list of files when specified as multipart/form-data.")
    create_new_if_exist: Optional[StrictBool] = Field(default=None, description="Specifies whether to create the new file if it already exists or not.", alias="createNewIfExist")
    store_original_file_flag: Optional[StrictBool] = Field(default=None, description="Specifies whether to upload documents in the original formats as well or not.", alias="storeOriginalFileFlag")
    keep_convert_status: Optional[StrictBool] = Field(default=None, description="Specifies whether to keep the file converting status or not.", alias="keepConvertStatus")
    stream: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]] = Field(default=None, description="The request input stream.")
    __properties: ClassVar[List[str]] = ["file", "contentType", "contentDisposition", "files", "createNewIfExist", "storeOriginalFileFlag", "keepConvertStatus", "stream"]

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
        """Create an instance of UploadRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content_type
        if self.content_type:
            _dict['contentType'] = self.content_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content_disposition
        if self.content_disposition:
            _dict['contentDisposition'] = self.content_disposition.to_dict()
        # set to None if file (nullable) is None
        # and model_fields_set contains the field
        if self.file is None and "file" in self.model_fields_set:
            _dict['file'] = None

        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        # set to None if store_original_file_flag (nullable) is None
        # and model_fields_set contains the field
        if self.store_original_file_flag is None and "store_original_file_flag" in self.model_fields_set:
            _dict['storeOriginalFileFlag'] = None

        # set to None if stream (nullable) is None
        # and model_fields_set contains the field
        if self.stream is None and "stream" in self.model_fields_set:
            _dict['stream'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UploadRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file": obj.get("file"),
            "contentType": ContentType.from_dict(obj["contentType"]) if obj.get("contentType") is not None else None,
            "contentDisposition": ContentDisposition.from_dict(obj["contentDisposition"]) if obj.get("contentDisposition") is not None else None,
            "files": obj.get("files"),
            "createNewIfExist": obj.get("createNewIfExist"),
            "storeOriginalFileFlag": obj.get("storeOriginalFileFlag"),
            "keepConvertStatus": obj.get("keepConvertStatus"),
            "stream": obj.get("stream")
        })
        return _obj


