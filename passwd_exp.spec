Summary:	password expiration email notifier
Name:		passwd_exp
Version:	1.2.9
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://devel.dob.sk/passwd_exp/%{name}-%{version}b.tar.gz
# Source0-md5:	48eb2435cde93286cc05d3bfd20743c3
Patch0:		%{name}-DESTDIR.patch
URL:		http://devel.dob.sk/passwd_exp/
BuildRequires:	perl-Text-Tokenizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
passwd_exp notifies users of password or account expiration via email.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-sendmail=/usr/lib/sendmail \
	--with-mail=/bin/mail \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/passwd_exp
%dir %{_sysconfdir}/passwd_exp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/passwd_exp/passwd_exp.conf
%{_mandir}/man1/passwd_exp.1*
%dir %{_datadir}/passwd_exp
%dir %{_datadir}/passwd_exp/mod
%{_datadir}/passwd_exp/mod/_shell.reader
%{_datadir}/passwd_exp/mod/_termcap.reader
%{_datadir}/passwd_exp/mod/passwd.bsd
%{_datadir}/passwd_exp/mod/passwd.bsd.info
%{_datadir}/passwd_exp/mod/shadow.linux
%{_datadir}/passwd_exp/mod/shadow.linux.info
%{_datadir}/passwd_exp/mod/vmail.pfadmin
%{_datadir}/passwd_exp/mod/vmail.pfadmin.info
%{_datadir}/passwd_exp/passwd_exp-admin.cron
%{_datadir}/passwd_exp/passwd_exp.cron