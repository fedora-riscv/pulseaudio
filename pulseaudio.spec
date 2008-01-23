%define drvver 0.9

Name:		pulseaudio
Summary: 	Improved Linux sound server
Version:	0.9.6
Release:	2%{?dist}.1
License:	GPL
Group:		System Environment/Daemons
Source0:	http://0pointer.de/lennart/projects/pulseaudio/pulseaudio-%{version}.tar.gz
URL:		http://pulseaudio.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: tcp_wrappers, libsamplerate-devel, libsndfile-devel
BuildRequires: liboil-devel, m4, libcap-devel, libtool-ltdl-devel, pkgconfig
BuildRequires: alsa-lib-devel, glib2-devel, avahi-devel GConf2-devel
BuildRequires: lirc-devel doxygen jack-audio-connection-kit-devel
BuildRequires: hal-devel libatomic_ops-devel
# Libtool is dragging in rpaths.  Fedora's libtool should get rid of the
# unneccessary ones.
BuildRequires: libtool
BuildRequires:	libXt-devel, xorg-x11-proto-devel

Patch1: 	pulseaudio-0.9.6-nochown.patch
Patch2: 	pulseaudio-0.9.6-droproot.patch

%description
PulseAudio is a sound server for Linux and other Unix like operating 
systems. It is intended to be an improved drop-in replacement for the 
Enlightened Sound Daemon (ESOUND).

%package esound-compat
Summary:	PulseAudio EsounD daemon compatibility script
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}
Conflicts:	esound

%description esound-compat
A compatibility script that allows applications to call /usr/bin/esd
and start PulseAudio with EsounD protocol modules.

%package module-lirc
Summary:	LIRC support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-lirc
LIRC volume control module for the PulseAudio sound server.

%package module-x11
Summary:	X11 support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-x11
X11 bell and security modules for the PulseAudio sound server.

%package module-zeroconf
Summary:	Zeroconf support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-zeroconf
Zeroconf publishing module for the PulseAudio sound server.

%package module-jack
Summary:	JACK support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-jack
JACK sink and source modules for the PulseAudio sound server.

%package module-gconf
Summary:	GConf support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-gconf
GConf configuration backend for the PulseAudio sound server.

%package devel
Summary:	Headers and libraries for PulseAudio server module development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-module-x11 = %{version}-%{release}
Requires:	%{name}-lib-devel = %{version}-%{release}

%description devel
Headers and libraries for developing modules for the PulseAudio sound server.

%package lib
Summary:	Libraries for PulseAudio clients
License:	LGPL
Group:		System Environment/Libraries

%description lib
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package lib-glib2
Summary:	GLIB 2.x bindings for PulseAudio clients
License:	LGPL
Group:		System Environment/Libraries

%description lib-glib2
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package lib-zeroconf
Summary:    Zeroconf support for PulseAudio clients
License:	LGPL
Group:      System Environment/Libraries

%description lib-zeroconf
This package contains the runtime libraries and tools that allow PulseAudio
clients to automatically detect PulseAudio servers using Zeroconf.

%package lib-devel
Summary:	Headers and libraries for PulseAudio client development
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-lib-glib2 = %{version}-%{release}
Requires:	%{name}-lib-zeroconf = %{version}-%{release}
Requires:   pkgconfig glib2-devel

%description lib-devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package utils
Summary:	PulseAudio sound server utilities
License:	LGPL
Group:		Applications/Multimedia
Requires:	%{name}-lib = %{version}-%{release}

%description utils
This package contains command line utilities for the PulseAudio sound server.

%prep
%setup -q 
%patch1 -p1
%patch2 -p1

