# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/bin/ssh; \

%define selinux_policyver 38.1.23-1

Name:   ssh_daemon_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module to run ssh as a daemon

Group:	System Environment/Base
License:	GPLv2+
# This is an example. You will need to change it.
# For a complete guide on packaging your policy
# see https://fedoraproject.org/wiki/SELinux/IndependentPolicy
URL:		https://github.com/Mine02C4/ssh_daemon_selinux
Source0:	ssh_daemon.pp
Source1:	ssh_daemon.if


Requires: policycoreutils-python-utils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for ssh_daemon.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/ssh_daemon.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r ssh_daemon
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/ssh_daemon.pp
%{_datadir}/selinux/devel/include/contrib/ssh_daemon.if


%changelog
* Sat Apr 13 2024 NIWA Naoya <mine@mine02c4.nagoya> 1.0-1
- Initial version

