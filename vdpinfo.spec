
%define name	vdpinfo
%define version	0.0.4
%define rel	1

Summary:	VDPAU acceleration information utility
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
License:	MIT
Group:		Development/X11
URL:		http://www.nvnews.net/vbulletin/showthread.php?t=124978
Source:		http://www.cs.rug.nl/~wladimir/vdpinfo/vdpinfo-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	vdpau-devel
BuildRequires:	libx11-devel
BuildRequires:	python

%description
Simple utility that queries and displays the VDPAU capabilities of
your X display and prints them in tabular format.

%prep
%setup -q -n %{name}
sed -i 's/^LDFLAGS=/LDFLAGS=%{ldflags} /' Makefile

%build
python functions.py > VDPDeviceImpl.h
%make CXXFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%{name}

