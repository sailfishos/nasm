#specfile originally created for Fedora, modified for Moblin Linux
# -*- coding: utf-8 -*-
Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 2.09.10
Release: 1
License: simplified BSD license
Group: Development/Languages
URL: http://nasm.sourceforge.net/
Source0: nasm-%{version}.tar.bz2
Source1: nasm-%{version}-xdoc.tar.bz2
Source2: nasm.sh
BuildRequires: perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info


%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM
Group: Development/Tools

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup -q
tar xjf %{SOURCE1} --strip-components 1

%build
%configure
make all
#gzip -9f doc/nasmdoc.{ps,txt}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make INSTALLROOT=$RPM_BUILD_ROOT install install_rdf
install -d $RPM_BUILD_ROOT/%{_infodir}
install -m 644 -t $RPM_BUILD_ROOT/%{_infodir} doc/info/*
install -d $RPM_BUILD_ROOT/etc/profile.d
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d/ 

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
[ -e %{_infodir}/nasm.info.gz ] && /sbin/install-info %{_infodir}/nasm.info.gz  %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
  [ -e %{_infodir}/nasm.info.gz ] && /sbin/install-info --delete %{_infodir}/nasm.info.gz %{_infodir}/dir || :
fi

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README TODO
%{_bindir}/nasm
%{_bindir}/ndisasm
%doc %{_mandir}/*/*
%doc %{_infodir}/nasm.info*.gz
/etc/profile.d/nasm.sh


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

