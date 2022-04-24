from typing import List

from lib.action import PWVBase


class FixAccount(PWVBase):
    """
    Account model:
    {
      "id": "string",
      "name": "string",
      "address": "string",
      "userName": "string",
      "platformId": "string",
      "safeName": "string",
      "secretType": "key",
      "platformAccountProperties": {},
      "secretManagement": {
        "automaticManagementEnabled": true,
        "manualManagementReason": "string",
        "status": "inProcess",
        "lastModifiedTime": 0,
        "lastReconciledTime": 0,
        "lastVerifiedTime": 0
      },
      "remoteMachinesAccess": {
        "remoteMachines": "string",
        "accessRestrictedToRemoteMachines": true
      },
      "createdTime": 0
      "categoryModificationTime": 111111111111111111111
    }
    """

    def run(self, params: dict):
        pass

