
Name: app-ftp-plugin-core
Group: ClearOS/Libraries
Version: 5.9.9.2
Release: 4%{dist}
Summary: FTP Server Accounts Plugin - APIs and install
License: LGPLv3
Packager: ClearFoundation
Vendor: ClearFoundation
Source: app-ftp-plugin-%{version}.tar.gz
Buildarch: noarch
Requires: app-base-core
Requires: app-accounts-core

%description
FTP Plugin long description

This package provides the core API and libraries.

%prep
%setup -q -n app-ftp-plugin-%{version}
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/ftp_plugin
cp -r * %{buildroot}/usr/clearos/apps/ftp_plugin/

install -D -m 0644 packaging/ftp.php %{buildroot}/var/clearos/accounts/plugins/ftp.php

%post
logger -p local6.notice -t installer 'app-ftp-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/ftp_plugin/deploy/install ] && /usr/clearos/apps/ftp_plugin/deploy/install
fi

[ -x /usr/clearos/apps/ftp_plugin/deploy/upgrade ] && /usr/clearos/apps/ftp_plugin/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ftp-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/ftp_plugin/deploy/uninstall ] && /usr/clearos/apps/ftp_plugin/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
%exclude /usr/clearos/apps/ftp_plugin/packaging
%exclude /usr/clearos/apps/ftp_plugin/tests
%dir /usr/clearos/apps/ftp_plugin
/usr/clearos/apps/ftp_plugin/deploy
/usr/clearos/apps/ftp_plugin/language
/usr/clearos/apps/ftp_plugin/libraries
/var/clearos/accounts/plugins/ftp.php