%build
%configure --disable-ltdl-install --disable-static --disable-rpath --with-system-user=pulse --with-system-group=pulse --with-realtime-group=pulse-rt --with-access-group=pulse-access
make LIBTOOL=/usr/bin/libtool
make doxygen

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/pulse-%{drvver}/modules/*.la
# configure --disable-static had no effect; delete manually.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
chmod 755 $RPM_BUILD_ROOT%{_bindir}/pulseaudio

ln -s esdcompat $RPM_BUILD_ROOT%{_bindir}/esd

%clean
rm -rf $RPM_BUILD_ROOT

%pre
groupadd -r pulse &>/dev/null || :
useradd -r -c 'PulseAudio daemon' \
    -s /sbin/nologin -d / -g pulse pulse &>/dev/null || :
groupadd -r pulse-rt &>/dev/null || :
groupadd -r pulse-access &>/dev/null || :

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    userdel pulse &>/dev/null || :
    groupdel pulse &>/dev/null || :
    groupdel pulse-rt &>/dev/null || :
    groupdel pulse-access &>/dev/null || :
fi

%post lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%post lib-glib2 -p /sbin/ldconfig
%postun lib-glib2 -p /sbin/ldconfig

%post lib-zeroconf -p /sbin/ldconfig
%postun lib-zeroconf -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%attr(4755,root,root) %{_bindir}/pulseaudio
%{_libdir}/libpulsecore.so.*
%dir %{_libdir}/pulse-%{drvver}/
%dir %{_libdir}/pulse-%{drvver}/modules/
%{_libdir}/pulse-%{drvver}/modules/libalsa-util.so
%{_libdir}/pulse-%{drvver}/modules/libauthkey-prop.so
%{_libdir}/pulse-%{drvver}/modules/libauthkey.so
%{_libdir}/pulse-%{drvver}/modules/libcli.so
%{_libdir}/pulse-%{drvver}/modules/libdbus-util.so
%{_libdir}/pulse-%{drvver}/modules/libiochannel.so
%{_libdir}/pulse-%{drvver}/modules/libioline.so
%{_libdir}/pulse-%{drvver}/modules/libipacl.so
%{_libdir}/pulse-%{drvver}/modules/liboss-util.so
%{_libdir}/pulse-%{drvver}/modules/libpacket.so
%{_libdir}/pulse-%{drvver}/modules/libparseaddr.so
%{_libdir}/pulse-%{drvver}/modules/libpdispatch.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-http.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-native.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{drvver}/modules/libpstream-util.so
%{_libdir}/pulse-%{drvver}/modules/libpstream.so
%{_libdir}/pulse-%{drvver}/modules/librtp.so
%{_libdir}/pulse-%{drvver}/modules/libsocket-client.so
%{_libdir}/pulse-%{drvver}/modules/libsocket-server.so
%{_libdir}/pulse-%{drvver}/modules/libsocket-util.so
%{_libdir}/pulse-%{drvver}/modules/libstrlist.so
%{_libdir}/pulse-%{drvver}/modules/libtagstruct.so
%{_libdir}/pulse-%{drvver}/modules/module-alsa-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-alsa-source.so
%{_libdir}/pulse-%{drvver}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-cli.so
%{_libdir}/pulse-%{drvver}/modules/module-combine.so
%{_libdir}/pulse-%{drvver}/modules/module-detect.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-hal-detect.so
%{_libdir}/pulse-%{drvver}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-match.so
%{_libdir}/pulse-%{drvver}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-null-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-oss-mmap.so
%{_libdir}/pulse-%{drvver}/modules/module-oss.so
%{_libdir}/pulse-%{drvver}/modules/module-pipe-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-pipe-source.so
%{_libdir}/pulse-%{drvver}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{drvver}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{drvver}/modules/module-rtp-send.so
%{_libdir}/pulse-%{drvver}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-sine.so
%{_libdir}/pulse-%{drvver}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{drvver}/modules/module-volume-restore.so

%files esound-compat
%defattr(-,root,root)
%{_bindir}/esdcompat
%{_bindir}/esd

%files module-lirc
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-lirc.so

%files module-x11
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/libx11prop.so
%{_libdir}/pulse-%{drvver}/modules/libx11wrap.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-bell.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-publish.so

%files module-zeroconf
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/libavahi-wrap.so
%{_libdir}/pulse-%{drvver}/modules/module-zeroconf-publish.so

%files module-jack
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-jack-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-jack-source.so

%files module-gconf
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-gconf.so
%{_libexecdir}/pulse/gconf-helper

%files devel
%defattr(-,root,root)
%{_includedir}/pulsecore/
%{_libdir}/libpulsecore.so

%files lib
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.*
%{_libdir}/libpulse-simple.so.*

%files lib-glib2
%defattr(-,root,root)
%{_libdir}/libpulse-mainloop-glib.so.*

%files lib-zeroconf
%defattr(-,root,root)
%{_bindir}/pabrowse
%{_libdir}/libpulse-browse.so.*

%files lib-devel
%defattr(-,root,root)
%doc doxygen/html
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/libpulse-browse.so
%{_libdir}/pkgconfig/libpulse*.pc

%files utils
%defattr(-,root,root)
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pax11publish
%{_bindir}/padsp
%{_libdir}/libpulsedsp.so

%changelog
* Wed Jan 23 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.6-2.1
- Fix CVE-2008-0008 security issue (#425481)

* Tue May 29 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.6-2
- Add libatomic_ops-devel as a build requirement.

* Tue May 29 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.6-1
- Upgrade to 0.9.6.

* Sat Mar  2 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-5
- Fix merge problems with patch.

* Fri Mar  2 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-4
- Add patch to handle ALSA changing the frame size (bug 230211).
- Add patch for suspended ALSA devices (bug 228205).

* Mon Feb  5 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-3
- Add esound-compat subpackage that allows PulseAudio to be a drop-in
  replacement for esd (based on patch by Matthias Clasen).
- Backport patch allows startup to continue even when the users'
  config cannot be read.

* Wed Oct 23 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-2
- Create user and groups for daemon.

* Mon Aug 28 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-1
- Upgrade to 0.9.5.

* Wed Aug 23 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-3
- Make sure JACK modules are built and packaged.

* Tue Aug 22 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-2
- Merge the ALSA modules into the main package as ALSA is the
  standard API.

* Sun Aug 20 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-1
- Update to 0.9.4.
- Remove fix for rpath as it is merged upstream.

* Fri Jul 21 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.9.3-2
- Remove static libraries.
- Fix for rpath issues.

* Fri Jul 21 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.3-1
- Update to 0.9.3
- GLib 1.2 bindings dropped.
- Howl compat dropped as Avahi is supported natively.
- Added fix for pc files on x86_64.

* Sat Jul  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.2-1
- Update to 0.9.2.
- Added Avahi HOWL compat dependencies.

* Thu Jun  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.1-1
- Update to 0.9.1.

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-2
- Build and package doxygen docs
- Call ldconfig for relevant subpackages.

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-1
- Update to 0.9.0

* Tue May  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.8.1-1
- Update to 0.8.1
- Split into more packages
- Remove the modules' static libs as those shouldn't be used (they shouldn't
  even be installed)

* Fri Feb 24 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-2
- dance around with perms so we don't strip the binary
- add missing BR

* Mon Nov 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-1
- Initial package for Fedora Extras
