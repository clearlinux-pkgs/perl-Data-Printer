#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Printer
Version  : 0.40
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-0.40.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-0.40.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-printer-perl/libdata-printer-perl_0.40-1.debian.tar.xz
Summary  : 'colored pretty-print of Perl data structures and objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Printer-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone::PP)
BuildRequires : perl(File::HomeDir)
BuildRequires : perl(File::Which)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Sort::Naturally)
BuildRequires : perl(Try::Tiny)

%description
## Data::Printer ##
Data::Printer is a Perl module to pretty-print Perl data structures
and objects in full color. It is meant to display variables on
screen, properly formatted to be inspected by a human.

%package dev
Summary: dev components for the perl-Data-Printer package.
Group: Development
Provides: perl-Data-Printer-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Printer package.


%package license
Summary: license components for the perl-Data-Printer package.
Group: Default

%description license
license components for the perl-Data-Printer package.


%prep
%setup -q -n Data-Printer-0.40
cd ..
%setup -q -T -D -n Data-Printer-0.40 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-Printer-0.40/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Printer
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Printer/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.0/DDP.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Printer.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Printer/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Printer/Filter/DB.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Printer/Filter/DateTime.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Printer/Filter/Digest.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DDP.3
/usr/share/man/man3/Data::Printer.3
/usr/share/man/man3/Data::Printer::Filter.3
/usr/share/man/man3/Data::Printer::Filter::DB.3
/usr/share/man/man3/Data::Printer::Filter::DateTime.3
/usr/share/man/man3/Data::Printer::Filter::Digest.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Printer/deblicense_copyright
