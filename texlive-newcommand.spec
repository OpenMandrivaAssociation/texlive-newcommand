# revision 18704
# category Package
# catalog-ctan /support/newcommand
# catalog-date 2010-06-02 16:01:13 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-newcommand
Version:	2.0
Release:	11
Summary:	Generate new LaTeX command definitions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/newcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Generating any other than the simple \newcommand-style
commands, in LaTeX, is tedious (in the least). This script
allows the specification of commands in a 'natural' style; the
script then generates macros to define the command.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/newcommand/README
%doc %{_texmfdistdir}/doc/latex/newcommand/newcommand.pdf
%doc %{_texmfdistdir}/doc/latex/newcommand/newcommand.py
%doc %{_texmfdistdir}/doc/latex/newcommand/newcommand.tex
%doc %{_texmfdistdir}/doc/latex/newcommand/spark.py

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 754271
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719109
- texlive-newcommand
- texlive-newcommand
- texlive-newcommand
- texlive-newcommand

