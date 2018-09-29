#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostLocaleConan(base.BoostBaseConan):
    name = "boost_locale"
    url = "https://github.com/bincrafters/conan-boost_locale"
    lib_short_names = ["locale"]
    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"
    b2_options = {
        "boost.locale.iconv" : "off",
        "boost.locale.icu" : "on",
    }
    source_only_deps = [
        "chrono",
        "date_time",
        "numeric_conversion",
        "ratio",
        "thread",
        "unordered"
    ]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_function",
        "boost_iterator",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_system",
        "boost_type_traits"
    ]

    def requirements(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

    def package_info_additional(self):
        if self.options.use_icu:
            self.cpp_info.defines.append("BOOST_LOCALE_WITH_ICU=1")
        elif self.settings.os == "Macos":
            self.cpp_info.libs.append("iconv")

