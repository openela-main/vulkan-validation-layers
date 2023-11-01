Name:           vulkan-validation-layers
Version:        1.3.239.0
Release:        2%{?dist}
Summary:        Vulkan validation layers

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-ValidationLayers-sdk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  glslang-devel
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

Requires: spirv-tools-libs >= 2019.4-1.20191109
%description
Vulkan validation layers

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vulkan-headers

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n Vulkan-ValidationLayers-sdk-%{version}


%build
# Decrease debuginfo verbosity to reduce memory consumption even more
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')


%cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DGLSLANG_INSTALL_DIR=%{_prefix} \
        -DBUILD_LAYER_SUPPORT_FILES:BOOL=ON \
        -DUSE_ROBIN_HOOD_HASHING:BOOL=OFF \
        -DSPIRV_HEADERS_INCLUDE_DIR=%{_includedir} \
        -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/vulkan/ .
%ninja_build


%install
%ninja_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_datadir}/vulkan/explicit_layer.d/*.json
%{_libdir}/libVkLayer_*.so

%files devel
%{_includedir}/vulkan/
%{_libdir}/libVkLayer_utils.a

%changelog
* Wed Feb 15 2023 Dave Airlie <airlied@redhat.com> - 1.3.239.0-2
- Try and fix validation layer exports

* Tue Feb 14 2023 Dave Airlie <airlied@redhat.com> - 1.3.239.0-1
- Update to 1.3.239.0

* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 1.3.224.0-1
- Update to 1.3.224.0

* Mon Jun 20 2022 Dave Airlie <airlied@redhat.com> - 1.3.216.0-1
- Update to 1.3.216.0

* Tue Feb 22 2022 Dave Airlie <airlied@redhat.com> - 1.3.204.0-1
- Update to 1.3.204.0

* Mon Feb 01 2021 Dave Airlie <airlied@redhat.com> - 1.2.162.0-1
- Update to 1.2.162.0

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 1.2.131.1-1
- Update for 8.2.0 for vulkan 1.2

* Sat Dec 07 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-3
- Update for 8.2.0

* Fri Nov 29 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-2
- Add explicit spirv toos libs requires

* Wed Nov 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-1
- Update validation layers to 1.1.126.0

* Wed Jul 31 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-1
- Update validation layers to 1.1.114.0

* Wed Mar 06 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update valdiation layers to 1.1.101.0

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-3
- Workaround i686 build issue

* Tue Jun 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-2
- Exclude i686 due to 'virtual memory exhausted' FTBFS

* Sat Jun 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package
