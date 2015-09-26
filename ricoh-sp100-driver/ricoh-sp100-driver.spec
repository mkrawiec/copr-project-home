Name:       ricoh-sp100-driver
Version: 0.4.20150927gitbc2c48
Release:    1%{?dist}
Summary:    CUPS driver for Ricoh Aficio SP 100 familty printers
License:    GPLv2
Url:        https://github.com/droidzone/ricoh-sp100

Source0:    %{name}-%{version}.tar.gz

BuildRequires:  cups-devel

Requires:       jbigkit
Requires:       ImageMagick
Requires:       ghostscript-core
Requires:       inotify-tools

%description
Driver and CUPS filter for Ricoh Aficio SP-100, SP-111 and SP-200 family laser
printers

%prep
%autosetup

%install
install -D -m 0755 pstoricohddst-gdi %{buildroot}%{_cups_serverbin}/filter/pstoricohddst-gdi
install -D -m 0644 RICOH_Aficio_SP_100.ppd %{buildroot}%{_datadir}/ppd/Ricoh/RICOH_Aficio_SP_100.ppd
install -D -m 0644 RICOH_Aficio_SP_111.ppd %{buildroot}%{_datadir}/ppd/Ricoh/RICOH_Aficio_SP_111.ppd
install -D -m 0644 RICOH_Aficio_SP_204.ppd %{buildroot}%{_datadir}/ppd/Ricoh/RICOH_Aficio_SP_204.ppd

%files
%{_cups_serverbin}/filter/pstoricohddst-gdi
%{_datadir}/ppd/Ricoh/*.ppd

%changelog
