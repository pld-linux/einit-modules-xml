# TODO:
# - more pld like
# - split to module lib and default conf?
Summary:	Event-based init daemon - modules xml
Summary(pl.UTF-8):	Demon init oparty na zdarzeniach - moduły xml
Name:		einit-modules-xml
Version:	2.0.0.0
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	http://einit.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	7a40d4a529ee111e0d9a7b525da26c28
URL:		http://www.einit.org/
BuildRequires:	expat-devel
BuildRequires:	libnl-devel >= 1.0-0.pre6.3
BuildRequires:	ncurses-devel
BuildRequires:	einit-devel >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include
%define		_prefix	/

%description
eINIT modules xml.

%description -l pl.UTF-8
Moduły xml dla eINIT.

%prep
%setup -q

%build
export CFLAGS=-I%{_includedir}/ncurses
export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/einit/modules/,%{_sysconfdir}/einit/conf.d,%{_libdir}/einit/defaults/conf.d}

export CFLAGS=-I%{_includedir}/ncurses
export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons install \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{_sysconfdir}/einit/conf.d
%{_sysconfdir}/einit/conf.d/*.xml
%dir %{_libdir}/einit/defaults/conf.d
%{_libdir}/einit/defaults/conf.d/*.xml
%dir %{_libdir}/einit/modules-xml
%{_libdir}/einit/modules-xml/*.xml
%attr(755,root,root) %{_libdir}/einit/modules/module-xml.so
