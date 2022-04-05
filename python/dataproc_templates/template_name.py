# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from enum import Enum

__all__ = ['TemplateName']


class TemplateName(Enum):
    """Enumeration of all template types"""

    GCSTOBIGQUERY = 'GCSTOBIGQUERY'

    @classmethod
    def from_string(cls, template_name: str) -> TemplateName:
        """
        Get the TemplateName value from a string.

        This is not case-sensitive.

        Args:
            template_name (str): The string representation of
                the template name.
        
        Returns:
            TemplateName: the TemplateName value corresponding
                to the provided string
        
        Raises:
            ValueError: if the given template name is invalid
        """

        try:
            return cls[template_name.upper()]
        except KeyError as err:
            raise ValueError(f'Invalid template name {template_name}')