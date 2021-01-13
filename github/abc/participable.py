"""
/github/abc/participable.py

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

from github.iterator import CollectionIterator


class Participable():
    """
    Represents an object that can be participated on.
    """

    __slots__ = ()

    def fetch_participants(self, **kwargs):
        """
        |aiter|

        Fetches users participating on the participable.

        Parameters
        ----------
        **kwargs
            Keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.User`.
        """

        from github.objects import User

        def map_func(data):
            return User.from_data(data, self.http)

        map = {
            "Issue": self.http.fetch_issue_participants,
            "PullRequest": self.http.fetch_pull_request_participants,
        }

        return CollectionIterator(
            map[self.data["__typename"]],
            self.id,
            map_func=map_func,
            **kwargs
        )
