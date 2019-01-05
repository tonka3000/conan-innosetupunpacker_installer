#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):

    def imports(self):
        self.copy("*", src="", dst="")

    def test(self):
        if not tools.which("innounp.exe"):
            raise Exception("could not find innounp.exe with which")
        if not os.path.exists("innounp.exe"):
            raise Exception("could not find innounp.exe")
