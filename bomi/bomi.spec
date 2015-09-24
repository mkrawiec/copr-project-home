Name:       bomi
Summary:    A multimedia player
License:    GPLv2
Group:      Applications/Multimedia
Version: 0.9.11
Release:    1%{?dist}
Url:        http://bomi-player.github.io/
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
# waf is written in Python 2.x.
BuildRequires:  python
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Quick) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2
BuildRequires:  pkgconfig(alsa)
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass) >= 0.12.1
BuildRequires:  pkgconfig(libavcodec) >= 55.34.1
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat) >= 55.12.0
BuildRequires:  pkgconfig(libavutil) >= 52.48.101
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcb-xtest)
# Streaming support for Dailymotion, YouTube, etc.

Requires: youtube-dl
Requires: qt5-qtquickcontrols

%description
bomi is a themable Qt-based multimedia player based on the MPV
video backend which is aimed for easy usage but also provides
various powerful features and convenience functions.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure \
  --release                             \
  %{?jobs:--parallel=%{jobs}}           \
  --prefix=%{_prefix}                   \
  --actiondir=%{_datadir}/solid/actions
make %{?_smp_mflags}

%install
make DEST_DIR=%{?buildroot:%{buildroot}} install

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%files
%defattr(-,root,root)
%doc CHANGES.txt COPYING.txt CREDITS.txt GPL.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*.1.gz
%dir %{_datadir}/solid/
%dir %{_datadir}/solid/actions/
%{_datadir}/solid/actions/*
%{_datadir}/bash-completion/completions/%{name}

%changelog