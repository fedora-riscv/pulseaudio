%define drvver 0.9

Name:		pulseaudio
Summary: 	Improved Linux sound server
Version:	0.9.13
Release:	6%{?dist}
License:	GPLv2+
Group:		System Environment/Daemons
Source0:	http://0pointer.de/lennart/projects/pulseaudio/pulseaudio-%{version}.tar.gz
URL:		http://pulseaudio.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: tcp_wrappers-devel, libsamplerate-devel, libsndfile-devel
BuildRequires: liboil-devel, m4, libcap-devel, libtool-ltdl-devel, pkgconfig
BuildRequires: alsa-lib-devel, glib2-devel, avahi-devel, GConf2-devel
BuildRequires: lirc-devel, doxygen, jack-audio-connection-kit-devel
BuildRequires: hal-devel, libatomic_ops-devel, PolicyKit-devel bluez-libs-devel
BuildRequires: xmltoman
# Libtool is dragging in rpaths.  Fedora's libtool should get rid of the
# unneccessary ones.
BuildRequires: libtool
BuildRequires: libXt-devel, xorg-x11-proto-devel
BuildRequires: openssl-devel
BuildRequires: gdbm-devel
BuildRequires: speex-devel >= 1.2
BuildRequires: libasyncns-devel
BuildRequires: intltool
Requires:	%{name}-core-libs = %{version}-%{release}
Obsoletes:	pulseaudio-devel
Patch1: 0001-Initialize-exit_idle_time-to-1-instead-of-0-when-i.patch
Patch2: 0002-Unload-module-bluetooth-device-if-the-remote-device.patch
Patch3: 0003-instead-of-resetting-virtual_volume-unconditionally.patch
Patch4: 0004-use-pa_channel_map_init_extend-instead-of-pa_chann.patch
Patch5: 0005-if-the-channel-map-was-modified-due-to-PA_SINK_INPUT.patch
Patch6: 0006-define-0dB-in-PA-as-maximum-amplification.patch
Patch7: 0007-Fix-a-potential-C-C99-ism-add-a-log-message-on-er.patch
Patch8: 0008-Fix-two-typos-that-broke-tunnels.patch
Patch9: 0009-properly-remove-dbus-matches-an-filters-when-unloadi.patch
Patch10: 0010-Fix-possible-invalid-read-while-attempting-to-load-m.patch
Patch11: 0011-always-check-for-libtool-prefix-binary-name-to-avoid.patch
Patch12: 0012-Fix-spelling-of-privilige.patch
Patch13: 0013-Make-missing-git-changelog.perl-non-fatal.patch
Patch14: 0014-fix-invalid-validity-check.patch
Patch15: 0015-convert-argument-to-boolean-int-in-PA_UNLIKELY-too.patch
Patch16: 0016-include-log.h-near-the-end-so-that-macro.h-can-be-in.patch
Patch17: 0017-Try-to-catch-certain-driver-errors.patch
Patch18: 0018-make-the-debug-trap-macro-a-proper-macro-in-macro.h.patch
Patch19: 0019-don-t-set-the-volume-of-pacat-unless-it-is-explicitl.patch
Patch20: 0020-warn-if-ALSA-wakes-us-up-and-there-is-actually-nothi.patch
Patch21: 0021-fix-build.patch
Patch22: 0022-make-sure-to-use-64bit-rounding-even-on-32bit-machin.patch
Patch23: 0023-make-shm-marker-architecture-independant-patch-from.patch
Patch24: 0024-Make-sure-libpulse-never-gets-unloaded.patch

%description
PulseAudio is a sound server for Linux and other Unix like operating 
systems. It is intended to be an improved drop-in replacement for the 
Enlightened Sound Daemon (ESOUND).

%package esound-compat
Summary:	PulseAudio EsounD daemon compatibility script
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}
Provides:	esound
Obsoletes:      esound

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
Requires:	%{name}-utils = %{version}-%{release}

%description module-x11
X11 bell and security modules for the PulseAudio sound server.

%package module-zeroconf
Summary:	Zeroconf support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}
Requires: 	pulseaudio-utils

%description module-zeroconf
Zeroconf publishing module for the PulseAudio sound server.

%package module-bluetooth
Summary:	Bluetooth proximity support for the PulseAudio sound server
Group:		System Environment/Daemons
Requires:	%{name} = %{version}-%{release}

%description module-bluetooth
Contains a module that can be used to automatically turn down the volume if
a bluetooth mobile phone leaves the proximity or turn it up again if it enters the
proximity again

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

%package libs
Summary:	Libraries for PulseAudio clients
License:	LGPLv2+
Group:		System Environment/Libraries
Provides:	pulseaudio-lib
Obsoletes:      pulseaudio-lib

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package core-libs
Summary:        Core libraries for the PulseAudio sound server.
License:	LGPLv2+
Group:		System Environment/Libraries

