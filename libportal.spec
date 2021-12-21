%define major 0
%define libname %mklibname portal %{major}
%define devname %mklibname -d portal

Name: libportal
Version: 0.5
Release: 1
Source0: https://github.com/flatpak/libportal/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Async API for most Flatpak portals
URL: http://github.com/flatpak/libportal
License: GPL
Group: System/Libraries
BuildRequires: meson ninja
BuildRequires: xmlto
BuildRequires: systemd-macros
BuildRequires: qt5-devel
BuildRequires: pkgconfig(Qt5X11Extras)
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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

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

%files -n %{devname}
%{_includedir}/libportal
%{_libdir}/*.so
%{_libdir}/pkgconfig/libportal.pc
%doc %{_datadir}/gtk-doc/html/libportal
