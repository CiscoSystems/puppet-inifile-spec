Name:		puppet-inifile	
Version:	0.1
Release:	1cisco%{?dist}
Summary:	Puppet inifile module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-inifile.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This module provides resource types for use in managing INI-style configuration files

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{name}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{name}/

%files
%dir %{_usr}/share/puppet/modules/%{name}/
%{_usr}/share/puppet/modules/%{name}/*


%defattr(-,root,root,-)
%doc README.md

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 25 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

