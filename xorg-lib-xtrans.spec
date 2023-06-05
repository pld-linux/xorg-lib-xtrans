Summary:	xtrans library - network API translation layer
Summary(pl.UTF-8):	Biblioteka xtrans - warstwa tłumaczenia sieciowego API
Name:		xorg-lib-xtrans
Version:	1.5.0
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.xz
# Source0-md5:	12344cd74a1eb25436ca6e6a2cf93097
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xz
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
Obsoletes:	libXtrans-devel < 0.2
BuildArch:	noarch

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
	--enable-docs \
	--without-fop

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# (.html version) packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/xtrans/xtrans.*

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md doc/xtrans.html
%{_includedir}/X11/Xtrans
%{_npkgconfigdir}/xtrans.pc
%{_aclocaldir}/xtrans.m4
