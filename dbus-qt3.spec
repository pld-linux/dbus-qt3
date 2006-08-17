#
%define		rname		dbus-1-qt3
#
Summary:	Qt-based library for using D-BUS
Summary(pl):	Biblioteka do u¿ywania D-BUS oparta o Qt
Name:		dbus-qt3
Version:	0.2
Release:	2
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://www.sbox.tugraz.at/home/v/voyager/%{rname}-%{version}.tar.bz2
# Source0-md5:	574ec7c8e0c227498a4fbbd6b2255853
Patch0:		%{name}-configure.patch
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.91
BuildRequires:	qt-devel >= 6:3.1.0
Obsoletes:	dbus-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with the
Qt thread abstraction and main loop.

%description -l pl
Dodatkowa biblioteka D-BUS do integracji standardowej biblioteki D-BUS
z abstrakcj± w±tków i g³ówn± pêtl± Qt.

%package devel
Summary:	Header files for Qt-based library for using D-BUS
Summary(pl):	Pliki nag³ówkowe biblioteki do u¿ywania D-BUS opartej o Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.91
Obsoletes:	dbus-qt-devel

%description devel
Header files for Qt-based library for using D-BUS.

%description devel -l pl
Pliki nag³ówkowe biblioteki do u¿ywania D-BUS opartej o Qt.

%package static
Summary:	Static Qt-based library for using D-BUS
Summary(pl):	Statyczna biblioteka do u¿ywania D-BUS oparta o Qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	dbus-qt-static

%description static
Static Qt-based library for using D-BUS.

%description static -l pl
Statyczna biblioteka do u¿ywania D-BUS oparta o Qt.

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/libdbus-1-qt3.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-1-qt3.so
%{_libdir}/libdbus-1-qt3.la

%{_includedir}/dbus-1.0/qt3

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-1-qt3.a
