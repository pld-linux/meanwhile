#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Lotus Sametime library
Summary(pl):	Biblioteka Lotus Sametime
Name:		meanwhile
Version:	1.0.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/meanwhile/%{name}-%{version}.tar.gz
# Source0-md5:	bf4ced109a367b4c5d71fe63c043270e
URL:		http://meanwhile.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
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

%description -l pl
Sercem projektu Meanwhile jest biblioteka Meanwhile udostêpniaj±ca
podstawow± funkcjonalno¶æ sesji Lotus Sametime wraz z g³ównymi
us³ugami: sprawdzaniem obecno¶ci, komunikatorem, konferencj±
wielou¿ytkownikow±, przechowywaniem ustawieñ, sprawdzaniem to¿samo¶ci
i przesy³aniem plików. Ten rozszerzalny interfejs kliencki umo¿liwia
dodawanie dodatkowych us³ug do sesji w czasie pracy, pozwalaj±c na
prost± integracjê obs³ugi przysz³ych us³ug, takich jak katalog
u¿ytkowników czy wspó³dzielenie tablicy i ekranu.

%package devel
Summary:	Header files for meanwhile library
Summary(pl):	Pliki nag³ówkowe biblioteki meanwhile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0

%description devel
This is the package containing the header files for meanwhile.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki meanwhile.

%package static
Summary:	Static meanwhile library
Summary(pl):	Statyczna biblioteka meanwhile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static meanwhile library.

%description static -l pl
Statyczna biblioteka meanwhile.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--%{!?with_static_libs:dis}%{?with_static_libs:en}able-static

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
