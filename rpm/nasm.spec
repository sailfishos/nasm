#specfile originally created for Fedora, modified for Moblin Linux
# -*- coding: utf-8 -*-
Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 3.02
Release: 1
License: BSD
URL: http://www.nasm.us
Source0: %{name}-%{version}.tar.xz
Source1: nasm.sh
BuildRequires: perl

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%autogen
%configure
%make_build

%install
# Dummy manpages so install doesn't fail
touch nasm.1 ndisasm.1
%make_install
install -D -t %{buildroot}%{_sysconfdir}/profile.d %{SOURCE1}

%files
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_sysconfdir}/profile.d/nasm.sh
%exclude %{_datadir}/man
