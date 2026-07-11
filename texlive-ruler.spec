%global tl_name ruler
%global tl_revision 54251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A typographic ruler for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/ruler.tex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ruler.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The file processes to produce (real) rulers; the author suggests
printing them on transparent plastic and trimming for use as a "real"
ruler. The rule widths are 0.05mm, which can be challenging for (old)
laser printers.

