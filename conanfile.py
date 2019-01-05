#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from conans.errors import ConanException


class InnoSetupUnpackerInstallerConan(ConanFile):
    name = "innosetupunpacker_installer"
    version = "0.47.0"
    description = "Inno Setup Unpacker binaries for use in recipes"
    topics = ("conan", "innosetupunpacker_installer")
    url = "https://github.com/bincrafters/conan-innosetupunpacker_installer"
    homepage = "https://sourceforge.net/projects/innounp"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "GPL-2.0"
    exports = ["LICENSE.md"]
    settings = "os_build", "arch_build"

    def build_requirements(self):
        if tools.os_info.is_windows:
            self.build_requires("7z_installer/1.0@conan/stable")

    def build(self):
        if not tools.os_info.is_windows:
            raise ConanException("Inno Setup Unpacker is only available on windows")

        version_short = ".".join(self.version.split(".")[:2])
        source_url = "{}/files/innounp/innounp%20{}/innounp{}.rar/download".format(self.homepage, version_short, version_short.replace(".", ""))
        self.output.info("Download {}".format(source_url))
        filename = "inno_setup_unpacker.rar"
        tools.download(source_url, filename)
        self.run('7z e {} "-o{}"'.format(filename, self.build_folder))

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="")
        self.copy(pattern="innounp.*", dst="", src="", keep_path=True)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)
