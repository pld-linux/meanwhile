#
%bcond_without	static_libs	# disable static libraries

Summary:	Lotus Sametime library
Name:		meanwhile
Version:	0.4.2
Release:	1
License:	GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Libraries
Source0:	http://dl.sourceforge.net/meanwhile/%{name}-%{version}.tar.gz
# Source0-md5:	-
URL:		http://meanwhile.sourceforge.net
BuildRequires:	glib-devel
BuildRequires:	pkgconfig
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The heart of the Meanwhile Project is the Meanwhile library, providing
the basic Lotus Sametime session functionality along with the core
services; Presence Awareness, Instant Messaging, Multi-user
Conferencing, Preferences Storage, Identity Resolution, and File
Transfer. This extensible client interface allows additional services
to be added to a session at runtime, allowing for simple integration
of future service handlers such as the user directory and whiteboard
and screen-sharing.

%package devel
Summary:	Development libraries and header files for meanwhile library
Group:		Development/Libraries
Requires:	pkgconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for meanwhile.

%package static
Summary:	Static meanwhile library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static meanwhile library.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--%{!?with_static_libs:dis}%{?with_static_libs:en}able-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmeanwhile.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmeanwhile.so
%{_libdir}/libmeanwhile.la
%{_includedir}/meanwhile
%{_pkgconfigdir}/meanwhile.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmeanwhile.a
%endif
