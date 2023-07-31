#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Data-Printer
Version  : 1.001001
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-1.001001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-1.001001.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-printer-perl/libdata-printer-perl_0.40-1.debian.tar.xz
Summary  : 'colored & full-featured pretty print of Perl data structures and objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Printer-license = %{version}-%{release}
Requires: perl-Data-Printer-perl = %{version}-%{release}
Requires: perl(Clone::PP)
Requires: perl(Sort::Naturally)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Moo::Role)
BuildRequires : perl(Moose::Role)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Data::Printer
=============
[![Coverage Status](https://coveralls.io/repos/garu/Data-Printer/badge.png)](https://coveralls.io/r/garu/Data-Printer)
[![CPAN version](https://badge.fury.io/pl/Data-Printer.png)](http://badge.fury.io/pl/Data-Printer)

%package dev
Summary: dev components for the perl-Data-Printer package.
Group: Development
Provides: perl-Data-Printer-devel = %{version}-%{release}
Requires: perl-Data-Printer = %{version}-%{release}

%description dev
dev components for the perl-Data-Printer package.


%package license
Summary: license components for the perl-Data-Printer package.
Group: Default

%description license
license components for the perl-Data-Printer package.


%package perl
Summary: perl components for the perl-Data-Printer package.
Group: Default
Requires: perl-Data-Printer = %{version}-%{release}

%description perl
perl components for the perl-Data-Printer package.


%prep
%setup -q -n Data-Printer-1.001001
cd %{_builddir}
tar xf %{_sourcedir}/libdata-printer-perl_0.40-1.debian.tar.xz
cd %{_builddir}/Data-Printer-1.001001
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Printer-1.001001/deblicense/
pushd ..
cp -a Data-Printer-1.001001 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Printer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Printer/3c118aa664530e21bda2161d5abc8f87b629f9e0 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DDP.3
/usr/share/man/man3/Data::Printer.3
/usr/share/man/man3/Data::Printer::Config.3
/usr/share/man/man3/Data::Printer::Filter.3
/usr/share/man/man3/Data::Printer::Filter::ContentType.3
/usr/share/man/man3/Data::Printer::Filter::DB.3
/usr/share/man/man3/Data::Printer::Filter::DateTime.3
/usr/share/man/man3/Data::Printer::Filter::Digest.3
/usr/share/man/man3/Data::Printer::Filter::Web.3
/usr/share/man/man3/Data::Printer::Object.3
/usr/share/man/man3/Data::Printer::Profile.3
/usr/share/man/man3/Data::Printer::Profile::Dumper.3
/usr/share/man/man3/Data::Printer::Profile::JSON.3
/usr/share/man/man3/Data::Printer::Theme.3
/usr/share/man/man3/Data::Printer::Theme::Classic.3
/usr/share/man/man3/Data::Printer::Theme::Material.3
/usr/share/man/man3/Data::Printer::Theme::Monokai.3
/usr/share/man/man3/Data::Printer::Theme::Solarized.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Printer/3c118aa664530e21bda2161d5abc8f87b629f9e0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
