Name:       baka-mplayer
Summary:    The mpv based media player
License:    GPLv2
Group:      Applications/Multimedia
Version: 2.0.3
Release:    1%{?dist}
Url:        http://bakamplayer.u8sand.net/
Source0:    %{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires: gcc-c++
BuildRequires: qt5-qttools-devel
BuildRequires: pkgconfig(Qt5Core) >= 5.2.0
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(mpv)

Requires: youtube-dl

Requires(post): gtk-update-icon-cache
Requires(postun): gtk-update-icon-cache


%description
Baka MPlayer is a free and open source, cross-platform, libmpv based multimedia
player. Its simple design reflects the idea for an uncluttered, simple and
enjoyable environment for watching tv shows.


%prep
%autosetup


%build
%{_qt5_qmake} src/Baka-MPlayer.pro \
    CONFIG+="release install_translations man.extra" \
    lupdate=lupdate-qt5 \
    lrelease=lrelease-qt5 \

make %{?_smp_mflags}


%install
%make_install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%files
%defattr(-,root,root,-)
%doc DOCS/%{name}.md LICENSE
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop


%changelog
