Summary:	Automatic generator of unit tests for C/C++ libraries
Name:		api-sanity-checker
Version:	1.12.9
Release:	%mkrel 3
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		http://forge.ispras.ru/projects/api-sanity-autotest
Source0:	http://forge.ispras.ru/attachments/download/1278/api-sanity-checker-%{version}.tar.gz
Requires:	gcc-c++
Requires:	binutils
BuildRequires:  help2man
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q
chmod 0644 LICENSE.txt
chmod 0755 %{name}.pl
cp %{name}.pl %{name}
# Generate man page
help2man -N --no-discard-stderr --help-option="--info" -o %{name}.1 ./%{name}
sed -i 's/\(.\)/\n\1/' %{name}.1
sed -i 's/API "1"/API-SANITY-CHECKER "1"/' %{name}.1

%build
# Nothing to build.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_mandir}/man1/*
%doc LICENSE.txt doc/*
%{_bindir}/%{name}
