%{?scl:%scl_package nodejs-osenv}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-osenv
Version:        0.1.3
Release:        2%{?dist}
Summary:        Look up environment settings specific to different operating systems
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
License:        ISC
URL:            https://github.com/isaacs/osenv
Source0:        http://registry.npmjs.org/osenv/-/osenv-%{version}.tgz

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Look up environment settings specific to different operating systems.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/osenv
cp -pr package.json osenv.js %{buildroot}%{nodejs_sitelib}/osenv

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/osenv
%doc LICENSE README.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.3-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-1
- New upstream release

* Fri Feb 28 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.3-6
- rebuilt, bump release to fix rhbz#1070612

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.3-5
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.3-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- initial package generated by npm2rpm
