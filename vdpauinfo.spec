Summary:	VDPAU acceleration information utility
Name:		vdpauinfo
Version:	1.5
Release:	3
License:	MIT
Group:		Development/X11
URL:		https://gitlab.freedesktop.org/vdpau/vdpauinfo
Source0:	https://gitlab.freedesktop.org/vdpau/vdpauinfo/-/archive/%{version}/vdpauinfo-%{version}.tar.bz2
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(x11)

Recommends:	%{_lib}vdpau-driver-nouveau

%description
Simple utility that queries and displays the VDPAU capabilities of
your X display and prints them in tabular format.

%prep
%setup -q

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
