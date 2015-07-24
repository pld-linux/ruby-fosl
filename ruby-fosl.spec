%define	pkgname	fosl
Summary:	A Ruby API for reading lsof(1) output
Name:		ruby-%{pkgname}
Version:	0.0.2
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	bdd7bcd1fba2383ade2ea938fb26b903
URL:		https://github.com/jordansissel/fosl
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	lsof
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Ruby API for reading lsof(1) output.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/fosl
