Name:       mp3diags
Version: 1.2.02
Release:    1%{?dist}
Summary:    Tool for finding and fixing problems in MP3 files
License:    GPLv2
Url:        http://mp3diags.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  qt-devel 
BuildRequires:  zlib-devel
BuildRequires:  boost-devel 
BuildRequires:  boost-devel-static 
BuildRequires:  gcc-c++


%description
Finds problems in MP3 files and helps the user to fix many of them using included tools. 
Looks at both the audio part (VBR info, quality, normalization) and the tags containing track 
information (ID3.) Also includes a tag editor and a file renamer.

%prep
%autosetup

./AdjustMt.sh

%build
pushd src
qmake-qt4
lrelease-qt4 src.pro
%__make %{?_smp_flags}
popd #src

%install
%__install -D -m0755 bin/MP3Diags "%{buildroot}%{_bindir}/MP3Diags"
%__ln_s MP3Diags "%{buildroot}%{_bindir}/mp3diags"

%__install -D -m0644 desktop/MP3Diags.desktop "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%__install -D -m0644 desktop/MP3Diags48.png "%{buildroot}%{_datadir}/pixmaps/MP3Diags.png"

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%files
%defattr(-,root,root)
%{_bindir}/mp3diags
%{_bindir}/MP3Diags
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/MP3Diags.png