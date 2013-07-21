%define name iozone3
%define version 397
%define release %mkrel 1

Summary:	Filesystem characterization & benchmark tool
Name:		%{name}
Version:	414
Release:	1
License:	Public Domain
Group:		Monitoring
URL:		http://www.iozone.org/
Source0:	http://www.iozone.org/src/current/iozone3_414.tar
Obsoletes:	iozone < %{version}
Provides:	iozone
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program allows one to characterize the filesystem performance
of vendors platform. It supports single stream, throughput, 
pthreads, async I/O and much more.

%prep
%setup -n %{name}_%{version}

%build
cd src/current
%make linux CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
cd $RPM_BUILD_DIR/%{name}_%{version}/src/current/
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 iozone %{buildroot}%{_bindir}
install -m 755 gnu3d.dem %{buildroot}%{_bindir}
install -m 755 gengnuplot.sh %{buildroot}%{_bindir}
install -m 755 fileop %{buildroot}%{_bindir}
install -m 755 Generate_Graphs %{buildroot}%{_bindir}

cd $RPM_BUILD_DIR/%{name}_%{version}/docs
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 iozone.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc docs/*.gz src/current/Gnuplot.txt docs/*.pdf docs/*.doc
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Nov 04 2011 Andrey Bondrov <abondrov@mandriva.org> 397-1
+ Revision: 717624
- New version 397

  + Stéphane Téletchéa <steletch@mandriva.org>
    - update to new version 373

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 326-2mdv2011.0
+ Revision: 619675
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 326-1mdv2010.0
+ Revision: 440691
- update to new version 326
- compile with %%optflags and %%ldflags
- spec file clean

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 287-4mdv2010.0
+ Revision: 429516
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 287-3mdv2009.0
+ Revision: 247242
- rebuild

* Tue Feb 26 2008 Erwan Velu <erwan@mandriva.org> 287-1mdv2008.1
+ Revision: 175414
- release 287

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 281-1mdv2008.1
+ Revision: 131599
- kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Lenny Cartier <lenny@mandriva.com> 281-1mdv2007.0
+ Revision: 115813
- Import iozone3


