#
%define		rname		libdbus-1-qt3
#
Summary:	Qt-based library for using D-BUS
Summary(pl.UTF-8):	Biblioteka do używania D-BUS oparta o Qt
Name:		dbus-qt3
Version:	0.8.1
Release:	2
# AFL v2.1 or GPL v2+, but Qt license enforces GPL
License:	GPL v2+
Group:		Libraries
Source0:	http://people.freedesktop.org/~krake/dbus-1-qt3/%{rname}-%{version}.tar.bz2
# Source0-md5:	6308f50cfc715919c677fc10129421a0
Patch0:		%{name}-configure.patch
Patch1:		kde-ac260-lt.patch
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.6.1
BuildRequires:	dbus-devel >= 0.91
BuildRequires:	qt-devel >= 6:3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with the
Qt thread abstraction and main loop.

%description -l pl.UTF-8
Dodatkowa biblioteka D-BUS do integracji standardowej biblioteki D-BUS
z abstrakcją wątków i główną pętlą Qt.

%package devel
Summary:	Header files for Qt-based library for using D-BUS
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.91

%description devel
Header files for Qt-based library for using D-BUS.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt.

%package static
Summary:	Static Qt-based library for using D-BUS
Summary(pl.UTF-8):	Statyczna biblioteka do używania D-BUS oparta o Qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qt-based library for using D-BUS.

%description static -l pl.UTF-8
Statyczna biblioteka do używania D-BUS oparta o Qt.

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libdbus-1-qt3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbus-1-qt3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-1-qt3.so
%{_libdir}/libdbus-1-qt3.la
%{_includedir}/dbus-1.0/qt3
%{_pkgconfigdir}/dbus-1-qt3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-1-qt3.a
