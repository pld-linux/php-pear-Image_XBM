%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	XBM
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate XBM images
Summary(pl.UTF-8):   %{_pearname} - obróbka obrazów XBM
Name:		php-pear-%{_pearname}
Version:	0.9.0
%define	_rc RC1
%define	_rel 1
Release:	%{_rc}.%{_rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	b31e294640e1e2370a0270288364469e
URL:		http://pear.php.net/package/Image_XBM/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Text/Figlet.*)'

%description
Package for manipulate XBM images.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa do obróbki obrazów XBM.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/data/%{_pearname}/docs/* docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
