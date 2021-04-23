#specfile originally created for Fedora, modified for Moblin Linux
# -*- coding: utf-8 -*-
Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 2.15.05
Release: 1
License: BSD
URL: http://www.nasm.us
Source0: %{name}-%{version}.tar.xz
Source1: nasm.sh
BuildRequires: perl
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%autogen
%configure
%make_build

%install
# Dummy manpages so install doesn't fail
touch nasm.1 ndisasm.1
make DESTDIR=%{buildroot} install install_rdf
install -D -t %{buildroot}%{_sysconfdir}/profile.d %{SOURCE1}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_sysconfdir}/profile.d/nasm.sh
%exclude %{_datadir}/man

%files rdoff
%defattr(-,root,root)
%{_bindir}/ldrdf
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com
%{_bindir}/rdfdump
%{_bindir}/rdflib
%{_bindir}/rdx
%{_bindir}/rdf2ith
%{_bindir}/rdf2srec
