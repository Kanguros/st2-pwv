from typing import List

from lib.action import PWVBase


class FindAccounts(PWVBase):

    def run(self,
            text: List[str] = None,
            safe: str = None):

        self.auth()

