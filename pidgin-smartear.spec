%define pidgin_version 2.2.1
%define release 9
%define fversion 2.0.0-1

Summary:	Pidgin plugin to assign a different sound to each buddy
Name:		pidgin-smartear
Version:	2.0.0
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Networking/Instant messaging
URL:		https://somewhere.fscked.org/smartear/
Source:		http://somewhere.fscked.org/smartear/smartear-%{fversion}.tar.bz2
#gw add missing internal header
Patch: smartear-2.0.0-1-internal.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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



%changelog
* Fri Sep 16 2011 Götz Waschk <waschk@mandriva.org> 1:2.0.0-8mdv2012.0
+ Revision: 699960
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1:2.0.0-7mdv2011.0
+ Revision: 441851
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1:2.0.0-6mdv2009.1
+ Revision: 350207
- 2009.1 rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1:2.0.0-5mdv2009.0
+ Revision: 259038
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:2.0.0-4mdv2009.0
+ Revision: 246970
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1:2.0.0-2mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 1:2.0.0-2mdv2008.0
+ Revision: 95093
- rebuild for pidgin 2.2.1

  + Michael Scherer <misc@mandriva.org>
    - Improve summary

* Wed May 23 2007 Götz Waschk <waschk@mandriva.org> 1:2.0.0-1mdv2008.0
+ Revision: 30014
- fix buildrequires
- fix build with pidgin
- rename

