Name:		texlive-zx-calculus
Version:	69455
Release:	1
Summary:	A library to typeset ZX Calculus diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zx-calculus
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zx-calculus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zx-calculus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This library (based on the great TikZ and TikZ-cd packages)
allows you to typeset ZX-calculus directly in LaTeX. It comes
with many pre-built wire shapes, a highly customizable node
style (with multiple flavours for putting labels inside or
outside nodes), and a "debugging" mode to avoid getting lost in
big diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/zx-calculus
%doc %{_texmfdistdir}/doc/latex/zx-calculus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
