# $Rev: 3233 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	xtrans library - network API translation layer
Summary(pl):	Biblioteka xtrans - warstwa t³umaczenia sieciowego API
Name:		xorg-lib-xtrans
Version:	0.99.0
Release:	0.04
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/xtrans-%{version}.tar.bz2
# Source0-md5:	ffd4ac956cd680da6e47e0703a91e4b8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/xtrans-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description -l pl
Biblioteka xtrans dostarcza warstwê t³umaczenia sieciowego API s³u¿±c±
do oddzielenia aplikacji i bibliotek X od kaprysów sieciowych systemu
operacyjnego.

%package devel
Summary:	xtrans library - network API translation layer
Summary(pl):	Biblioteka xtrans - warstwa t³umaczenia sieciowego API
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXtrans-devel

%description devel
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description devel -l pl
Biblioteka xtrans dostarcza warstwê t³umaczenia sieciowego API s³u¿±c±
do oddzielenia aplikacji i bibliotek X od kaprysów sieciowych systemu
operacyjnego.

%prep
%setup -q -n xtrans-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	aclocaldir=%{_aclocaldir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_includedir}/X11/Xtrans
%{_pkgconfigdir}/xtrans.pc
%{_aclocaldir}/xtrans.m4
