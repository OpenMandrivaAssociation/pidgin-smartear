%define	smartear_version 1.0.0
%define gaim_version 1.0.2
%define release 1mdk

%define gaim_epoch 1
%define req_gaim_version 1.0.0

Summary:	SmartEar plugin for gAIM
Name:		gaim-smartear
Version:	%{gaim_version}_%{smartear_version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Networking/Instant messaging
URL:		http://somewhere.fscked.org/smartear/
Source:		http://somewhere.fscked.org/smartear/smartear-%{smartear_version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gaim-devel >= %{gaim_epoch}:%{req_gaim_version}
Requires:	gaim >= %{gaim_epoch}:%{req_gaim_version}

%description
This is a plugin for GAIM, an instant messanger.
With it, you can assign different sounds to play for different buddies
or whole groups of buddies. SmartEar allows you to opt to play sounds
when a buddy sends you an IM, signs on, returns from away or idle, or
any combination of these, so you'll know by the sound what the
important people are doing.

Author suggests turning off default gaim sound event before using this
plugin.

%prep
%setup -q -n smartear-%{smartear_version}

%build
libtool --mode=compile gcc `pkg-config --cflags gaim gtk+-2.0` $RPM_OPT_FLAGS -c smartear.c -o smartear.lo
libtool --mode=link    gcc `pkg-config --libs gaim` $RPM_OPT_FLAGS -o smartear.la -rpath %{_libdir}/gaim smartear.lo -module -avoid-version 

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/gaim
libtool --mode=install /usr/bin/install smartear.la %{buildroot}%{_libdir}/gaim/smartear.la

# remove files not bundled
rm -f %{buildroot}%{_libdir}/gaim/*.{la,a}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gaim/smartear.so

