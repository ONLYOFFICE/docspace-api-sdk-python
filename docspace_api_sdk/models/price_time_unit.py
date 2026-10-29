#
# (c) Copyright Ascensio System SIA 2026
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



from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PriceTimeUnit(int, Enum):
    """
    [1 - None, 2 - Hour, 3 - Day, 4 - Week, 5 - Month, 6 - Year, 7 - ThreeYears, 8 - Minute]
    """

    """
    allowed enum values
    """
    None_ = 1
    Hour = 2
    Day = 3
    Week = 4
    Month = 5
    Year = 6
    ThreeYears = 7
    Minute = 8

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PriceTimeUnit from a JSON string"""
        return cls(json.loads(json_str))

