%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	XBM
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate XBM images
Summary(pl):	%{_pearname} - obr�bka obraz�w XBM
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ac7a8bfd0a526f899797bb810becbfce
URL:		http://pear.php.net/package/Image_XBM/
BuildRequires:	rpm-php-pearprov >= 4.4.2-13
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package for manipulate XBM images.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa do obr�bki obraz�w XBM.

Ta klasa ma w PEAR status: %{_status}.

%prep
# FIXME: remove -f if the package.xml gets fixed!
%pear_package_setup -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
