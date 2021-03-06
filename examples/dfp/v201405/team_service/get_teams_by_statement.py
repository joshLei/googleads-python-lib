#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets a single team by ID.

To create teams, run create_teams.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

Tags: TeamService.getTeamsByStatement
"""

__author__ = ('Nicholas Chen',
              'Joseph DiLallo')

# Import appropriate modules from the client library.
from googleads import dfp

TEAM_ID = 'INSERT_TEAM_ID_HERE'


def main(client, team_id):
  # Initialize appropriate service.
  team_service = client.GetService('TeamService', version='v201405')

  # Create a filter statement to select a single team by ID.
  values = [{
      'key': 'teamId',
      'value': {
          'xsi_type': 'NumberValue',
          'value': team_id
      }
  }]
  query = 'WHERE id = :teamId'
  statement = dfp.FilterStatement(query, values)

  while True:
    # Get teams by statement.
    response = team_service.getTeamsByStatement(statement.ToStatement())
    if 'results' in response:
      # Display results.
      for team in response['results']:
        print ('Team with id \'%s\' and name \'%s\' was found.'
               % (team['id'], team['name']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']

if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client, TEAM_ID)
