Summary:	LIDS administration utility
Summary(pl):	Narzêdzie do administrowania LIDS
Name:		lidstools
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.lids.org/download/%{name}-%{version}.tar.gz
URL:		http://www.lids.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-static
Obsoletes:	lidsasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
lidsadm is a utility to administer the Linux Intrusion Detection
System offered by the Linux kernel with lids patch.

%description -l pl
lidsadm to narzêdzie do administrowania LIDS (Linux Intrusion
Detestion System) dostêpnym w j±drze Linuksa z ³at± lids.

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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog INSTALL NEWS README doc/FAQ
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%attr(700,root,root) %dir %{_sysconfdir}/lids
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lids/*