%description core-libs
This package contains runtime libraries that are used internally in the
PulseAudio sound server.

%package libs-glib2
Summary:	GLIB 2.x bindings for PulseAudio clients
License:	LGPLv2+
Group:		System Environment/Libraries
Provides:	pulseaudio-lib-glib2
Obsoletes:      pulseaudio-lib-glib2

%description libs-glib2
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package libs-zeroconf
Summary:    Zeroconf support for PulseAudio clients
License:	LGPLv2+
Group:      System Environment/Libraries
Provides:	pulseaudio-lib-zeroconf
Obsoletes:      pulseaudio-lib-zeroconf

%description libs-zeroconf
This package contains the runtime libraries and tools that allow PulseAudio
clients to automatically detect PulseAudio servers using Zeroconf.

%package libs-devel
Summary:	Headers and libraries for PulseAudio client development
License:	LGPLv2+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-libs-glib2 = %{version}-%{release}
Requires:	%{name}-libs-zeroconf = %{version}-%{release}
Requires:   pkgconfig glib2-devel
Provides:	pulseaudio-lib-devel
Obsoletes:      pulseaudio-lib-devel

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package utils
Summary:	PulseAudio sound server utilities
License:	LGPLv2+
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}

%description utils
This package contains command line utilities for the PulseAudio sound server.

%prep
%setup -q -T -b0
%patch1 -p1 -b .0001-Initialize-exit_idle_time-to-1-instead-of-0-when-i.patch
%patch2 -p1 -b .0002-Unload-module-bluetooth-device-if-the-remote-device.patch
%patch3 -p1 -b .0003-instead-of-resetting-virtual_volume-unconditionally.patch
%patch4 -p1 -b .0004-use-pa_channel_map_init_extend-instead-of-pa_chann.patch
%patch5 -p1 -b .0005-if-the-channel-map-was-modified-due-to-PA_SINK_INPUT.patch
%patch6 -p1 -b .0006-define-0dB-in-PA-as-maximum-amplification.patch
%patch7 -p1 -b .0007-Fix-a-potential-C-C99-ism-add-a-log-message-on-er.patch
%patch8 -p1 -b .0008-Fix-two-typos-that-broke-tunnels.patch
%patch9 -p1 -b .0009-properly-remove-dbus-matches-an-filters-when-unloadi.patch
%patch10 -p1 -b .0010-Fix-possible-invalid-read-while-attempting-to-load-m.patch
%patch11 -p1 -b .0011-always-check-for-libtool-prefix-binary-name-to-avoid.patch
%patch12 -p1 -b .0012-Fix-spelling-of-privilige.patch
%patch13 -p1 -b .0013-Make-missing-git-changelog.perl-non-fatal.patch
%patch14 -p1 -b .0014-fix-invalid-validity-check.patch
%patch15 -p1 -b .0015-convert-argument-to-boolean-int-in-PA_UNLIKELY-too.patch
%patch16 -p1 -b .0016-include-log.h-near-the-end-so-that-macro.h-can-be-in.patch
%patch17 -p1 -b .0017-Try-to-catch-certain-driver-errors.patch
%patch18 -p1 -b .0018-make-the-debug-trap-macro-a-proper-macro-in-macro.h.patch
%patch19 -p1 -b .0019-don-t-set-the-volume-of-pacat-unless-it-is-explicitl.patch
%patch20 -p1 -b .0020-warn-if-ALSA-wakes-us-up-and-there-is-actually-nothi.patch
%patch21 -p1 -b .0021-fix-build.patch
%patch22 -p1 -b .0022-make-sure-to-use-64bit-rounding-even-on-32bit-machin.patch
%patch23 -p1 -b .0023-make-shm-marker-architecture-independant-patch-from.patch
%patch24 -p1 -b .0024-Make-sure-libpulse-never-gets-unloaded.patch

