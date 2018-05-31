import logging
import os
from concurrent.futures import ThreadPoolExecutor
from urllib.error import URLError, HTTPError
from urllib.request import urlopen, Request

import whois


class WebScanner:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.sub_links = self._load_sub_links()
        pass

    def find_admin(self, url):
        futures = []
        if self._check_link(url) is None:
            return futures

        with ThreadPoolExecutor(max_workers=4) as executor:
            available_links = []
            for sub_link in self.sub_links:
                future = executor.submit(self._check_link, url + "/" + sub_link)
                futures.append(future)

            for future in futures:
                result = future.result()
                if result is not None:
                    available_links.append(result)
            return available_links

    def whois(self, url):
        re = whois.whois(url)
        import json

        # array = re
        data = json.loads(str(re))
        res=""
        for d in data:
            res += str(d).upper().replace("_"," ")+ ": "+ str(data[d]).replace("'","").replace("[","").replace("]","")+"\n"

        return res

    def _check_link(self, req_link):
        self.logger.debug("Scanning " + req_link)
        req = Request(req_link)
        try:
            urlopen(req)
        except HTTPError:
            # self.logger.exception("HTTPError")
            return
        except URLError:
            # self.logger.exception("URLError")
            return
        else:
            return req_link

    @staticmethod
    def _load_sub_links():
        with open(os.path.dirname(os.path.abspath(__file__)) + "/resources/link.txt", "r") as f:
            content = f.read().splitlines()
            return content



