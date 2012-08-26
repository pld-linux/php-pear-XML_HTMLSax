%define		_status		stable
%define		_pearname	XML_HTMLSax
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - a SAX based parser for HTML and other badly formed XML documents
Summary(pl.UTF-8):	%{_pearname} - analizator SAX dla HTML-a i innych źle sformułowanych dokumentów XML
Name:		php-pear-%{_pearname}
Version:	3.0.0
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	73b75ef6d68c74115b6da8d151293633
URL:		http://pear.php.net/package/XML_HTMLSax/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.5
Requires:	php-pear
Obsoletes:	php-pear-XML_HTMLSax-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_HTMLSax is a SAX based XML parser for badly formed XML documents,
such as HTML. The original code base was developed by Alexander Zhukov
and published at http://sourceforge.net/projects/phpshelve/, who in
turn was inspired by the Python HTMLSax package. Alexander kindly gave
permission to modify the code and license for inclusion in PEAR.
PEAR::XML_HTMLSax takes the last release from Sourceforge
(HTMLSax2002082201) and changes the API to make using HTMLSax very
similar to using the native PHP Expat extension, opening it up for use
with projects like SAX filters:
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
This version also fixes some bugs and adds further features such as
the ability to handle processing instructions and JSP/ASP markup.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_HTMLSax to oparty na SAX analizator XML-a dla źle sformułowanych
dokumentów XML, takich jak HTML. Oryginalny kod został stworzony przez
Alexandra Zhukova i opublikowany pod
http://sourceforge.net/projects/phpshelve/, który z kolei był
inspirowany pakietem HTMLSax dla Pythona. Alexander pozwolił na
modyfikowanie kodu i licencjonowanie do włączenia do PEAR.
PEAR::XML_HTMLSax wywodzi się z ostatniej wersji z Sourceforge
(HTMLSax2002082201) i ma zmienione API, aby można było używać HTMLSax
bardzo podobnie do natywnego rozszerzenia PHP Expat, pozwalając na
używanie w projektach typu filtry SAX:
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Ta wersja dodatkowo poprawia kilka błędów i dodaje nowe możliwości,
takie jak obsługa przetwarzania instrukcji i znaczników JSP/ASP.

Ta klasa ma w PEAR status: %{_status}.

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
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/XML/HTMLSax
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/HTMLSax/*.php
