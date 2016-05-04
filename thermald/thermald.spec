Name:       thermald
Summary:    The Linux Thermal Daemon program from 01.org
License:    GPLv2
Version: 1.5.3
Release:    1%{?dist}
Url:        https://01.org/linux-thermal-daemon
Source0:    %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libxml-2.0)
%{?systemd_requires}
BuildRequires: systemd


%description
Thermal Daemon is a Linux daemon for monitoring and controlling platform
temperatures. Once the system temperature reaches a certain threshold,
the Linux daemon activates various cooling methods to try to cool the system.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install

# Remove Upstart stuff
rm -fr %{buildroot}/etc/init/


%post
%systemd_post thermald.service


%preun
%systemd_preun thermald.service


%postun
%systemd_postun_with_restart thermald.service


%files
%doc README.txt
%license COPYING
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.thermald.conf
%config(noreplace) %{_sysconfdir}/thermald/thermal-conf.xml
%config(noreplace) %{_sysconfdir}/thermald/thermal-cpu-cdev-order.xml
%{_unitdir}/thermald.service
%{_sbindir}/thermald
%{_datadir}/dbus-1/system-services/org.freedesktop.thermald.service
%{_mandir}/man5/thermal-conf.xml.5.gz
%{_mandir}/man8/thermald.8.gz


%changelog
