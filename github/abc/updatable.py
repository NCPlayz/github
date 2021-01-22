"""
/github/abc/updatable.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from github.enums import CannotUpdateReason


class Updatable():
    """
    Represents an entity that can be updated.
    """

    __slots__ = ()

    @property
    def viewer_can_update(self):
        """
        Whether the authenticated user can update the updatable.

        :type: :class:`bool`
        """

        return self.data["viewerCanUpdate"]

    @property
    def viewer_cannot_update_reasons(self):
        """
        A list of reasons why the authenticated user cannot update this
        updatable.

        :type: List[:class:`~github.enums.CannotUpdateReason`]
        """

        reasons = self.data.get("viewerCannotUpdateReasons", [])
        return [CannotUpdateReason.try_value(r) for (r) in reasons]
