Summary:	Automatic generator of unit tests for C/C++ libraries
Name:		api-sanity-checker
Version:	1.98.7
Release:	1
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		https://github.com/lvc/api-sanity-checker/
Source0:	https://github.com/lvc/api-sanity-checker/archive/refs/tags/%{version}.tar.gz
Requires:	gcc-c++
Requires:	binutils
BuildArch:	noarch
BuildRequires:	abi-compliance-checker

%description
API Sanity Checker (ASC) is an automatic generator of basic unit tests
for shared C/C++ libraries. It is able to generate reasonable (in most,
but unfortunately not all, cases) input data for parameters and compose
simple ("sanity" or "shallow"-quality) test cases for every function in
the API through the analysis of declarations in header files. The quality
of generated tests allows to check absence of critical errors in simple
use cases. The tool is able to build and execute generated tests and
detect crashes (segfaults), aborts, all kinds of emitted signals,
non-zero program return code and program hanging. It may be considered
as a tool for out-of-the-box low-cost sanity checking (fuzzing) of the
library API or as a test development framework for initial generation
of templates for advanced tests. Also it supports universal T2C format
of tests, random test generation mode, specialized data types and other
useful features.

%prep
%autosetup -p1

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/api-sanity-checker
