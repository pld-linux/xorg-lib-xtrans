Summary:	xtrans library - network API translation layer
Summary(pl.UTF-8):	Biblioteka xtrans - warstwa tłumaczenia sieciowego API
Name:		xorg-lib-xtrans
Version:	1.2.5
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2
# Source0-md5:	2d1e57e82acc5f21797e92341415af2f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	groff
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description -l pl.UTF-8
Biblioteka xtrans dostarcza warstwę tłumaczenia sieciowego API służącą
do oddzielenia aplikacji i bibliotek X od kaprysów sieciowych systemu
operacyjnego.

%package devel
Summary:	xtrans library - network API translation layer
Summary(pl.UTF-8):	Biblioteka xtrans - warstwa tłumaczenia sieciowego API
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXtrans-devel

%description devel
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description devel -l pl.UTF-8
Biblioteka xtrans dostarcza warstwę tłumaczenia sieciowego API służącą
do oddzielenia aplikacji i bibliotek X od kaprysów sieciowych systemu
operacyjnego.

%prep
%setup -q -n xtrans-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-docs

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README Xtrans.html
%{_includedir}/X11/Xtrans
%{_npkgconfigdir}/xtrans.pc
%{_aclocaldir}/xtrans.m4
