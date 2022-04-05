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
from typing import Dict

from abc import ABC as AbstractClass, abstractmethod

__all__ = ['BaseTemplate']


class BaseTemplate(AbstractClass):
    """Base class for all Dataproc Templates"""

    @classmethod
    def build(cls) -> BaseTemplate:
        """
        Factory method for building an instance of this template class.

        This might not be necessary once we define how templates
        are constructed and how arguments are handled.
        """

        return cls()
    
    @abstractmethod
    def run(self, properties: Dict[str, str]) -> None:
        """
        Runs this template

        Args:
            properties (Dict[str, str]): Properties set for this
                template run
        """

        pass