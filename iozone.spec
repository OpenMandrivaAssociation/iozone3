%define name iozone3
%define version 373
%define release %mkrel 1

Summary:	Filesystem characterization & benchmark tool
Name:		iozone3
Version:	326
Release:	%mkrel 2
License:	Public Domain
Group:		Monitoring
URL:		http://www.iozone.org/
Source0:	http://www.iozone.org/src/current/%{name}_%{version}.tar.bz2
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
