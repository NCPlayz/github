"""
/github/query/builtin_mutations.py

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

MUTATE_PROJECT_CREATE_COLUMN = """
mutation mutate_project_create_column ($input: AddProjectColumnInput!) {
  addProjectColumn (input: $input) {
    columnEdge {
      node {
        __typename
        createdAt
        databaseId
        id
        name
        purpose
        resourcePath
        updatedAt
        url
      }
    }
  }
}
"""

MUTATE_PROJECTCARD_MOVE_TO = """
mutation mutate_projectcard_move_to ($input: MoveProjectCardInput!) {
  moveProjectCard (input: $input) {
    cardEdge {
      node {
        __typename
        createdAt
        databaseId
        id
        isArchived
        note
        resourcePath
        state
        updatedAt
        url
      }
    }
  }
}
"""

MUTATE_PROJECTCOLUMN_CREATE_CARD = """
mutation mutate_projectcolumn_create_card ($input: AddProjectCardInput!) {
  addProjectCard (input: $input) {
    cardEdge {
      node {
        __typename
        createdAt
        databaseId
        id
        isArchived
        note
        resourcePath
        state
        updatedAt
        url
      }
    }
  }
}
"""

MUTATE_PROJECTCOLUMN_MOVE_TO = """
mutation mutate_projectcolumn_move_to ($input: MoveProjectColumnInput!) {
  moveProjectColumn (input: $input) {
    columnEdge {
      node {
        __typename
        createdAt
        databaseId
        id
        name
        purpose
        resourcePath
        updatedAt
        url
      }
    }
  }
}
"""

MUTATE_PROJECTOWNER_CREATE_PROJECT = """
mutation mutate_projectowner_create_project ($input: CreateProjectInput!) {
  createProject (input: $input) {
    project {
      __typename
      body
      bodyHTML
      closed
      closedAt
      createdAt
      databaseId
      id
      name
      number
      resourcePath
      state
      updatedAt
      url
      viewerCanUpdate
    }
  }
}

"""
