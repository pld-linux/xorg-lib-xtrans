# $Rev: 3233 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xtrans library
Summary(pl):	Biblioteka xtrans
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
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/xtrans-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xtrans library.

%description -l pl
Biblioteka xtrans.


%package devel
Summary:	xtrans library
Summary(pl):	Biblioteka xtrans
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
xtrans library

%description devel -l pl
Biblioteka xtrans


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
