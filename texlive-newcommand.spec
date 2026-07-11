%global tl_name newcommand
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Generate new LaTeX command definitions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/newcommand
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcommand.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Generating any other than the simple \newcommand-style commands, in
LaTeX, is tedious (in the least). This script allows the specification
of commands in a 'natural' style; the script then generates macros to
define the command.

