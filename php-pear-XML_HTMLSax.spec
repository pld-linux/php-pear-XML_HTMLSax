%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       HTMLSax
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - A SAX based parser for HTML and other badly formed XML documents
Summary(pl):	%{_pearname} - analizator SAX dla HTML i innych ¼le sformu³owanych dokumentów XML
Name:		php-pear-%{_pearname}
Version:	2.1.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f2cd9ea8ed1c59cc3046675d41c7cf98
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

This class has in PEAR status: %{_status}.

%description -l pl
XML_HTMLSax to oparty na SAX analizator XML do ¼le sformu³owanych
dokumentów XML, takich jak HTML. Oryginalny kod zosta³ stworzony przez
Alexandra Zhukova i opublikowany pod
http://sourceforge.net/projects/phpshelve/, który z kolei by³
inspirowany pakietem HTMLSax dla Pythona. Alexander pozwoli³ na
modyfikowanie kodu i licencjonowanie do w³±czenia do PEAR.
PEAR::XML_HTMLSax wywodzi siê z ostatniej wersji z Sourceforge
(HTMLSax2002082201) i ma zmienione API, aby mo¿na by³o u¿ywaæ HTMLSax
bardzo podobnie do natywnego rozszerzenia PHP Expat, pozwalaj±c na
u¿ywanie w projektach typu filtry SAX:
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Ta wersja dodatkowo poprawia kilka b³êdów i dodaje nowe mo¿liwo¶ci,
takie jak obs³uga przetwarzania instrukcji i znaczników JSP/ASP.

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
%doc %{_pearname}-%{version}/docs
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
