%global tl_name babel-croatian
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3l
Release:	%{tl_revision}.1
Summary:	Babel contributed support for Croatian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/croatian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-croatian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package establishes Croatian conventions in a document (or a subset
of the conventions, if Croatian is not the main language of the
document).

