%define name iozone3
%define version 281
%define release %mkrel 1

Summary: Filesystem characterization & benchmark tool
Name: %{name}
Version: %{version}
Release: %{release}
License: Public Domain
Group: Monitoring
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://www.iozone.org/src/current/%{name}_%{version}.tar.bz2
URL: http://www.iozone.org/
Obsoletes: iozone
Provides: iozone

%description
This program allows one to characterize the filesystem performance
of vendors platform. It supports single stream, throughput, 
pthreads, async I/O and much more.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}_%{version}

%build 
cd src/current
make linux 

%install
cd $RPM_BUILD_DIR/%{name}_%version/src/current/
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 iozone $RPM_BUILD_ROOT%{_bindir}
install -m 755 gnu3d.dem $RPM_BUILD_ROOT%{_bindir}
install -m 755 gengnuplot.sh $RPM_BUILD_ROOT%{_bindir}
install -m 755 fileop $RPM_BUILD_ROOT%{_bindir}
install -m 755 Generate_Graphs $RPM_BUILD_ROOT%{_bindir}

cd $RPM_BUILD_DIR/%{name}_%version/docs
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (0644,root,root,755) 
%doc docs/*.gz src/current/Gnuplot.txt docs/*.pdf docs/*.doc
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*


