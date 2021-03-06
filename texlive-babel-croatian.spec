# revision 30260
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-croatian
Version:	1.3l
Release:	2
Summary:	TeXLive babel-croatian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-croatian package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-croatian/croatian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-croatian/croatian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-croatian/croatian.dtx
%doc %{_texmfdistdir}/source/generic/babel-croatian/croatian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
