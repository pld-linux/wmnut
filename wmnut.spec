Summary:	Dockable UPS Monitor
Summary(pl.UTF-8):	Dokowalny monitor UPS-ów
Name:		wmnut
Version:	0.60
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://wmnut.tuxfamily.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	b37429c06fc4e5b80fc668a5f1401f74
Patch0:		%{name}-ksh.patch
URL:		http://wmnut.tuxfamily.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	nut-devel >= 1.4.0-1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMNUT is an UPS/Battery Monitor. It is used to visually display and
interpret details of UPS/Battery status via NUT - Network UPS Tools
framework. WMNUT is dockable using WindowMaker and AfterStep window
managers.

%description -l pl.UTF-8
WMNUT jest monitorem stanu UPS-a i baterii. Służy do wizualnego
pokazywania i interpretacji szczegółów stanu UPS-ów i baterii poprzez
NUT - sieciowe narzędzia do UPS-ów. WMNUT jest dokowalny pod kontrolą
Window Makera lub AfterStepa.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-nut-libs=/usr/lib \
	--with-nut-includes=/usr/include/nut

%{__make} \
	LIBS="-lssl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install wmnutrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wmnutrc
