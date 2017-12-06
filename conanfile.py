from conans import ConanFile, tools


class BoostLocaleConan(ConanFile):
    name = "Boost.Locale"
    version = "1.65.1"
    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Level11Group/1.65.1@bincrafters/testing"
    options = {"use_icu": [True, False]}
    default_options = "use_icu=False"
    lib_short_names = ["locale"]
    is_header_only = False
    is_in_cycle_group = True

    def configure(self):
        self.options["Boost.Level11Group"].use_icu = self.options.use_icu 

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-locale"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
