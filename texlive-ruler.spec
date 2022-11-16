Name:		texlive-ruler
Version:	54251
Release:	1
Summary:	A typographic ruler for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ruler
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ruler.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file processes to produce (real) rulers; the author
suggests printing them on transparent plastic and trimming for
use as a "real" ruler. The rule widths are 0.05mm, which can be
challenging for (old) laser printers.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/ruler

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
