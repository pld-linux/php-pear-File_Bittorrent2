%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Bittorrent2
%define		_status		stable
%define		_pearname	File_Bittorrent2
Summary:	%{_pearname} - Decode and Encode data in Bittorrent format
Summary(pl.UTF-8):	%{_pearname} - Kodowanie i dekodowanie danych w formacie Bittorrent
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	64dc1a1756ddf92992be98a1453190d9
URL:		http://pear.php.net/package/File_Bittorrent2/
BuildRequires:	php-pear-PEAR-core
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of three classes which handles the encoding and
decoding of data in Bittorrent format.

You can also extract useful informations from .torrent files, create
.torrent files and query the torrent's scrape page to get its
statistics.

PHP5 only.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza dwie klasy obsługujące kodowanie i dekodowanie
danych w formacie Bittorent.

Można także wydobyć wiele przydatnych informacji z plików .torrent
oraz pobrać statystykę ze strony danego torrenta.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/File_Bittorrent2/{example.php,example_mktorrent.php,install-x86-universal-2005.0.iso.torrent,scrape.php,torrentinfo.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/Bittorrent2

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/File_Bittorrent2
