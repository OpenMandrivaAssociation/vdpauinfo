
%define name	vdpauinfo
%define version	0.0.6
%define snap	20090221
%define rel	1

Summary:	VDPAU acceleration information utility
Name:		%{name}
Version:	%{version}
%if %snap
Release:	%mkrel 0.%snap.%rel
%else
Release:	%mkrel %rel
%endif
License:	MIT
Group:		Development/X11
URL:		http://www.nvnews.net/vbulletin/showthread.php?t=124978
# rm -rf vdpauinfo && git clone git://anongit.freedesktop.org/~aplattner/vdpauinfo && cd vdpauinfo/
# git archive --prefix=vdpauinfo-$(date +%Y%m%d)/ --format=tar HEAD | lzma > ../vdpauinfo-$(date +%Y%m%d).tar.lzma
Source:		vdpauinfo-%{snap}.tar.lzma
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	vdpau-devel >= 0.1
BuildRequires:	libx11-devel
BuildRequires:	python
Obsoletes:	vdpinfo < 0.0.6

%description
Simple utility that queries and displays the VDPAU capabilities of
your X display and prints them in tabular format.

%prep
%setup -q -n %{name}-%snap

%build
python functions.py > VDPDeviceImpl.h
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE AUTHORS
%{_bindir}/%{name}

