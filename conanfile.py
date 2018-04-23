#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLocaleConan(ConanFile):
    name = "boost_locale"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["locale"]
    is_header_only = False

    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"

    source_only_deps = [
        "chrono",
        "date_time",
        "numeric_conversion",
        "ratio",
        "thread",
        "unordered"
    ]

    requires = (
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_function/1.67.0@bincrafters/testing",
        "boost_iterator/1.67.0@bincrafters/testing",
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_system/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing"
    )

    def requirements(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

    def b2_options(self, lib_name=None):
        # pylint: disable=unused-argument
        if self.options.use_icu:
            return " boost.locale.iconv=off boost.locale.icu=on"
        else:
            return " boost.locale.icu=off"

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    def package_info_additional(self):
        if self.options.use_icu:
            self.cpp_info.defines.append("BOOST_LOCALE_WITH_ICU=1")
        elif self.settings.os == "Macos":
            self.cpp_info.libs.append("iconv")

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_locale"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()

    # END
