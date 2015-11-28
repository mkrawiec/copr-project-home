Name:           hubicfuse
Version: 2.1.0
Release:        1%{?dist}
Summary:        A fuse filesystem to access HubiC cloud storage

License:        MIT
Url:            https://github.com/TurboGit/hubicfuse
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  file-devel


%description
HubicFuse is a FUSE application which provides access to Hubic's cloud files
via a mount-point.


%prep
%autosetup


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%defattr(-,root,root,-)
/usr/bin/hubicfuse
%doc


%changelog
