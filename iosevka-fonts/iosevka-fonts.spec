%global fontname iosevka
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version: 1.0beta2
Release:        1%{?dist}
Summary:        A programmer's typeface

Group:          User Interface/X
License:        OFL
URL:            https://github.com/be5invis/Iosevka
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Iosevka is a monospace coding typeface inspired by Pragmata Pro, M+ and PF DIN
Mono. It is designed to have a narrow shape to be space efficient and
compatible to CJK characters.

%prep
%setup -q

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc


%changelog

