%define module  UNIVERSAL-isa
%define name    perl-%{module}
%define version 1.01
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Hack around calling UNIVERSAL::isa() as a function
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/UNIVERSAL/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(CGI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Whenever you use "isa" in UNIVERSAL as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but if they use
UNIVERSAL::isa (the module whose docs you are reading), the kittens can live
long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure that if it's
called as a function on objects which override isa, isa will be called on those
objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*

