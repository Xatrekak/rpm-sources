%global commit 160502771054d31d2f4c2fa46ad42c96336f3a74
%global shortcommit 1605027

Name:           ryzenadj
Version:        0.13.0
Release:        2.%{shortcommit}%{?dist}
Summary:        Power management settings for Ryzen APU

License:        LGPL
URL:            https://github.com/FlyGoat/RyzenAdj
Source0:	https://github.com/FlyGoat/RyzenAdj/archive/%{commit}.tar.gz

BuildRequires:  pciutils-devel
BuildRequires:  cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++

%global debug_package %{nil}

%description
Adjust power management settings for Mobile Raven Ridge Ryzen Processors.

%package devel
Summary:	Power management settings for Ryzen APU
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains necessary header files for RyzenAdj Development.

%prep
%autosetup -n RyzenAdj-%{commit}


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
install -Dsm 755 %{_builddir}/RyzenAdj-%{commit}/%__cmake_builddir/ryzenadj %{buildroot}/%{_bindir}/ryzenadj
install -Dsm 744 %{_builddir}/RyzenAdj-%{commit}/%__cmake_builddir/libryzenadj.so %{buildroot}/%{_libdir}/libryzenadj.so
install -Dm 744 %{_builddir}/RyzenAdj-%{commit}/lib/ryzenadj.h %{buildroot}/%{_includedir}/ryzenadj.h

%files
%{_bindir}/ryzenadj
%{_libdir}/libryzenadj.so

%files devel
%{_includedir}/ryzenadj.h


%changelog
* Fri Jun 03 2022 Sukhmeet Singh 0.10.0.1
- Initial Build

