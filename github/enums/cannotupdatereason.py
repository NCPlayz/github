"""
/github/enums/cannotupdatereason.py

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

from github.enums import Enum


class CannotUpdateReason(Enum):
    """
    Represents a reason the authenticated user cannot update an updatable.
    """

    # https://developer.github.com/v4/enum/commentcannotupdatereason/

    archived                = "ARCHIVED"
    denied                  = "DENIED"
    insufficient_access     = "INSUFFICIENT_ACCESS"
    locked                  = "LOCKED"
    login_required          = "LOGIN_REQUIRED"
    maintenance             = "MAINTENANCE"
    verified_email_required = "VERIFIED_EMAIL_REQUIRED"
