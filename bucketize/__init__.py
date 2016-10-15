#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bucketize.py
#
#  Copyright 2016 Jelle Smet <development@smetj.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import sys
import signal
import argparse
from time import time
import re


class Bucketize(object):

    def __init__(self, bucketize, template, ignore_regex, exit_regex):
        self.bucketize = bucketize
        self.template = template
        self.ignore_regex = ignore_regex
        self.exit_regex = exit_regex

        self.counter = 0
        signal.signal(signal.SIGALRM, self.timeout)

    def timeout(self, num, stack):

        sys.stdout.write(self.template.format(amount=self.counter, time=time()))
        sys.stdout.write("\n")
        sys.stdout.flush()
        self.counter = 0
        signal.alarm(self.bucketize)

    def readInput(self):
        signal.alarm(self.bucketize)
        while True:
            line = ''
            while True:
                try:
                    line += sys.stdin.read(1)
                except IOError:
                    pass
                else:
                    if line.endswith('\n'):
                        if not self.filter(line):
                            self.counter += 1
                        break

    def filter(self, string):

        if self.exit_regex != "":
            if re.search(self.exit_regex, string):
                sys.exit(0)
        if self.ignore_regex != "":
            if re.search(self.ignore_regex, string):
                return True
            else:
                return False
        else:
            return False


def main():

    try:
        parser = argparse.ArgumentParser(description="Determine STDIN line rate at the chosen interval")
        parser.add_argument("--time_bucket_size", type=int, dest="time_bucket_size", default=10, help="The time bucket in seconds.")
        parser.add_argument("--output_template", type=str, dest="output_template", default='{amount}', help="Template to construct the output. {amount} is the number of lines read per bucket. {time} is epoch.")
        parser.add_argument("--ignore_regex", type=str, default="", help="If defined, ignores any lines matching the regex.")
        parser.add_argument("--exit_regex", type=str, default="", help="If defined, exits when line matches.")

        arguments = vars(parser.parse_args())

        i = Bucketize(arguments["time_bucket_size"], arguments["output_template"], arguments["ignore_regex"], arguments["exit_regex"])
        i.readInput()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
