%define upstream_name    UNIVERSAL-isa
%define upstream_version 1.20120726

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.20120726
Release:	3

Summary:	Hack around calling UNIVERSAL::isa() as a function
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-isa-1.20120726.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*

%changelog
* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.140-1mdv2011.0
+ Revision: 685753
- new version

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 401984
- rebuild using %%perl_convert_version

* Thu Jun 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2010.0
+ Revision: 389097
- update to new version 1.03

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2010.0
+ Revision: 383545
- update to new version 1.02

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 279089
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.06-7mdv2009.0
+ Revision: 242112
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-5mdv2008.0
+ Revision: 87074
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-4mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-3mdk
- Fix SPEC according to Perl Policy
    - BuildRequires
    - Source URL

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdk
- fix buildrequires

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- New release 0.06

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- New release 0.05

* Tue Sep 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdk
- first mdk release


