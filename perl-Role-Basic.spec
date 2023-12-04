#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Role-Basic
Version  : 0.13
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/O/OV/OVID/Role-Basic-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OV/OVID/Role-Basic-0.13.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/librole-basic-perl/librole-basic-perl_0.13-2.debian.tar.xz
Summary  : 'Just roles. Nothing else.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Role-Basic-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Role-Basic
INSTALLATION
To install this module, run the following commands:
perl Build.PL
./Build
./Build test
./Build install

%package dev
Summary: dev components for the perl-Role-Basic package.
Group: Development
Provides: perl-Role-Basic-devel = %{version}-%{release}
Requires: perl-Role-Basic = %{version}-%{release}

%description dev
dev components for the perl-Role-Basic package.


%package perl
Summary: perl components for the perl-Role-Basic package.
Group: Default
Requires: perl-Role-Basic = %{version}-%{release}

%description perl
perl components for the perl-Role-Basic package.


%prep
%setup -q -n Role-Basic-0.13
cd %{_builddir}
tar xf %{_sourcedir}/librole-basic-perl_0.13-2.debian.tar.xz
cd %{_builddir}/Role-Basic-0.13
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Role-Basic-0.13/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Role::Basic.3
/usr/share/man/man3/Role::Basic::Philosophy.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
