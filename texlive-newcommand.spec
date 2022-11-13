Name:		texlive-newcommand
Version:	18704
Release:	1
Summary:	Generate new LaTeX command definitions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/newcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