%build
CFLAGS="-ggdb" %configure --disable-ltdl-install --disable-static --disable-rpath --with-system-user=pulse --with-system-group=pulse --with-realtime-group=pulse-rt --with-access-group=pulse-access
make LIBTOOL=/usr/bin/libtool #%{?_smp_mflags}
make doxygen

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/pulse-%{drvver}/modules/*.la
# configure --disable-static had no effect; delete manually.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
chmod 755 $RPM_BUILD_ROOT%{_bindir}/pulseaudio
rm $RPM_BUILD_ROOT/%{_libdir}/libpulsecore.so
# preserve time stamps, for multilib's sake
touch -r src/daemon/daemon.conf.in $RPM_BUILD_ROOT%{_sysconfdir}/pulse/daemon.conf
touch -r src/daemon/default.pa.in $RPM_BUILD_ROOT%{_sysconfdir}/pulse/default.pa
touch -r src/daemon/org.pulseaudio.policy $RPM_BUILD_ROOT%{_datadir}/PolicyKit/policy/org.pulseaudio.policy
touch -r man/pulseaudio.1.xml.in $RPM_BUILD_ROOT%{_mandir}/man1/pulseaudio.1
touch -r man/default.pa.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/default.pa.5
touch -r man/pulse-client.conf.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/pulse-client.conf.5
touch -r man/pulse-daemon.conf.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/pulse-daemon.conf.5
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/pulse

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
groupadd -r pulse &>/dev/null || :
useradd -r -c 'PulseAudio System Daemon' -s /sbin/nologin -d /var/run/pulse -g pulse pulse &>/dev/null || :
groupadd -r pulse-rt &>/dev/null || :
groupadd -r pulse-access &>/dev/null || :

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post libs-glib2 -p /sbin/ldconfig
%postun libs-glib2 -p /sbin/ldconfig

%post libs-zeroconf -p /sbin/ldconfig
%postun libs-zeroconf -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%attr(4755,root,root) %{_bindir}/pulseaudio
%dir %{_libdir}/pulse-%{drvver}/
%dir %{_libdir}/pulse-%{drvver}/modules/
%{_libdir}/pulse-%{drvver}/modules/libalsa-util.so
%{_libdir}/pulse-%{drvver}/modules/libauthkey.so
%{_libdir}/pulse-%{drvver}/modules/libauth-cookie.so
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
%{_libdir}/pulse-%{drvver}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{drvver}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-device-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-stream-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-remap-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-always-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-console-kit.so
%{_libdir}/pulse-%{drvver}/modules/module-position-event-sounds.so
%{_datadir}/PolicyKit/policy/org.pulseaudio.policy
%{_mandir}/man1/pulseaudio.1.gz
%{_mandir}/man5/default.pa.5.gz
%{_mandir}/man5/pulse-client.conf.5.gz
%{_mandir}/man5/pulse-daemon.conf.5.gz
%dir %{_libexecdir}/pulse
%attr(0700, pulse, pulse) %dir %{_localstatedir}/lib/pulse

%files esound-compat
%defattr(-,root,root)
%{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1.gz

%files module-lirc
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-lirc.so

%files module-x11
%defattr(-,root,root)
%config %{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulse-%{drvver}/modules/libx11prop.so
%{_libdir}/pulse-%{drvver}/modules/libx11wrap.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-bell.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-publish.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-xsmp.so

%files module-zeroconf
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/libavahi-wrap.so
%{_libdir}/pulse-%{drvver}/modules/module-zeroconf-publish.so
%{_libdir}/pulse-%{drvver}/modules/module-zeroconf-discover.so

%files module-jack
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-jack-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-jack-source.so

%files module-bluetooth
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-bluetooth-proximity.so
%{_libdir}/pulse-%{drvver}/modules/module-bluetooth-device.so
%{_libdir}/pulse-%{drvver}/modules/module-bluetooth-discover.so
%{_libdir}/pulse-%{drvver}/modules/libbluetooth-ipc.so
%{_libdir}/pulse-%{drvver}/modules/libbluetooth-sbc.so
%{_libexecdir}/pulse/proximity-helper

%files module-gconf
%defattr(-,root,root)
%{_libdir}/pulse-%{drvver}/modules/module-gconf.so
%{_libexecdir}/pulse/gconf-helper

%files libs -f %{name}.lang
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.*
%{_libdir}/libpulse-simple.so.*

%files core-libs
%defattr(-,root,root)
%{_libdir}/libpulsecore.so.*

%files libs-glib2
%defattr(-,root,root)
%{_libdir}/libpulse-mainloop-glib.so.*

%files libs-zeroconf
%defattr(-,root,root)
%{_bindir}/pabrowse
%{_libdir}/libpulse-browse.so.*
%{_mandir}/man1/pabrowse.1.gz

%files libs-devel
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
%{_bindir}/pasuspender
%{_libdir}/libpulsedsp.so
%{_mandir}/man1/pabrowse.1.gz
%{_mandir}/man1/pacat.1.gz
%{_mandir}/man1/pacmd.1.gz
%{_mandir}/man1/pactl.1.gz
%{_mandir}/man1/paplay.1.gz
%{_mandir}/man1/pasuspender.1.gz
%{_mandir}/man1/padsp.1.gz
%{_mandir}/man1/pax11publish.1.gz

%changelog
* Sat Nov 1 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-6
- Backport another two fixes from current git master

* Tue Oct 28 2008 Matthias Clasen <mclasen@redhat.com> 0.9.13-5
- Require new enough speex-devel

* Fri Oct 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-4
- Backport another fix from current git master

* Thu Oct 23 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-3
- Backport a couple of fixes from current git master

* Thu Oct 9 2008 Matthhias Clasen <mclasen@redhat.com> 0.9.13-2
- Handle locales properly

* Mon Oct 6 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-1
- New release

* Mon Sep 15 2008 Matthias Clasen <mclasen@redhat.com> 0.9.12-6
- Survive a missing ~/.pulse (#462407)

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.9.12-5
- Rebuild

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-4
- Ship /var/lib/pulse in the RPM

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-3
- Don't remove pulse users/groups on package removal

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-2
- Add intltool to deps

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-1
- Release 0.9.12

* Thu Jul 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-1
- Final release 0.9.11

* Tue Jul 22 2008 Jon McCann <jmccann@redhat.com> 0.9.11-0.7.git20080626
- Fix for CK API changes

* Thu Jun 26 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.6.git20080626
- New GIT snapshot

* Sun Jun 22 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.5.svn20080622
- New GIT snapshot

* Wed Jun 18 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.4.svn20080618
- New SVN snapshot

* Thu May 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.3.svn20080529
- Fix snapshot versioning

* Thu May 29 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.0.svn20080529
- New SVN snapshot

* Tue May 20 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.2.svn20080516
- Actually apply the patch

* Sat May 17 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.1.svn20080516
- Fix a wrong assertion in module-default-device-restore

* Fri May 16 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.0.svn20080516
- Update to an svn snapshot of the 'glitch-free' rewrite of pulseaudio

* Sun Mar 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.10-1
- Update to PulseAudio 0.9.10
- drop all patches, since they have been integrated upstream

* Thu Mar 27 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-13
- Abort on CPU time comsumption, so we can get core

* Thu Mar 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-12
- Own /usr/libexec/pulse (#437228)

* Wed Mar 12 2008 Adam Jackson <ajax@redhat.com> 0.9.8-11
- pulseaudio-0.9.8-disable-realtime.patch: Don't ask PolicyKit for increased
  scheduling mojo for now.  It's not clear that it's a win; and if it is,
  the policy should just be fixed to always allow it.

* Wed Mar 12 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-10
- Build the manual pages with xmltoman

* Fri Feb 29 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-9
- Fix the fix.

* Fri Feb 29 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-8
- Fix multilib issue (#228383)
- Prevent dumping core if exiting sooner that ltdl initializaion (#427962)

* Thu Feb 21 2008 Adam Tkac <atkac redhat com> 0.9.8-7
- really rebuild against new libcap

* Sun Feb 17 2008 Adam Tkac <atkac redhat com> 0.9.8-6
- rebuild against new libcap

* Wed Jan 23 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-5
- Fix CVE-2008-0008 security issue (#425481)

* Sun Jan 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-4.1
- Actually add content to pulseaudio-0.9.8-create-dot-pulse.patch
- Make the Source0 tag point to URL instead of a local file
- Drop the nochown patch; it's not applied at all and no longer needed

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-4
- add missing dependency on pulseaudio-utils for pulseaudio-module-x11

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-3
- Create ~/.pulse/ if not existant

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-2
- Add missing dependency on jack-audio-connection-kit-devel

* Wed Nov 28 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-1
- Upgrade to current upstream

* Wed Oct 17 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.16.svn20071017
- Another SVN snapshot, fixing another round of bugs (#330541)
- Split libpulscore into a seperate package to work around multilib limitation (#335011)

* Mon Oct 1 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.15.svn20071001
- Another SVN snapshot, fixing another round of bugs

* Sat Sep 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.14.svn20070929
- Another SVN snapshot, fixing a couple of subtle bugs

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.13.svn20070925
- Remove libpulsecore.so symlink from pulseaudio-libs-devel to avoid multilib issues

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.12.svn20070925
- New SVN snapshot
- Split off libflashsupport again
- Rename "-lib" packages to "-libs", like all other packages do it.
- Provide esound

* Fri Sep 7 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.11.svn20070907
- Update SVN snapshot, don't link libpulsecore.so statically anymore

* Wed Sep 5 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.10.svn20070905
- Update SVN snapshot

* Tue Sep 4 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.9.svn20070904
- Update SVN snapshot
- ship libflashsupport in our package
- drop pulseaudio-devel since libpulsecore is not linked statically

* Thu Aug 23 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.8.svn20070823
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.7.svn20070816
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.6.svn20070816
- Update SVN snapshot

* Tue Aug 14 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.5.svn20070814
- Forgot to upload tarball

* Tue Aug 14 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.4.svn20070814
- Update snapshot. Install file into /etc/xdg/autostart/ to load module-x11-smp 
  only after login

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.3.svn20070812
- Depend on tcp_wrappers-devel instead of tcp_wrappers, to make sure we
  actually get the headers installed.

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.2.svn20070812
- Update snapshot, contains 64 bit build fixes, and disables module-x11-xsmp by
  default to avoid deadlock when PA is started from gnome-session

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.1.svn20070812
- Take snapshot from SVN

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
