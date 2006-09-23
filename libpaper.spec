Name:		libpaper
Version:	1.1.20
Release:	2%{?dist}
Summary:	Library and tools for handling papersize
Group:		System Environment/Libraries
License:	GPL
URL:		http://packages.qa.debian.org/libp/libpaper.html
Source0:	http://ftp.debian.org/debian/pool/main/libp/libpaper/%{name}_%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	automake

%description
The paper library and accompanying files are intended to provide a 
simple way for applications to take actions based on a system- or 
user-specified paper size. This release is quite minimal, its purpose 
being to provide really basic functions (obtaining the system paper name 
and getting the height and width of a given kind of paper) that 
applications can immediately integrate.

%package devel
Summary:	Headers/Libraries for developing programs that use libpaper
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains headers and libraries that programmers will need 
to develop applications which use libpaper.

%prep
%setup -q

%build
touch NEWS AUTHORS
automake -a
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
# letter is a sane default
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
echo "letter" > $RPM_BUILD_ROOT%{_sysconfdir}/papersize

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc COPYING ChangeLog README
%config(noreplace) %{_sysconfdir}/papersize
%{_bindir}/paperconf
%{_libdir}/libpaper.so.*
%{_sbindir}/paperconfig
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(-, root, root, -)
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%changelog
* Sat Sep 23 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.20-2
- nuke static lib
- own /etc/papersize
- fix mixed spaces/tabs rpmlint warning

* Sat Sep 23 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.20-1
- initial package for Fedora Extras
