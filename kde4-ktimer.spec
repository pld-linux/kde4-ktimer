%define		_state		stable
%define		orgname		ktimer
%define		qtver		4.8.1

Summary:	K Desktop Environment - Task Scheduler
Name:		kde4-%{orgname}
Version:	4.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	237385d86f6866704245ade7162c0562
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kaccessible >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTimer is a little tool to execute programs after some time.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_desktopdir}/kde4/kmouth.desktop
%{_datadir}/config/kmouthrc
%dir %{_datadir}/apps/kmouth
%{_datadir}/apps/kmouth/kmouthui.rc
%{_datadir}/apps/kmouth/icons
%{_datadir}/apps/kmouth/phrasebookdialogui.rc
%dir %{_datadir}/apps/kmouth/books
%lang(de) %{_datadir}/apps/kmouth/books/de
%lang(sv) %{_datadir}/apps/kmouth/books/sv
%{_datadir}/apps/kmouth/books/en
%{_iconsdir}/hicolor/*/apps/kmouth.png
%{_docdir}/kde/HTML/en/kmouth
%{_mandir}/man1/kmouth.1*
