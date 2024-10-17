%define upstream_name    Makefile-DOM
%define upstream_version 0.004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Tokens representing ordinary white space
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Makefile/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Clone)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Params::Util)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'MDOM::Node' class provides an abstract base class for the Element
classes that are able to contain other elements the MDOM::Document manpage,
the MDOM::Statement manpage, and the MDOM::Structure manpage.

As well as those listed below, all of the methods that apply to the
MDOM::Element manpage objects also apply to 'MDOM::Node' objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


