# ToDo:
# - pl summary/description
%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       HTMLSax
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - A SAX based parser for HTML and other badly formed XML documents
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	795b38020a9984440f57312b0c80b438
URL:		http://pear.php.net/
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
