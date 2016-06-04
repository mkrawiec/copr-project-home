Name: aqemu
Version: 0.9.2
Release: 1%{?dist}
Summary: A QT graphical interface to QEMU and KVM
Group: Applications/Emulators
License: GPLv2+
URL: https://github.com/tobimensch/aqemu
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core) >= 5.2.0
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: libvncserver-devel
BuildRequires: desktop-file-utils
BuildRequires: gnutls-devel
BuildRequires: hicolor-icon-theme

%description
AQEMU is a graphical user interface to QEMU and KVM, written in Qt4. The
program has a user-friendly interface and allows user to set the
majority of QEMU and KVM options on their virtual machines.

%prep
%autosetup
sed -i -e 's/COMMAND rcc/COMMAND rcc-qt5/g' CMakeLists.txt

%build
%cmake
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# Copy 48x48 and 64x64 icons to correct location.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,64x64}/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}_48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mv %{buildroot}%{_datadir}/pixmaps/%{name}_64x64.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
# Remove directories from install which are not being deployed in RPM.
rm -rf %{buildroot}%{_datadir}/pixmaps
rm -rf %{buildroot}%{_datadir}/menu
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# Validate the icon file.
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/%{name}
%doc AUTHORS CHANGELOG COPYING TODO
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
