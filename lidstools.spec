Summary:	LIDS administration utility
Summary(pl.UTF-8):	Narzędzie do administrowania LIDS
Name:		lidstools
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.lids.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	9510dbdfbff718d88bf556b678a2ad3b
URL:		http://www.lids.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-static
Obsoletes:	lidsadm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
lidsadm is a utility to administer the Linux Intrusion Detection
System offered by the Linux kernel with lids patch.

%description -l pl.UTF-8
lidsadm to narzędzie do administrowania LIDS (Linux Intrusion
Detestion System) dostępnym w jądrze Linuksa z łatą lids.

%prep
%setup -q

%build
# Ehhh...
mv example/example/* example
mv doc/doc/doc/doc/* doc

%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README doc/FAQ
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%attr(700,root,root) %dir %{_sysconfdir}/lids
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lids/*
