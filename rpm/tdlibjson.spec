Name: tdlibjson
Summary: Cross-platform library for building Telegram clients
Version:    1.3.0
Release: 1
Group:   Development/Libraries
License: BSL-1.0
URL:     https://github.com/blacksailer/td
Source0: tdlibjson.tar.gz
BuildRequires: cmake >= 3.1
BuildRequires: gperf
BuildRequires: openssl-devel


Provides: tdjson

%description
%{summary}.

%package devel
Summary:    Development files for Telegram TD library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q

%build

%define cmake_build %__cmake --build .
%define cmake_install make DESTDIR=%{?buildroot} install

SOURCE_DIR=`pwd`

mkdir -p %{_builddir}/build
cd %{_builddir}/build

%cmake \
-DCMAKE_BUILD_TYPE=Release $SOURCE_DIR

make

%install
cd %{_builddir}/build
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libtdjson.so
%{_libdir}/libtdjson.so.1
%{_libdir}/libtdjson.so.1.2.0

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/td
%dir %{_includedir}/td/telegram
%{_includedir}/td/telegram/td_api.h
%{_includedir}/td/telegram/td_json_client.h
%{_includedir}/td/telegram/td_log.h
%{_includedir}/td/telegram/tdjson_export.h
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/tdlibjson.pc
