%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	HTMLSax
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a SAX based parser for HTML and other badly formed XML documents
Summary(pl):	%{_pearname} - analizator SAX dla HTML-a i innych �le sformu�owanych dokument�w XML
Name:		php-pear-%{_pearname}
Version:	3.0.0
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	73b75ef6d68c74115b6da8d151293633
URL:		http://pear.php.net/package/XML_HTMLSax/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%description -l pl
XML_HTMLSax to oparty na SAX analizator XML-a dla �le sformu�owanych
dokument�w XML, takich jak HTML. Oryginalny kod zosta� stworzony przez
Alexandra Zhukova i opublikowany pod
http://sourceforge.net/projects/phpshelve/, kt�ry z kolei by�
inspirowany pakietem HTMLSax dla Pythona. Alexander pozwoli� na
modyfikowanie kodu i licencjonowanie do w��czenia do PEAR.
PEAR::XML_HTMLSax wywodzi si� z ostatniej wersji z Sourceforge
(HTMLSax2002082201) i ma zmienione API, aby mo�na by�o u�ywa� HTMLSax
bardzo podobnie do natywnego rozszerzenia PHP Expat, pozwalaj�c na
u�ywanie w projektach typu filtry SAX:
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Ta wersja dodatkowo poprawia kilka b��d�w i dodaje nowe mo�liwo�ci,
takie jak obs�uga przetwarzania instrukcji i znacznik�w JSP/ASP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,tests}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
