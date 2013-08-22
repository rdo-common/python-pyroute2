%global pkgname pyroute2

Name: python-%{pkgname}
Version: 0.1.11
Release: 1%{?dist}
Summary: Pure Python netlink library
License: GPLv2+
Group: Development/Languages
URL: https://github.com/svinota/%{pkgname}

BuildArch: noarch
BuildRequires: python2-devel
Source: http://peet.spb.ru/archives/%{pkgname}-%{version}.tar.gz

%description
PyRoute2 provides basic netlink interface for Python programs. Aiming
to provide a complete implementation of several netlink families, this
library is still in alpha state, so check STATUS file, the work is in
progress.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# nothing to build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc STATUS* README* LICENSE
%{python_sitelib}/%{pkgname}*

%changelog
* Thu Aug 22 2013 Peter V. Saveliev <peet@redhat.com> 0.1.11-1
- IPRSocket threadless objects
- rtnl: tc filters improvements

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 26 2013 Peter V. Saveliev <peet@redhat.com> 0.1.10-1
- fd and threads leaks fixed
- shutdown sequence fixed (release() calls)
- ipdb: interface removal
- ipdb: fail on transaction sync timeout

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-2
- fedpkg import fix

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-1
- several races fixed
- Python 2.6 compatibility issues fixed

* Thu Jun 05 2013 Peter V. Saveliev <peet@redhat.com> 0.1.8-1
- initial RH build

