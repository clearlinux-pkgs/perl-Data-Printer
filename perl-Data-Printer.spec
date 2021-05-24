#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Printer
Version  : 1.000004
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-1.000004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-1.000004.tar.gz
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
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Try::Tiny)

%description
Data::Printer
=============
[![Build status](https://travis-ci.org/garu/Data-Printer.svg?branch=master)](https://travis-ci.org/garu/Data-Printer)
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
%setup -q -n Data-Printer-1.000004
cd %{_builddir}
tar xf %{_sourcedir}/libdata-printer-perl_0.40-1.debian.tar.xz
cd %{_builddir}/Data-Printer-1.000004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Printer-1.000004/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Printer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Printer/3c118aa664530e21bda2161d5abc8f87b629f9e0
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
/usr/lib/perl5/vendor_perl/5.34.0/DDP.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Common.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Config.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/ARRAY.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/CODE.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/ContentType.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/DB.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/DateTime.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/Digest.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/FORMAT.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/GLOB.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/GenericClass.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/HASH.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/REF.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/Regexp.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/SCALAR.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/VSTRING.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Filter/Web.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Object.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Profile.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Profile/Dumper.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Profile/JSON.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Theme.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Theme/Classic.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Theme/Material.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Theme/Monokai.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Printer/Theme/Solarized.pm
