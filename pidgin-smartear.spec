%define pidgin_version 2.2.1
%define release %mkrel 2
%define fversion 2.0.0-1

Summary:	Pidgin plugin to assign a different sound to each buddy
Name:		pidgin-smartear
Version:	2.0.0
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Networking/Instant messaging
URL:		http://somewhere.fscked.org/smartear/
Source:		http://somewhere.fscked.org/smartear/smartear-%{fversion}.tar.bz2
#gw add missing internal header
Patch: smartear-2.0.0-1-internal.patch
BuildRequires:	libtool
BuildRequires:	pidgin-devel >= %pidgin_version
Requires:	pidgin >= %pidgin_version
Provides: gaim-smartear
Obsoletes: gaim-smartear

%description
This is a plugin for Pidgin, an instant messanger.
With it, you can assign different sounds to play for different buddies
or whole groups of buddies. SmartEar allows you to opt to play sounds
when a buddy sends you an IM, signs on, returns from away or idle, or
any combination of these, so you'll know by the sound what the
important people are doing.

Author suggests turning off default gaim sound event before using this
plugin.

%prep
%setup -q -n smartear-%fversion
%patch -p1

%build
libtool --mode=compile gcc -DPURPLE_PLUGINS -DVERSION=\"%version\"  `pkg-config --cflags pidgin gtk+-2.0` $RPM_OPT_FLAGS -c smartear.c -o smartear.lo
libtool --mode=link    gcc `pkg-config --libs pidgin` $RPM_OPT_FLAGS -o smartear.la -rpath %{_libdir}/pidgin smartear.lo -module -avoid-version 

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/pidgin
libtool --mode=install /usr/bin/install smartear.la %{buildroot}%{_libdir}/pidgin/smartear.la

# remove files not bundled
rm -f %{buildroot}%{_libdir}/pidgin/*.{la,a}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/pidgin/smartear.so

