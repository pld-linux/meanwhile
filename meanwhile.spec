#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Lotus Sametime library
Summary(pl.UTF-8):	Biblioteka Lotus Sametime
Name:		meanwhile
Version:	1.0.2
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/meanwhile/%{name}-%{version}.tar.gz
# Source0-md5:	bf4ced109a367b4c5d71fe63c043270e
Patch0:		%{name}-glib-includes.patch
Patch1:		%{name}-static-build.patch
URL:		http://meanwhile.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The heart of the Meanwhile Project is the Meanwhile library, providing
the basic Lotus Sametime session functionality along with the core
services: Presence Awareness, Instant Messaging, Multi-user
Conferencing, Preferences Storage, Identity Resolution, and File
Transfer. This extensible client interface allows additional services
to be added to a session at runtime, allowing for simple integration
of future service handlers such as the user directory and whiteboard
and screen-sharing.

%description -l pl.UTF-8
Sercem projektu Meanwhile jest biblioteka Meanwhile udostępniająca
podstawową funkcjonalność sesji Lotus Sametime wraz z głównymi
usługami: sprawdzaniem obecności, komunikatorem, konferencją
wieloużytkownikową, przechowywaniem ustawień, sprawdzaniem tożsamości
i przesyłaniem plików. Ten rozszerzalny interfejs kliencki umożliwia
dodawanie dodatkowych usług do sesji w czasie pracy, pozwalając na
prostą integrację obsługi przyszłych usług, takich jak katalog
użytkowników czy współdzielenie tablicy i ekranu.

%package devel
Summary:	Header files for meanwhile library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki meanwhile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0

%description devel
This is the package containing the header files for meanwhile.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki meanwhile.

%package static
Summary:	Static meanwhile library
Summary(pl.UTF-8):	Statyczna biblioteka meanwhile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static meanwhile library.

%description static -l pl.UTF-8
Statyczna biblioteka meanwhile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	%{__enable_disable static_libs static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmeanwhile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmeanwhile.so.1

%files devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-doc-%{version}
%attr(755,root,root) %{_libdir}/libmeanwhile.so
%{_libdir}/libmeanwhile.la
%{_includedir}/meanwhile
%{_pkgconfigdir}/meanwhile.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmeanwhile.a
%endif
