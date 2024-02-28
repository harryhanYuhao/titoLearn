%global srcname copr-tito-quickdoc

Name: hellocopr
Version: 1.1.2
Release: 1%{?dist}
License: GPLv3
Summary: A trivial python 3 program for demonstrating RPM packaging
Url: https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/copr-tito-quickdoc
# cd copr-tito-quickdoc
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?el6}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
Hellocopr is a very simple demonstration program that does nothing but display
some text on the command line. It is used as an example for automatic RPM
packaging using tito and Fedora's Copr user repository.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
%py3_build

%install
%py3_install

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/hellocopr
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk> 1.1.2-1
- Try
* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk>
- updated quickdoc file (ce@lcts.de)
- Update README.md (ce@lcts.de)
- Update README.md (ce@lcts.de)
- annotate doc specfile (ce@lcts.de)
- update readme (ce@lcts.de)
- add annotated specfile (ce@lcts.de)
- add quickdoc (ce@lcts.de)
- update readme (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.2-1]. (ce@lcts.de)
- let tito manage the version string (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.1-1]. (ce@lcts.de)
- single-source program version (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.0-1]. (ce@lcts.de)
- Initialized to use tito. (ce@lcts.de)
- add specfile (ce@lcts.de)
- add mail address (ce@lcts.de)
- display version (ce@lcts.de)

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk>
- updated quickdoc file (ce@lcts.de)
- Update README.md (ce@lcts.de)
- Update README.md (ce@lcts.de)
- annotate doc specfile (ce@lcts.de)
- update readme (ce@lcts.de)
- add annotated specfile (ce@lcts.de)
- add quickdoc (ce@lcts.de)
- update readme (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.2-1]. (ce@lcts.de)
- let tito manage the version string (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.1-1]. (ce@lcts.de)
- single-source program version (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.0-1]. (ce@lcts.de)
- Initialized to use tito. (ce@lcts.de)
- add specfile (ce@lcts.de)
- add mail address (ce@lcts.de)
- display version (ce@lcts.de)

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk>
- updated quickdoc file (ce@lcts.de)
- Update README.md (ce@lcts.de)
- Update README.md (ce@lcts.de)
- annotate doc specfile (ce@lcts.de)
- update readme (ce@lcts.de)
- add annotated specfile (ce@lcts.de)
- add quickdoc (ce@lcts.de)
- update readme (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.2-1]. (ce@lcts.de)
- let tito manage the version string (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.1-1]. (ce@lcts.de)
- single-source program version (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.0-1]. (ce@lcts.de)
- Initialized to use tito. (ce@lcts.de)
- add specfile (ce@lcts.de)
- add mail address (ce@lcts.de)
- display version (ce@lcts.de)

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk>
- updated quickdoc file (ce@lcts.de)
- Update README.md (ce@lcts.de)
- Update README.md (ce@lcts.de)
- annotate doc specfile (ce@lcts.de)
- update readme (ce@lcts.de)
- add annotated specfile (ce@lcts.de)
- add quickdoc (ce@lcts.de)
- update readme (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.2-1]. (ce@lcts.de)
- let tito manage the version string (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.1-1]. (ce@lcts.de)
- single-source program version (ce@lcts.de)
- Automatic commit of package [hellocopr] release [1.0.0-1]. (ce@lcts.de)
- Initialized to use tito. (ce@lcts.de)
- add specfile (ce@lcts.de)
- add mail address (ce@lcts.de)
- display version (ce@lcts.de)

* Fri Jul 24 2020 Christopher Engelhard <ce@lcts.de> 1.0.2-1
- let tito manage the version string (ce@lcts.de)

* Fri Jul 24 2020 Christopher Engelhard <ce@lcts.de> 1.0.1-1
- single-source program version (ce@lcts.de)

* Fri Jul 24 2020 Christopher Engelhard <ce@lcts.de> 1.0.0-1
- new package built with tito


