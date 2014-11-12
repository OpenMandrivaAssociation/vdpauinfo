Summary:	VDPAU acceleration information utility
Name:		vdpauinfo
Version:	0.1
Release:	2
License:	MIT
Group:		Development/X11
URL:		http://freedesktop.org/wiki/Software/VDPAU
Source0:	http://people.freedesktop.org/~aplattner/vdpau/vdpauinfo-%{version}.tar.gz
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(x11)
Obsoletes:	vdpinfo < 0.0.6

%description
Simple utility that queries and displays the VDPAU capabilities of
your X display and prints them in tabular format.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS
%{_bindir}/%{name}
