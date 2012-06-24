Summary:	xtrans library - network API translation layer
Summary(pl):	Biblioteka xtrans - warstwa t�umaczenia sieciowego API
Name:		xorg-lib-xtrans
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/xtrans-%{version}.tar.bz2
# Source0-md5:	da1628280f945e8d48a4c2e80ee28873
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description -l pl
Biblioteka xtrans dostarcza warstw� t�umaczenia sieciowego API s�u��c�
do oddzielenia aplikacji i bibliotek X od kaprys�w sieciowych systemu
operacyjnego.

%package devel
Summary:	xtrans library - network API translation layer
Summary(pl):	Biblioteka xtrans - warstwa t�umaczenia sieciowego API
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXtrans-devel

%description devel
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%description devel -l pl
Biblioteka xtrans dostarcza warstw� t�umaczenia sieciowego API s�u��c�
do oddzielenia aplikacji i bibliotek X od kaprys�w sieciowych systemu
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
%doc AUTHORS COPYING ChangeLog
%{_includedir}/X11/Xtrans
%{_pkgconfigdir}/xtrans.pc
%{_aclocaldir}/xtrans.m4
