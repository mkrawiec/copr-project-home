%define path_man_en %{_builddir}/%{name}-%{version}/man/en

Name: libchardet
Version: 1.0.4
Release: 2%{?dist}
Summary: Mozilla Universal Chardet library

Group: System Environment/Libraries
License: MPLv1.1 or GPLv2+
URL: http://oops.org
Source0: http://mirror.oops.org/pub/oops/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++

%description
libchardet provides an interface to Mozilla's universal charset detector,
which detects the charset used to encode data.

%package devel
Summary: Header and object files for development using libchardet
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}, libstdc++-devel

%description devel
The libchardet-devel package contains the header and object files necessary
for developing programs which use the libchardet libraries.

%prep
%setup -q

# Fix rpmlint file-not-utf8
for i in detect_init.3 detect_obj_free.3 detect_obj_init.3 detect_reset.3 ; do
  iconv --from=ISO-8859-1 --to=UTF-8 %{path_man_en}/$i > %{path_man_en}/$i.conv
  mv %{path_man_en}/$i.conv %{path_man_en}/$i
done

%build
%configure --disable-static

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%defattr(0755,root,root)
%{_libdir}/%{name}.so.*
%doc LICENSE Changelog

%files devel
#%defattr(0644,root,root,0755)
#%attr(0755,root,root) 
%{_bindir}/chardet-config
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/chardet.pc
%{_includedir}/chardet/*.h
%{_mandir}/man3/*
%lang(ko) %{_mandir}/ko/man3/*

%changelog
