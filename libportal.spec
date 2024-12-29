%define major 1
%define libname %mklibname portal %{major}
%define girname %mklibname portal-gir %{major}
%define devname %mklibname -d portal

Name: libportal
Version: 0.9.0
Release: 1
Source0: https://github.com/flatpak/libportal/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Async API for most Flatpak portals
URL: https://github.com/flatpak/libportal
License: GPL
Group: System/Libraries
BuildRequires: meson ninja
BuildRequires: xmlto
BuildRequires: systemd-macros
BuildRequires: qt5-devel
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(gi-docgen)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(vapigen)
BuildRequires: gtk-doc

%description
Async API for most Flatpak portals

%package -n %{libname}
Summary:	Async API for most Flatpak portals
Group:		System/Libraries

%description -n %{libname}
Async API for most Flatpak portals

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
Async API for most Flatpak portals

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libportal.so.%{major}*
%{_libdir}/libportal-*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Xdp-1.0.typelib
%{_libdir}/girepository-1.0/XdpGtk3-1.0.typelib
%{_libdir}/girepository-1.0/XdpGtk4-1.0.typelib

%files -n %{devname}
%{_includedir}/libportal*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libportal.pc
%{_libdir}/pkgconfig/libportal-gtk3.pc
%{_libdir}/pkgconfig/libportal-gtk4.pc
%{_libdir}/pkgconfig/libportal-qt5.pc
%{_libdir}/pkgconfig/libportal-qt6.pc
%{_datadir}/gir-1.0/Xdp-1.0.gir
%{_datadir}/gir-1.0/XdpGtk3-1.0.gir
%{_datadir}/gir-1.0/XdpGtk4-1.0.gir
%{_datadir}/vala/vapi/libportal*
%doc %{_datadir}/doc/libportal-1/
