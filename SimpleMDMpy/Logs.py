#!/usr/bin/env python

"""Logs module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class Logs(SimpleMDMpy.SimpleMDM.Connection):
    """GET all the LOGS"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/logs")
    
    # FIXME: when setting limit, there may be an indefinite loop
    def get_logs(self, starting_after=None, limit=None):
        """And I mean all the LOGS"""
        url = self.url
        params = {}
        if starting_after:
            params['starting_after'] = starting_after
        if limit:
            params['limit'] = limit
        return self._get_data(url, params=params)
