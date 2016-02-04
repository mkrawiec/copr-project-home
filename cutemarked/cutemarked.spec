Name:       cutemarked
Summary:    Qt Markdown Editor
License:    GPLv2
Version: 0.11.2
Release:    1%{?dist}
Url:        http://cloose.github.io/CuteMarkEd
Source0:    %{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-qttools-devel
BuildRequires: pkgconfig(Qt5Core) >= 5.2.0
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(hunspell)
BuildRequires: libmarkdown-devel

Requires(post): gtk-update-icon-cache
Requires(postun): gtk-update-icon-cache


%description
A Qt-based, free and open source markdown editor with live HTML preview,
math expressions, code syntax highlighting and syntax highlighting of markdown
document.


%package plugin-fontawesome
Summary:    Qt Iconengine - Fontawesome plugin
License:    BSD

%description plugin-fontawesome
This package provides the fontawesome iconengine plugin


%prep
%autosetup


%build
%{_qt5_qmake} \
    lupdate=lupdate-qt5 \
    lrelease=lrelease-qt5 \

make %{?_smp_mflags}


%install
%make_install INSTALL_ROOT=%{buildroot}

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%files plugin-fontawesome
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/iconengines/libfontawesomeicon.so
/usr/%_lib/qt5/plugins/iconengines


%changelog
