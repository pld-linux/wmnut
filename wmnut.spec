Summary:	Dockable UPS Monitor
Summary(pl):	Dokowalny monitor UPS-ów
Name:		wmnut
Version:	0.0.9
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://wmnut.tuxfamily.org/files/%{name}-%{version}.tar.bz2
URL:		http://wmnut.tuxfamily.org/
BuildRequires:	XFree86-devel
BuildRequires:	nut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
WMNUT is an UPS/Battery Monitor. It is used to visually display and
interpret details of UPS/Battery status via NUT - Network UPS Tools
framework. WMNUT is dockable using WindowMaker and AfterStep
window managers.

%description -l pl
WMNUT jest monitorem stanu UPS-a i baterii. S³u¿y do wizualnego
pokazywania i interpretacji szczegó³ów stanu UPS-ów i baterii poprzez
NUT - sieciowe narzêdzia do UPS-ów. WMNUT jest dokowalny pod kontrol±
Window Makera lub AfterStepa.

%prep
%setup -q

%build
%{__make} -C wmnut \
	CC="%{__cc}" CFLAGS="%{rpmcflags}" \
	OBJNUT=/usr/lib/upsfetch.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install wmnut/wmnut $RPM_BUILD_ROOT%{_bindir}
install wmnut/wmnut.1 $RPM_BUILD_ROOT%{_mandir}/man1
install wmnut/wmnutrc $RPM_BUILD_ROOT%{_sysconfdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wmnutrc
