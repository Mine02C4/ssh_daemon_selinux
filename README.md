# SELinux policy module to run ssh as a daemon

Installing this policy allows ssh (not sshd) to run as a daemon. This is useful, for example, when using a SOCKS Proxy with ssh as a daemon.

## Requirements

- Distribution : Rocky Linux 9

I believe it works in other environments as well. I would like information on confirmation that it works.

## Installation

### Step. 1 : Add DNF repository

Execute the following command as root

```sh
dnf config-manager --add-repo https://raw.githubusercontent.com/Mine02C4/ssh_daemon_selinux/main/repo/ssh_daemon_selinux.repo
```

If you want to import GPG keys in advance, execute the following command. (Optional)

```sh
rpm --import https://raw.githubusercontent.com/Mine02C4/ssh_daemon_selinux/main/signature/public.gpg
```

### Step. 2 : Install package

Execute the following command as root

```sh
dnf install ssh_daemon_selinux
```

If you run the command for the first time without importing the GPG key, the fingerprint of the GPG key will be confirmed. Please check if it matches the following.

```
Userid     : "NIWA Naoya (ssh_daemon_selinux) <mine@mine02c4.nagoya>"
Fingerprint: ABCB BA2A 5C19 7F24 1C6D  0AF5 4C2C 05FE 51E5 7A2F
From       : https://raw.githubusercontent.com/Mine02C4/ssh_daemon_selinux/main/signature/public.gpg
```
